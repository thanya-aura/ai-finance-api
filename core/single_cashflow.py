def run(payload: dict) -> dict:
    demo = bool(payload.get("demo", False))
    return {"ok": True, "agent": "single", "demo": demo}