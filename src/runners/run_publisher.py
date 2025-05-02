from agent.publisher_agent import publisher_agent
from datetime import datetime


def run_publisher():
    print(f"\n🕒 Posting at {datetime.now().strftime('%H:%M:%S')}")

    try:
        publisher_agent.run("""
Fetch the latest frontend trends and generate a post based on one of them.

After writing the post, use the tool `check_post_relevance` to evaluate it.

If the result is 'reject', discard the post and try again with a new trend or different angle. You may retry up to 3 times.

Only publish the post if it passes the relevance check with an 'approve' result.

Be thoughtful and creative, but avoid posting anything generic or weak.
""")
    except Exception as e:
        print(f"❌ Post error: {e}")
