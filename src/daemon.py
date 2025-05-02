import schedule
import time
from datetime import datetime
from runners.run_publisher import run_publisher
from runners.run_commenter_proc import run_commenter_procedural


def log_schedule(title: str):
    print(f"\n⏱️ {title} at {datetime.now().strftime('%H:%M:%S')}")


def schedule_post(hour: str):
    schedule.every().day.at(hour).do(
        lambda: (log_schedule("Post"), run_publisher())
    )


def schedule_comment(hour: str):
    schedule.every().day.at(hour).do(
        lambda: (log_schedule("Comment"), run_commenter_procedural())
    )


for hour in ["09:00", "14:00", "19:00"]:
    schedule_post(hour)

for hour in ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00"]:
    schedule_comment(hour)

print("\n\n🕰️  Daemon started. Waiting for scheduled tasks...")

while True:
    schedule.run_pending()
    time.sleep(30)
