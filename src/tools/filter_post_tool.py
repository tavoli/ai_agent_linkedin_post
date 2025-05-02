from langchain.tools import tool
from llm.filter_post import is_post_relevant


@tool
def is_post_relevant_tool(post: str) -> str:
    """
    Determines if a LinkedIn post is worth commenting on to increase visibility as a frontend developer.

    Input: post text (string)
    Output: 'YES' if worth commenting, else 'NO'
    """
    try:
        return "YES" if is_post_relevant(post) else "NO"
    except Exception as e:
        return f"❌ Error in relevance filter: {e}"
