import json
from pathlib import Path


def get_failed_prs():

    file_path = Path(__file__).parent / "sample_prs.json"

    with open(file_path) as f:
        prs = json.load(f)

    failed = []

    for pr in prs:
        if pr["status"] == "failed":
            failed.append(pr)

    return failed


def get_pr_logs(pr_id):

    file_path = Path(__file__).parent / "sample_logs.json"

    with open(file_path) as f:
        logs = json.load(f)

    return logs.get(str(pr_id), {})