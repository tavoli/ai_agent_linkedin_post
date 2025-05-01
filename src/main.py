from llm.generate_topic import generate_topic
from llm.generate_post import generate_post
from linkedin.format_linkedin_post import format_linkedin_post
from linkedin.post_to_linkedin import post_to_linkedin
from memory.topic_memory import load_recent_topics, save_recent_topic
from config import LINKEDIN_PERSON_URN

if __name__ == "__main__":
    recent = load_recent_topics()
    topic = generate_topic(recent)
    save_recent_topic(topic)
    post = generate_post(topic)
    post_json = format_linkedin_post(post_text=post, person_urn=LINKEDIN_PERSON_URN)
    result = post_to_linkedin(post_json)

    if result["success"]:
        print(f"✅ Post published successfully! URN: {result['post_urn']}")
    else:
        print(f"❌ Failed to post: {result['status']} - {result['message']}")
