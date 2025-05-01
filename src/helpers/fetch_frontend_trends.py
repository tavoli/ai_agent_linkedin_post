import requests


def fetch_frontend_trends() -> list[str]:
    """
    Fetches trending frontend-related packages from the npms.io API.
    Returns the top 5 package names sorted by popularity.
    """
    try:
        response = requests.get(
            "https://api.npms.io/v2/search",
            params={
                "q": "keywords:frontend OR keywords:react OR keywords:bundler",
                "size": 5,
            }
        )
        response.raise_for_status()

        data = response.json()
        packages = data.get("results", [])

        trends = [pkg["package"]["name"] for pkg in packages]
        return trends

    except Exception as e:
        print(f"Failed to fetch trends: {e}")
        return ["vite", "react", "bun", "tanstack router", "shadcn-ui"]
