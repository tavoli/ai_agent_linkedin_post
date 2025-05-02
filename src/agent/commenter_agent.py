from langchain.agents import initialize_agent, Tool, AgentType
from langchain.tools import StructuredTool
from tools.scrape_feed_tool import scrape_feed_tool
from tools.filter_post_tool import is_post_relevant_tool
from tools.generate_comment_tool import generate_comment_tool
from tools.comment_tool import post_comment_tool
from config import llm

tools = [
    Tool.from_function(
        func=scrape_feed_tool,
        name="scrape_feed",
        description="Scrapes up to N LinkedIn posts from your feed. Each post includes a URN and snippet of text."
    ),

    Tool.from_function(
        func=is_post_relevant_tool,
        name="is_post_relevant",
        description="Returns YES if the input post is worth commenting on for professional frontend developer visibility."
    ),

    Tool.from_function(
        func=generate_comment_tool,
        name="generate_comment",
        description="Generates a short, humble, professional comment based on a LinkedIn post. Avoids pretending the user has done anything."
    ),

    StructuredTool.from_function(
        func=post_comment_tool,
        name="post_comment",
        description="Posts a comment to a LinkedIn post. Input must include 'urn' and 'comment'."
    )
]

commenter_agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True,
    agent_kwargs={
        "system_message": """
You are a professional assistant who comments on LinkedIn posts to build public reputation for a frontend developer.

Goal:
- Scrape feed posts
- Check if post is worth commenting
- If YES, generate a short honest comment (never say "I used this")
- Post it using the API

Comment on up to 3 relevant posts. Starts all over again if no relevant posts are found.
"""
    }
)
