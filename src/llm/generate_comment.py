from langchain.schema import HumanMessage, SystemMessage
from config import llm


def generate_comment(post_text: str) -> str:
    """
    Generates a brief, humble, and honest comment based on the post content.
    The comment must never imply that the user has done or tried anything.
    """

    prompt = f"""
You are writing a LinkedIn comment for a frontend developer who wants to build a thoughtful, humble online presence.

Based on this post, write a comment that:
- Responds to the **main idea** of the post
- Shows appreciation, curiosity, or engagement
- Is under 300 characters
- Does NOT claim experience (no "I used this", "I tried this")
- Uses a professional, honest, and modest tone

Post content:
\"\"\"{post_text}\"\"\"

Respond only with the comment.
"""

    messages = [
        SystemMessage(content="You are a careful assistant writing professional LinkedIn comments."),
        HumanMessage(content=prompt)
    ]

    try:
        response = llm.invoke(messages)
        return response.content.strip().lower()
    except Exception as e:
        print(f"❌ Comment generation error: {e}")
        return "Thanks for sharing this insight!"
