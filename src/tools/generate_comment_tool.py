from langchain.tools import tool
from llm.generate_comment import generate_comment


@tool
def generate_comment_tool(post: str) -> str:
    """
    Generates a short, honest, and humble LinkedIn comment based on the given post content.
    Does not claim any personal experience or actions.
    """
    try:
        return generate_comment(post)
    except Exception as e:
        return f"❌ Error generating comment: {e}"
