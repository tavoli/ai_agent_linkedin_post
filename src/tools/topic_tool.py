from langchain.tools import tool
from llm.generate_topic import generate_topic


@tool()
def generate_topic_tool(recent_topics: str) -> str:
    """
    Generate a unique and timely frontend topic for a LinkedIn post.
    Accepts a comma-separated string of recent topics to avoid duplication.
    """
    recent_list = [t.strip() for t in recent_topics.split(",") if t.strip()]
    return generate_topic(recent_list)
