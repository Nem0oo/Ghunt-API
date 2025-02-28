from fastapi import FastAPI
from pathlib import Path
import subprocess
import time

app = FastAPI()

@app.get("/ghunt")
def run_ghunt(command: str, params: str, key: str):
    secret = Path('api_data/key.txt').read_text()
    jsonFileName = Path('/accounts_info/' + time.strftime("%Y%m%d-%H%M%S") + params.replace("@gmail.com",".json"))
    if key == secret:
        try:
            result = subprocess.run([
                "docker", "exec", "ghunt", "ghunt", command, params, "--json", jsonFileName
            ], capture_output=True, text=True)
            jsonContent = Path(jsonFileName).read_text()
            return {"output": {"text" : result.stdout, "json" : jsonContent}, "error": result.stderr}
        except Exception as e:
            return {"error": str(e)}
    return {"error":"Invalid key"}