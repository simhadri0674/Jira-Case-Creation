
# import os
# from dotenv import load_dotenv

# load_dotenv()

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
# JIRA_TOKEN = os.getenv("JIRA_TOKEN")
# SLACK_TOKEN = os.getenv("SLACK_TOKEN")
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER = os.getenv("GITHUB_OWNER")
GITHUB_REPO = os.getenv("GITHUB_REPO")

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")