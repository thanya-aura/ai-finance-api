# Auto-generated wrapper for 'margin_plus' (from https://github.com/thanya-aura/ai-margin-api.git)
from importlib import import_module
_mod = import_module("agents._vendor.margin_plus.__init__")

def _pick_entry(mod):
    for fn in ("run","main","execute","process","analyze","analyse","analyzer","standard_run","premium_run","plus_run","generate","compute"):
        f = getattr(mod, fn, None)
        if callable(f):
            return f
    Agent = getattr(mod, "Agent", None)
    if Agent is not None:
        inst = Agent()
        if hasattr(inst, "run") and callable(inst.run):
            return inst.run
    raise AttributeError("No runnable entrypoint found in module: agents._vendor.margin_plus.__init__")

_entry = _pick_entry(_mod)

def run(payload=None):
    if payload is None: payload = {}
    return _entry(payload)
