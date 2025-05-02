from playwright.sync_api import sync_playwright
from llm.generate_comment import generate_comment
from llm.filter_post import is_post_relevant
from memory.log import log_comment
from pathlib import Path
import time

session_path = "storage/state.json"
SESSION_PATH = Path(__file__).resolve().parent.parent.parent / session_path


def comment_on_relevant_posts(limit=10, max_comments=3):
    commented = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # set to True when stable
        context = browser.new_context(storage_state=SESSION_PATH)
        page = context.new_page()

        print("🔍 Opening LinkedIn feed...")
        page.goto("https://www.linkedin.com/feed/", timeout=60000)
        page.wait_for_timeout(5000)

        feed_items = page.locator("div.feed-shared-update-v2")

        index = 0
        while commented < max_comments and index < limit:
            feed_items = page.locator("div.feed-shared-update-v2")
            count = feed_items.count()

            if index >= count:
                # Scroll down to load more
                page.mouse.wheel(0, 2000)
                page.wait_for_timeout(2000)
                continue

            try:
                item = feed_items.nth(index)
                see_more_button = item.locator('button[aria-label*="see more"]')
                if see_more_button.count() > 0:
                    see_more_button.first.click()
                    page.wait_for_timeout(1000)
                content_block = item.locator("span.break-words").first
                post_text = content_block.inner_text().strip()[:1000].replace("\n", " ")

                if not is_post_relevant(post_text):
                    print(f"🚫 Post {index} not relevant")
                    index += 1
                    continue

                comment = generate_comment(post_text)
                print(f"💬 Writing comment:\n{comment[:80]}")

                comment_button = item.locator("button[aria-label*='Comment']")
                comment_button.click()
                page.wait_for_timeout(1000)

                # 🔒 Check if comment input is available
                comment_input = item.locator('div[role="textbox"]')
                if not comment_input.is_visible(timeout=2000):
                    print(f"🔒 Post {index} does not allow commenting — skipping")
                    index += 1
                    continue

                comment_input.scroll_into_view_if_needed()
                comment_input.click()
                page.wait_for_timeout(300)
                page.keyboard.insert_text(comment)
                page.wait_for_timeout(300)
                submit_button = item.locator("button.comments-comment-box__submit-button--cr")
                submit_button.click()
                page.wait_for_timeout(500)

                log_comment(f"commented_post_{index}", comment)
                print(f"✅ Comment posted on post {index}")
                commented += 1
                index += 1
                page.wait_for_timeout(2000)

            except Exception as e:
                print(f"⚠️ Error on post {index}: {e}")
                index += 1
                continue

        browser.close()
        print(f"🎯 Done: {commented} comments posted.")
