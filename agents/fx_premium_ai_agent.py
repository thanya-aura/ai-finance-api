# Universal auto-generated wrapper v3 for 'fx_premium'
from importlib import import_module
import pkgutil, inspect, asyncio

ROOT_PKG = "agents._vendor.fx_premium"
HINTS = ("run","main","execute","process","analyz","analyse","compute","generate","predict","forecast","report","entry","entrypoint","standard","premium","plus","agent")

def _score(name:str)->int:
    n=name.lower()
    s=0
    for k in HINTS:
        if k in n: s+=2
    if n in ("run","main","execute"): s+=5
    if "agent" in n: s+=1
    return s

def _iter_callables(mod):
    # module-level funcs
    for nm in dir(mod):
        if nm.startswith("_"): continue
        obj = getattr(mod, nm, None)
        if callable(obj) and inspect.isfunction(obj):
            yield ("func", f"{mod.__name__}.{nm}", obj, _score(nm))
    # class methods
    for nm in dir(mod):
        if nm.startswith("_"): continue
        cls = getattr(mod, nm, None)
        if inspect.isclass(cls):
            for mname, mobj in inspect.getmembers(cls, predicate=inspect.isfunction):
                if mname.startswith("_"): continue
                # try to instantiate with no-arg
                inst=None
                try:
                    sig=inspect.signature(cls)
                    if all(p.default!=inspect._empty or p.kind in (p.VAR_POSITIONAL,p.VAR_KEYWORD) or p.name=="self"
                           for p in sig.parameters.values()):
                        inst=cls()
                except Exception:
                    pass
                yield ("method", f"{mod.__name__}.{cls.__name__}.{mname}", (inst,mobj), _score(mname)+1)

def _walk(root_pkg_name):
    seen=set(); cand=[]
    def walk(name):
        if name in seen: return
        seen.add(name)
        try:
            m=import_module(name)
        except Exception:
            return
        cand.extend(_iter_callables(m))
        if hasattr(m,"__path__"):
            for _, sub, _ in pkgutil.iter_modules(m.__path__, m.__name__ + "."):
                walk(sub)
    walk(root_pkg_name)
    cand.sort(key=lambda x: x[3], reverse=True)
    return cand

_CANDS = _walk(ROOT_PKG)

def _call_entry(entry, payload):
    import inspect, asyncio
    def _invoke(fn, payload):
        try:
            res = fn(payload)
        except TypeError:
            res = fn()
        if inspect.iscoroutine(res):
            try:
                return asyncio.run(res)
            except RuntimeError:
                # มี event loop อยู่แล้ว
                loop = asyncio.get_event_loop()
                return loop.run_until_complete(res)
        return res
    try:
        # tuple => (instance, method) ที่ wrapper v3 เคยส่งมา
        if isinstance(entry, tuple):
            inst, meth = entry
            if inst is not None:
                return _invoke(lambda p=None: meth(inst, p), payload)
            else:
                return _invoke(meth, payload)
        # function ปกติ
        return _invoke(entry, payload)
    except Exception as e:
        return {"status":"ERROR","agent":"fx_premium","error":str(e)}
def run(payload=None):
    if payload is None: payload={}
    for _, fqname, entry, _ in _CANDS[:10]:  # ลองตัวเต็ง 10 อันดับแรก
        res = _call_entry(entry, payload)
        if isinstance(res, dict) and res.get("status")=="ERROR":
            # ถ้าผิดพลาด ลองตัวถัดไป
            continue
        # สำเร็จ
        return {"status":"OK","agent":"fx_premium","entry":fqname,"result":res}
    # ไม่เจออะไรเรียกได้
    try:
        base = import_module(ROOT_PKG)
        exports = [n for n in dir(base) if not n.startswith("_")]
    except Exception:
        exports = []
    return {"status":"NOOP","agent":"fx_premium","reason":"No callable entrypoint discovered","exports":exports}

