from typing import Annotated
from helpers.comment_post import post_comment


def post_comment_tool(urn: Annotated[str, "LinkedIn post URN"],
                      comment: Annotated[str, "Comment text"]) -> str:
    """
    Posts a comment to a LinkedIn activity using the LinkedIn API.
    """
    try:
        if not urn or not comment:
            return "❌ Missing 'urn' or 'comment'."

        post_comment(urn, comment)
        return f"✅ Comment posted on {urn}"

    except Exception as e:
        return f"❌ Error posting comment: {e}"
