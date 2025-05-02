from playwright.sync_api import sync_playwright
from pathlib import Path

session_path = "storage/state.json"
SESSION_PATH = Path(__file__).resolve().parent.parent.parent / session_path


def scrape_feed_posts(limit: int = 10) -> list[dict]:
    print("🔍 Launching browser and loading LinkedIn feed...")
    posts = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=SESSION_PATH)
        page = context.new_page()

        page.goto("https://www.linkedin.com/feed/")
        page.wait_for_selector('div.feed-shared-update-v2', timeout=10000)

        while len(posts) < limit:
            post_elements = page.query_selector_all('div.feed-shared-update-v2')

            for element in post_elements:
                try:
                    data_urn = element.get_attribute("data-urn")
                    if not data_urn or not data_urn.startswith("urn:li:activity:"):
                        continue

                    content = element.inner_text().strip()
                    if not content:
                        continue

                    post = {
                        "urn": data_urn,
                        "text": content[:600].replace("\n", " ")  # truncate for relevance
                    }

                    if post not in posts:
                        posts.append(post)

                    if len(posts) >= limit:
                        break

                except Exception as e:
                    print(f"⚠️ Error parsing post: {e}")
                    continue

            page.mouse.wheel(0, 1000)  # Scroll to load more posts
            page.wait_for_timeout(1500)

        browser.close()
    return posts
