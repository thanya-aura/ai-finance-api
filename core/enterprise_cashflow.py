def run(payload: dict) -> dict:
    company = payload.get("company")
    period  = payload.get("period")
    return {"ok": True, "agent": "enterprise", "company": company, "period": period}