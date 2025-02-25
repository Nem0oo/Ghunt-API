from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ghunt")
def run_ghunt(command: str, params: str):
    try:
        result = subprocess.run([
            "docker", "exec", "ghunt", "ghunt", command, params,
        ], capture_output=True, text=True)
        return {"output": result.stdout, "error": result.stderr}
    except Exception as e:
        return {"error": str(e)}