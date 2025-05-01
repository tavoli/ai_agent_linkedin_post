from langchain.agents import initialize_agent, AgentType, Tool
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage

from tools.post_tool import generate_post_tool, post_to_linkedin_tool
from tools.trend_tool import fetch_trends_tool, generate_topic_from_trend_tool
from memory.log import load_logged_topics

from config import llm


past_topics = load_logged_topics()
past_topics_summary = "\n".join(f"- {t}" for t in past_topics[-25:])

system_message = SystemMessage(content=f"""
You are a LinkedIn publishing strategist named 'PublisherBot'.

Your goal is to help a humble but sharp software developer post content regularly on LinkedIn that is timely, useful, and insightful.

Use only real frontend trends to generate topics. Focus on tools and libraries that are relevant in 2025.

Avoid repeating any topic that is too similar to the following list of past topics:

{past_topics_summary}

For the post content:
- Use a calm, self-aware tone
- Emphasize problem-solving and real benefits
- Avoid overconfidence or hype
- Never invent personal stories
- Structure posts with short lines and blank line spacing for LinkedIn formatting

Only publish if the topic seems genuinely useful and distinct from common posts.
""")

tools = [
    Tool.from_function(
        func=fetch_trends_tool,
        name="fetch_trends",
        description="Fetches a comma-separated list of trending frontend libraries and tools."
    ),
    Tool.from_function(
        func=generate_topic_from_trend_tool,
        name="generate_topic_from_trend",
        description="Given a frontend trend, generates a compelling LinkedIn topic idea."
    ),
    Tool.from_function(
        func=generate_post_tool,
        name="generate_post",
        description="Generates a well-formatted LinkedIn post based on a given topic."
    ),
    Tool.from_function(
        func=post_to_linkedin_tool,
        name="post_to_linkedin",
        description="Formats and publishes a LinkedIn post using the LinkedIn API."
    ),
]

memory = ConversationBufferMemory(memory_key="chat_history")

publisher_agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    memory=memory,
    verbose=True,
    agent_kwargs={
        "system_message": system_message
    }
)
