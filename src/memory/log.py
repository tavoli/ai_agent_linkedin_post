import json
from pathlib import Path
from datetime import datetime

posts_json_path = "data/posts_log.jsonl"
POST_LOG_PATH = Path(__file__).resolve().parent.parent.parent / posts_json_path
POST_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)


def log_post(topic: str, post: str, urn: str):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "topic": topic.strip(),
        "post": post.strip(),
        "urn": urn
    }
    with open(POST_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def load_logged_topics() -> list[str]:
    if not POST_LOG_PATH.exists():
        return []
    with open(POST_LOG_PATH, "r", encoding="utf-8") as f:
        return [
            json.loads(line)["topic"].strip()
            for line in f.readlines()
            if line.strip()
        ]


COMMENT_LOG_PATH = POST_LOG_PATH.parent / "comment_log.jsonl"
COMMENT_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)


def log_comment(urn: str, comment: str):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "urn": urn,
        "comment": comment.strip()
    }
    with open(COMMENT_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
