# Universal auto-generated wrapper v2 for 'variance_premium'
from importlib import import_module
import pkgutil, inspect

ROOT_PKG = "agents._vendor.variance_premium"
CAND_FN = ("run","main","execute","process","analyze","analyse","analyzer","standard_run","premium_run","plus_run","generate","compute","handle","entry","entrypoint")

def _callable_accepts_payload(fn):
    try:
        sig = inspect.signature(fn)
        # allow any signature; we'll try with payload then without
        return True
    except Exception:
        return True

def _find_entry_in_module(mod):
    # 1) functions with candidate names
    for name in dir(mod):
        obj = getattr(mod, name)
        lname = name.lower()
        if callable(obj) and lname in CAND_FN:
            return obj
    # 2) classes having candidate methods
    for name in dir(mod):
        obj = getattr(mod, name)
        if inspect.isclass(obj):
            for m in CAND_FN:
                meth = getattr(obj, m, None)
                if callable(meth):
                    try:
                        inst = obj()
                        return getattr(inst, m)
                    except Exception:
                        # constructor may require args; keep scanning
                        continue
    return None

def _find_entry_recursive(root_pkg_name):
    visited = set()
    def iter_pkg(pkg_name):
        if pkg_name in visited:
            return None
        visited.add(pkg_name)
        try:
            pkg = import_module(pkg_name)
        except Exception:
            return None
        entry = _find_entry_in_module(pkg)
        if entry:
            return entry
        if hasattr(pkg, "__path__"):
            for _, name, _ in pkgutil.iter_modules(pkg.__path__, pkg.__name__ + "."):
                entry = iter_pkg(name)
                if entry:
                    return entry
        return None
    return iter_pkg(root_pkg_name)

_ENTRY = _find_entry_recursive(ROOT_PKG)

def run(payload=None):
    if payload is None:
        payload = {}
    if _ENTRY:
        try:
            if _callable_accepts_payload(_ENTRY):
                try:
                    return _ENTRY(payload)
                except TypeError:
                    return _ENTRY()
            else:
                return _ENTRY()
        except Exception as e:
            return {"status":"ERROR","agent":"variance_premium","error":str(e)}
    # Fallback diagnostics so smoke won't crash
    try:
        base = import_module(ROOT_PKG)
        exports = [n for n in dir(base) if not n.startswith("_")]
    except Exception:
        exports = []
    return {"status":"NOOP","agent":"variance_premium","reason":"No runnable entrypoint found","exports":exports}
