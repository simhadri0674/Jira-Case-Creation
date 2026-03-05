
import time
from app.orchestrator import run_ci_flow

while True:
    run_ci_flow()
    time.sleep(300)
