import json, sys, importlib
# ใช้: python run_agent.py <agents.module_name> '{"key":"value"}'
if len(sys.argv) < 3:
    print("usage: python run_agent.py <module> <json-payload>")
    sys.exit(1)
mod = importlib.import_module(sys.argv[1])
payload = json.loads(sys.argv[2])
print(json.dumps(mod.run(payload), ensure_ascii=False))
