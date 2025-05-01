from langchain.tools import tool
from llm.generate_post import generate_post
from helpers.post_to_linkedin import post_to_linkedin
from helpers.format_linkedin_post import format_linkedin_post
from config import LINKEDIN_PERSON_URN


@tool()
def generate_post_tool(topic: str) -> str:
    """
    Generate a short, engaging LinkedIn post based on a given frontend topic.
    Returns formatted post text.
    """
    return generate_post(topic)


@tool()
def post_to_linkedin_tool(post_text: str) -> str:
    """
    Format a LinkedIn post and send it using the API.
    Returns the URN if successful, or an error message.
    """
    payload = format_linkedin_post(
            post_text=post_text,
            person_urn=LINKEDIN_PERSON_URN
    )
    result = post_to_linkedin(payload)

    if result["success"]:
        return f"✅ Post published! URN: {result['post_urn']}"
    else:
        return f"❌ Failed to post: {result['status']} - {result['message']}"
