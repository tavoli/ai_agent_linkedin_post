import requests
from config import LINKEDIN_ACCESS_TOKEN

def post_to_linkedin(payload: dict) -> dict:
    if not LINKEDIN_ACCESS_TOKEN:
        raise ValueError("Missing LINKEDIN_ACCESS_TOKEN in .env")

    headers = {
        "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
        "X-Restli-Protocol-Version": "2.0.0",
        "LinkedIn-Version": "202302",
        "Content-Type": "application/json",
    }

    response = requests.post("https://api.linkedin.com/v2/ugcPosts", json=payload, headers=headers)

    if response.status_code == 201:
        return {"success": True, "post_urn": response.headers.get("x-restli-id")}
    else:
        return {
            "success": False,
            "status": response.status_code,
            "message": response.json() if response.content else response.text,
        }
