from fastapi import FastAPI
from pathlib import Path
import subprocess

app = FastAPI()

@app.get("/ghunt")
def run_ghunt(command: str, params: str, key: str):
    secret = Path('api_data/key.txt').read_text()
    if key == secret:
        try:
            result = subprocess.run([
                "docker", "exec", "ghunt", "ghunt", command, params,
            ], capture_output=True, text=True)
            return {"output": result.stdout, "error": result.stderr}
        except Exception as e:
            return {"error": str(e)}
    return {"error":"Invalid key"}