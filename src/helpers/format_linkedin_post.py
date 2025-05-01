def format_linkedin_post(post_text: str, person_urn: str) -> dict:
    """
    Formats a post for LinkedIn's UGC API.

    Args:
        post_text (str): The LinkedIn post content (max 1300 visible chars).
        person_urn (str): e.g., "urn:li:person:abc123"

    Returns:
        dict: JSON payload ready for POST /v2/ugcPosts
    """

    clean_text = post_text.replace("\\n", "\n").replace("\\r", "\r")

    return {
        "author": person_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": clean_text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
