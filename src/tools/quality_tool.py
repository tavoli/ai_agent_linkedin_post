from langchain.tools import tool
from llm.check_post_relevance import check_post_relevance


@tool
def check_post_relevance_tool(post: str) -> str:
    """
    Evaluates whether a LinkedIn post is relevant, engaging, and well-formatted.
    Returns 'approve' or 'reject' with justification.
    """
    return check_post_relevance(post)
