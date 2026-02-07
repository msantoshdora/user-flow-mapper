# core/crawler.py
import requests
from bs4 import BeautifulSoup
from collections import deque
from app.utils.url import is_internal, normalize_url

MAX_PAGES = 100  # safety limit

def crawl_site(start_url: str, max_depth: int):
    visited = set()
    queue = deque([(start_url, 0)])
    pages = {}

    while queue:
        url, depth = queue.popleft()
        if len(visited) >= MAX_PAGES:
            break
        if url in visited or depth > max_depth:
            continue

        visited.add(url)
        try:
            res = requests.get(url, timeout=5)
        except Exception:
            continue

        soup = BeautifulSoup(res.text, "html.parser")
        links = []

        for a in soup.find_all("a", href=True):
            link = normalize_url(url, a["href"])
            if is_internal(start_url, link):
                links.append(link)
                queue.append((link, depth + 1))

        pages[url] = links

    return pages
