# lightweight entry shim for 'margin_standard'
import importlib, asyncio, inspect

def _call(fn, payload):
    try:
        res = fn(payload)
    except TypeError:
        res = fn()
    if inspect.iscoroutine(res):
        try:
            return asyncio.run(res)
        except RuntimeError:
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(res)
    return res

def run(payload=None):
    if payload is None:
        payload = {}
    m = importlib.import_module("ai_margin_api.agents.standard.standard_agent")
    fn = None
    for name in 'analyze_standard', 'analyze', 'run':
        f = getattr(m, name, None)
        if callable(f):
            fn = f; break
    if fn is None:
        return {"status":"NOOP","agent":"margin_standard","reason":"no suitable function in ai_margin_api.agents.standard.standard_agent"}
    try:
        out = _call(fn, payload)
        # ให้มีรูปแบบสม่ำเสมอ
        return {"status":"OK","agent":"margin_standard","called":fn.__name__,"result":out}
    except Exception as e:
        return {"status":"ERROR","agent":"margin_standard","error":str(e)}
