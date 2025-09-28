def run(payload: dict) -> dict:
    project = payload.get("project")
    period  = payload.get("period")
    return {"ok": True, "agent": "project", "project": project, "period": period}