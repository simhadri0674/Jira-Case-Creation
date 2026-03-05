from simulate_failed_pr import get_failed_prs, get_pr_logs


def classify_severity(logs):

    text = logs.get("logs", "").lower()

    if "authentication" in text:
        return "HIGH"

    if "test failure" in text:
        return "MEDIUM"

    return "LOW"


def create_jira_issue(pr, severity):

    print("\nJIRA ISSUE CREATED")
    print("------------------")
    print(f"Title: CI Failure PR #{pr['id']}")
    print(f"Severity: {severity}")
    print(f"Author: {pr['author']}")


def send_slack_notification(pr, severity):

    print("\nSLACK MESSAGE SENT")
    print("------------------")
    print(f"PR #{pr['id']} failed")
    print(f"Severity: {severity}")
    print(f"Link: {pr['url']}")


def run_pipeline():

    failed_prs = get_failed_prs()

    for pr in failed_prs:

        logs = get_pr_logs(pr["id"])

        severity = classify_severity(logs)

        create_jira_issue(pr, severity)

        send_slack_notification(pr, severity)


if __name__ == "__main__":
    run_pipeline()