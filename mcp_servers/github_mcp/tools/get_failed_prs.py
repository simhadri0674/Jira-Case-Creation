
# def get_failed_prs():
#     # Replace with real GitHub API call
#     return ["PR-123"]
import requests
from app.config import GITHUB_TOKEN, GITHUB_OWNER, GITHUB_REPO

def get_failed_prs():

    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/pulls?state=open"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    prs = response.json()

    failed_prs = []

    for pr in prs:
        if "fail" in pr["title"].lower():
            failed_prs.append({
                "id": pr["number"],
                "title": pr["title"],
                "url": pr["html_url"]
            })

    return failed_prs