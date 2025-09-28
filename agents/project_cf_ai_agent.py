# auto-generated thin wrapper (project_cf_ai_agent)
_candidates = ['core.project_cashflow', 'core.project_cf', 'processors.project_cf_ai_agent']
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
    raise NotImplementedError("Wrapper project_cf_ai_agent: underlying run() not found. Tried: " + str(_candidates) + "; last_err=" + repr(_last_err))

if _run is None:
    _run = _fallback_run

def run(*args, **kwargs):
    return _run(*args, **kwargs)
