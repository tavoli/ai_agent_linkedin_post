from helpers.comment_on_revelant_posts import comment_on_relevant_posts
from datetime import datetime


def run_commenter_procedural():
    print(f"\n💬 Running procedural commenter at {datetime.now().strftime('%H:%M:%S')}")
    try:
        comment_on_relevant_posts(limit=100, max_comments=3)
    except Exception as e:
        print(f"❌ Commenter error: {e}")
