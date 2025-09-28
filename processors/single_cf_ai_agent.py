# auto-generated thin wrapper
try:
    from core.single_cashflow import run as _run
except Exception as e:
    raise ImportError(f"single_cf_ai_agent wrapper could not import core.single_cashflow: {e}")

def run(*args, **kwargs):
    return _run(*args, **kwargs)
