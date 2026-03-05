
from app.severity_classifier import classify_severity
from mcp_servers.github_mcp.tools.get_failed_prs import get_failed_prs
from mcp_servers.github_mcp.tools.get_pr_logs import get_pr_logs
from mcp_servers.github_mcp.tools.get_pr_author import get_pr_author
from mcp_servers.github_mcp.tools.get_pr_link import get_pr_link
from mcp_servers.jira_mcp.tools.create_issue import create_issue
from mcp_servers.jira_mcp.tools.assign_issue import assign_issue
from mcp_servers.slack_mcp.tools.post_message import post_message

def run_ci_flow():
    failed_prs = get_failed_prs()

    for pr in failed_prs:
        logs = get_pr_logs(pr)
        severity = classify_severity(logs)
        issue_key = create_issue(pr, severity, logs)
        author = get_pr_author(pr)
        assign_issue(issue_key, author)
        pr_link = get_pr_link(pr)
        post_message(f"Jira Issue {issue_key} created for PR {pr_link}")
