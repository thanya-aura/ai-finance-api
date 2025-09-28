# ai-finance-api/run_agent.py
import json, sys, importlib
from pathlib import Path

# ใช้: python run_agent.py <agents.module_name> <json-payload> | @payload.json
if len(sys.argv) < 3:
    print("usage: python run_agent.py <module> <json> | @<json-file>")
    sys.exit(1)

mod = importlib.import_module(sys.argv[1])

arg = sys.argv[2]
if arg.startswith('@'):
    payload = json.loads(Path(arg[1:]).read_text(encoding='utf-8-sig'))
else:
    payload = json.loads(arg)

print(json.dumps(mod.run(payload), ensure_ascii=False))
