import requests

url = "https://jsonplaceholder.typicode.com/posts"
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    posts = response.json()[:5]  # Extract latest 5 posts
    print("--- Latest 5 Posts from JSONPlaceholder API ---")
    for idx, post in enumerate(posts, 1):
        print(f"Post #{idx}: {post['title']}")
except Exception as e:
    print(f"Error fetching data: {e}")
