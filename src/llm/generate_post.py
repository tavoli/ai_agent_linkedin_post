from langchain.prompts import PromptTemplate
from langchain.schema import SystemMessage, HumanMessage
from config import llm


def generate_post(topic: str) -> str:
    prompt = PromptTemplate.from_template("""
You are a storytelling assistant helping developers write high-performing long-form LinkedIn posts.

Write a story-driven post based on the following topic:

Topic: "{topic}"

Style & Structure:
- Begin with a short sentence that includes a curiosity or tension keyword like:
  fear, mystery, mistake, danger, power, secret, rule, bug, trap, breakthrough, warning, truth
- Follow with a second sentence that builds intrigue
- Continue with clear, short sentences reflecting on the issue or trend (not a personal story)
- Write each sentence on a new line
- Insert a blank line between every sentence to improve readability
- End with a thoughtful reflection or question to encourage discussion

Do not invent personal stories, quotes, or events.

Tone: human, honest, reflective, and professional.

Avoid:
- Hashtags
- Links
- Buzzwords
- Emojis

Keep total length under 1500 characters.
Return only the post text.
""")

    messages = [
        SystemMessage(content="You help developers write short, engaging LinkedIn posts."),
        HumanMessage(content=prompt.format(topic=topic))
    ]

    response = llm.invoke(messages)
    return response.content.strip()
