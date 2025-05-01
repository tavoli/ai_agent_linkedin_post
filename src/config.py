from dotenv import dotenv_values
from langchain_openai import ChatOpenAI

config = dotenv_values(".env")
OPENAI_API_KEY = config.get("OPENAI_API_KEY")
LINKEDIN_PERSON_URN = config.get("LINKEDIN_PERSON_URN")
LINKEDIN_ACCESS_TOKEN = config.get("LINKEDIN_ACCESS_TOKEN")

if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.8,
    api_key=OPENAI_API_KEY
)
