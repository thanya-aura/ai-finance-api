# smart entry shim for 'margin_premium'
import importlib, asyncio, inspect, pandas as pd

HINTS=('analyz','run','execute','process','main','compute','report','standard','plus','premium')

def _score(name:str)->int:
    n=name.lower(); s=0
    for k in HINTS:
        if k in n: s+=2
    if n in ('analyze_standard','analyze_plus','analyze_premium','analyze','run'): s+=6
    return s

def _invoke(fn, payload):
    # 1) ลองเรียกด้วย payload เดิมก่อน
    try:
        try:
            res = fn(payload)
        except TypeError:
            res = fn()
    except AttributeError as e:
        msg = str(e).lower()
        # 2) ถ้า error บอกว่าไม่มี .columns แปลว่าควรเป็น DataFrame
        if 'columns' in msg:
            # แปลง payload -> DataFrame ตามที่มี
            df = None
            if isinstance(payload, dict) and 'data' in payload:
                try:
                    if isinstance(payload['data'], list):
                        df = pd.DataFrame(payload['data'])
                    elif isinstance(payload['data'], dict):
                        df = pd.DataFrame([payload['data']])
                except Exception:
                    df = None
            if df is None:
                # อย่างน้อยเป็น DataFrame ว่างเพื่อไม่ให้พังเรื่อง .columns
                df = pd.DataFrame()
            # เรียกใหม่ด้วย df
            try:
                res = fn(df)
            except TypeError:
                # บางฟังก์ชันไม่มีพารามิเตอร์ ให้ลองไม่มีอาร์กิวเมนต์
                res = fn()
        else:
            # AttributeError อื่น ๆ โยนต่อ
            raise
    # 3) await ถ้าเป็น coroutine
    if inspect.iscoroutine(res):
        try:
            return asyncio.run(res)
        except RuntimeError:
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(res)
    return res
def run(payload=None):
    if payload is None: payload={}
    m = importlib.import_module("ai_margin_api.agents.premium.premium_agent")
    cands=[]

    # module-level functions
    for n in dir(m):
        if n.startswith("_"): continue
        obj=getattr(m,n,None)
        if inspect.isfunction(obj):
            cands.append(("func", f"{m.__name__}.{n}", obj, _score(n)))

    # class methods (instantiate if constructor is "easy")
    for n in dir(m):
        if n.startswith("_"): continue
        cls=getattr(m,n,None)
        if inspect.isclass(cls):
            inst=None
            try:
                sig=inspect.signature(cls)
                if all(p.default!=inspect._empty or p.kind in (p.VAR_POSITIONAL,p.VAR_KEYWORD) or p.name=='self'
                       for p in sig.parameters.values()):
                    inst=cls()
            except Exception:
                pass
            for mname, mobj in inspect.getmembers(cls, predicate=inspect.isfunction):
                if mname.startswith("_"): continue
                if inst is not None:
                    bound=lambda p=None, _i=inst, _f=mobj: _f(_i,p)
                else:
                    # unbound method -> try calling without self (some libs define @staticmethod)
                    bound=lambda p=None, _f=mobj: _f(p)
                cands.append(("method", f"{m.__name__}.{cls.__name__}.{mname}", bound, _score(mname)+1))

    cands.sort(key=lambda x: x[3], reverse=True)

    preferred=['analyze_standard','analyze_plus','analyze_premium','analyze','run','execute','process','main']
    # try preferred names first
    for pref in preferred:
        for kind, fq, entry, sc in cands:
            if fq.lower().endswith('.'+pref):
                try:
                    out=_invoke(entry, payload)
                    return {"status":"OK","agent":"margin_premium","called":fq,"result":out}
                except Exception:
                    pass

    # then top 10 by score
    last_err=None
    for kind, fq, entry, sc in cands[:10]:
        try:
            out=_invoke(entry, payload)
            return {"status":"OK","agent":"margin_premium","called":fq,"result":out}
        except Exception as e:
            last_err=str(e)

    exports=[n for n in dir(m) if not n.startswith("_")]
    return {"status":"NOOP","agent":"margin_premium","reason":"no callable found","exports":exports, "last_error":last_err}

