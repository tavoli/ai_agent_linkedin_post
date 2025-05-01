from langchain.schema import HumanMessage, SystemMessage
from config import llm


def check_post_relevance(post: str) -> str:
    """
    Uses an LLM to determine whether a LinkedIn post is engaging, relevant, and worth publishing.
    Returns 'approve' or 'reject' with reasoning.
    """

    messages = [
        SystemMessage(content="You are a professional LinkedIn strategist."),
        HumanMessage(content=f"""
Analyze the following LinkedIn post:

\"\"\"{post}\"\"\"

Determine if it is:
- Engaging in the first 3 lines
- Relevant to frontend developers in 2025
- Insightful and not generic
- Well-formatted (short lines, spaced)

Respond only with 'approve' or 'reject' and briefly justify your choice.
""")
    ]

    response = llm.invoke(messages)
    return response.content.strip()
