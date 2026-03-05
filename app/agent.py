
from fastapi import FastAPI
from app.orchestrator import run_ci_flow

app = FastAPI()

@app.get("/run")
def trigger():
    run_ci_flow()
    return {"status": "CI automation executed"}
