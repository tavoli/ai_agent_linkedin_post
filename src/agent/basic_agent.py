from langchain.agents import initialize_agent, AgentType
from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
from tools.topic_tool import generate_topic_tool
from tools.post_tool import generate_post_tool, post_to_linkedin_tool
from config import llm

tools = [
    Tool(
        name="generate_topic",
        func=generate_topic_tool,
        description="Generates a fresh and relevant frontend topic based on recent ones."
    ),
    Tool(
        name="generate_post",
        func=generate_post_tool,
        description="Generates a LinkedIn post based on a topic."
    ),
    Tool(
        name="post_to_linkedin",
        func=post_to_linkedin_tool,
        description="Formats and publishes the LinkedIn post using the API."
    )
]

memory = ConversationBufferMemory(memory_key="chat_history")

basic_agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
)
