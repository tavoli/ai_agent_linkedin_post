def format_linkedin_post(post_text: str, person_urn: str) -> dict:
    """
    Formats a post for LinkedIn's UGC API.

    Args:
        post_text (str): The LinkedIn post content (max 1300 visible chars).
        person_urn (str): e.g., "urn:li:person:abc123"

    Returns:
        dict: JSON payload ready for POST /v2/ugcPosts
    """

    return {
        "author": person_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": post_text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
