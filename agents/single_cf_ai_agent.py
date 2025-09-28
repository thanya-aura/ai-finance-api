# auto-generated thin wrapper (single_cf_ai_agent)
_candidates = ['processors.single_cf_ai_agent', 'core.single_cashflow', 'core.single_cf', 'app.core.single_cashflow', 'app.core.single_cf']
_last_err = None
_run = None
for _m in _candidates:
    try:
        _mod = __import__(_m, fromlist=['run'])
        _run = getattr(_mod, 'run', None)
        if _run:
            break
    except Exception as e:
        _last_err = e

def _fallback_run(*args, **kwargs):
    # postpone the error to call-time, not import-time
    raise NotImplementedError("Wrapper single_cf_ai_agent: underlying run() not found. Tried: " + str(_candidates) + "; last_err=" + repr(_last_err))

if _run is None:
    _run = _fallback_run

def run(*args, **kwargs):
    return _run(*args, **kwargs)
