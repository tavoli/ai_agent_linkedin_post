from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import SystemMessage, HumanMessage
from config import llm

def generate_topic(recent_topics=None):
    if recent_topics is None:
        recent_topics = []

    prompt = PromptTemplate.from_template("""
You are a technical content creator writing for frontend developers on LinkedIn.

Generate 1 unique and timely post topic idea about frontend development.

It should:
- Be relevant in 2025 (mention real tools, methods, or trends)
- Be specific enough to write a 300-character post about
- Be engaging and sound insightful

Avoid repeating these topics:
{recent}

Respond ONLY with the topic title.
""")

    messages = [
        SystemMessage(content="You generate concise post ideas for frontend devs."),
        HumanMessage(content=prompt.format(recent=", ".join(recent_topics)))
    ]

    response = llm.invoke(messages)
    return response.content.strip()
