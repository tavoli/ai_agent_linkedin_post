import schedule
import time
from datetime import datetime
from agent.publisher_agent import publisher_agent


def run_publisher():
    print(f"\nRunning at {datetime.now().strftime('%H:%M:%S')}")
    try:
        publisher_agent.run("""
        Fetch the latest frontend trends and generate a post based on one of them.

        After writing the post, use the tool `check_post_relevance` to evaluate it.

        If the result is 'reject', discard the post and try again with a new trend or different angle. You may retry up to 3 times.

        Only publish the post if it passes the relevance check with an 'approve' result.

        Be thoughtful and creative, but avoid posting anything generic or weak.
        """)
    except Exception as e:
        print(f"❌ Error: {e}")


schedule.every().day.at("08:00").do(run_publisher)
schedule.every().day.at("11:00").do(run_publisher)
schedule.every().day.at("14:00").do(run_publisher)
schedule.every().day.at("17:00").do(run_publisher)
schedule.every().day.at("20:00").do(run_publisher)

print("Publisher daemon started. Running 5x/day.")

while True:
    schedule.run_pending()
    time.sleep(30)
