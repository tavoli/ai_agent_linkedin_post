from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage
from config import llm


def generate_topic_from_trend(trend: str) -> str:
    """
    Given a frontend trend, generate a specific and compelling LinkedIn topic.
    """
    prompt = PromptTemplate.from_template("""
You are a technical content strategist for LinkedIn.

Turn this frontend trend into a compelling topic idea for a LinkedIn post:

Trend: "{trend}"

The result should be a short, specific topic title.
""")

    messages = [
        SystemMessage(content="You help generate specific LinkedIn post topics."),
        HumanMessage(content=prompt.format(trend=trend))
    ]

    response = llm.invoke(messages)
    return response.content.strip()
