
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
