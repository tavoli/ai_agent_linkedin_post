from config import LINKEDIN_ACCESS_TOKEN
from config import LINKEDIN_PERSON_URN
from datetime import datetime
import requests


def post_comment(activity_urn: str, comment: str):
    """
    Posts a comment to a LinkedIn activity using the REST API.
    Requires LINKEDIN_ACCESS_TOKEN and LINKEDIN_PERSON_URN in .env.
    """

    if not LINKEDIN_ACCESS_TOKEN:
        raise ValueError("Missing LINKEDIN_ACCESS_TOKEN in .env")

    if not LINKEDIN_PERSON_URN:
        raise ValueError("Missing LINKEDIN_PERSON_URN in .env")

    url = f"https://api.linkedin.com/rest/socialActions/{activity_urn}/comments"
    headers = {
        "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
        "LinkedIn-Version": "202302",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }

    payload = {
        "actor": LINKEDIN_PERSON_URN,
        "message": {
            "text": comment
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        print(f"✅ Comment posted on {activity_urn} at {datetime.now().isoformat()}")
    except Exception as e:
        print(f"❌ Failed to post comment: {e}\n{response.text if 'response' in locals() else ''}")
