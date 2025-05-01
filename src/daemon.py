import schedule
import time
from datetime import datetime
from agent.publisher_agent import publisher_agent


def run_publisher():
    print(f"\nRunning at {datetime.now().strftime('%H:%M:%S')}")
    try:
        result = publisher_agent.run(
            "Fetch the latest frontend trends, generate a LinkedIn post based on one of them, and publish it using my tone of voice."
        )
        print(f"✅ Post created and sent: \n{result}")
    except Exception as e:
        print(f"❌ Error: {e}")

# Run 5 times per day

schedule.every().day.at("08:00").do(run_publisher)
schedule.every().day.at("11:00").do(run_publisher)
schedule.every().day.at("13:56").do(run_publisher)
schedule.every().day.at("17:00").do(run_publisher)
schedule.every().day.at("20:00").do(run_publisher)

print("Publisher daemon started. Running 5x/day.")

while True:
    schedule.run_pending()
    time.sleep(30)
