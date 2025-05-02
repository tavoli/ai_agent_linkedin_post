from helpers.comment_on_revelant_posts import comment_on_relevant_posts

if __name__ == "__main__":
    print("🧪 Running on-the-fly LinkedIn commenter (Playwright UI)...")
    comment_on_relevant_posts(limit=100, max_comments=3)
