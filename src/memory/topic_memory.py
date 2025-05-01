import json
from pathlib import Path

RECENT_TOPICS_PATH = Path(__file__).resolve().parent.parent / "data" / "recent_topics.json"
MAX_TOPICS = 50  # keep only last 50 topics

def load_recent_topics() -> list:
    if not RECENT_TOPICS_PATH.exists():
        return []
    with open(RECENT_TOPICS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_recent_topic(topic: str):
    RECENT_TOPICS_PATH.parent.mkdir(parents=True, exist_ok=True)  # ensure /data exists
    recent = load_recent_topics()
    if topic in recent:
        return
    recent.append(topic)
    if len(recent) > MAX_TOPICS:
        recent = recent[-MAX_TOPICS:]  # keep latest N only
    with open(RECENT_TOPICS_PATH, "w", encoding="utf-8") as f:
        json.dump(recent, f, ensure_ascii=False, indent=2)
