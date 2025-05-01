from langchain.tools import tool
from helpers.fetch_frontend_trends import fetch_frontend_trends
from llm.generate_topic_from_trend import generate_topic_from_trend


@tool
def fetch_trends_tool(_: str = "") -> str:
    """
    Returns a comma-separated list of trending frontend terms.
    """
    return ", ".join(fetch_frontend_trends())


@tool
def generate_topic_from_trend_tool(trend: str) -> str:
    """
    Generates a topic idea from a single frontend trend.
    """
    return generate_topic_from_trend(trend)
