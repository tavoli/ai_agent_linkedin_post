from agent.commenter_agent import commenter_agent
from datetime import datetime


def run_commenter():
    print(f"\n💬 Commenting at {datetime.now().strftime('%H:%M:%S')}")

    try:
        commenter_agent.run(
            """
            Your task is to comment on up to 3 relevant LinkedIn feed posts.

            Step-by-step:
            - Use `scrape_feed` to get up to 10 posts.
            - For each post:
              - Use `is_post_relevant` to determine if it's relevant to frontend developers or interesting to international recruiters.
              - If YES:
                - Use `generate_comment` to write a short, honest comment (no pretending or experience).
                - Use `post_comment` to publish it.
            - Continue until you comment on 3 posts or run out of relevant content.

            Avoid repetition and always be honest in tone.
            """
        )
    except Exception as e:
        print(f"❌ Commenter error: {e}")
