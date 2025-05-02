from langchain.schema import HumanMessage, SystemMessage
from config import llm


def is_post_relevant(post_text: str) -> bool:
    """
    Uses LLM to determine whether commenting on this post would be helpful
    to increase visibility as a frontend developer looking for international opportunities.
    """
    prompt = f"""
You are helping a humble frontend developer gain international visibility on LinkedIn.

Given this post, should they comment on it to improve their public reputation in a genuine and non-promotional way?

Do NOT assume the person has used or experienced anything in the post.
Only answer YES if it's:
- related to frontend, tech, or developer culture
- professional, not personal
- appropriate to engage with publicly

Post content:
\"\"\"{post_text}\"\"\"

Respond ONLY with YES or NO.
"""

    messages = [
        SystemMessage(content="You are a strategic LinkedIn growth assistant."),
        HumanMessage(content=prompt)
    ]

    try:
        response = llm.invoke(messages)
        answer = response.content.strip().upper()
        return answer.startswith("YES")
    except Exception as e:
        print(f"❌ LLM relevance filter error: {e}")
        return False
