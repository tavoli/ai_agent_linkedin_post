from langchain.tools import tool
from helpers.scrape_feed import scrape_feed_posts


@tool
def scrape_feed_tool(limit: int = 10) -> list:
    """
    Scrapes up to N LinkedIn posts from your feed. Each post includes a URN and snippet of text.
    """
    return scrape_feed_posts(int(limit))
