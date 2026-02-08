import requests
from bs4 import BeautifulSoup
from collections import deque
from app.utils.url import is_internal, normalize_url

MAX_PAGES = 100  # safety limit
BLACKLIST_PATTERNS = ["/page/", "?page="]  # pagination & junk

def crawl_site(start_url: str, max_depth: int):
    visited = set()
    queue = deque([(start_url, 0)])
    pages = {}

    while queue:
        url, depth = queue.popleft()

        # 1. Hard safety limits
        if len(visited) >= MAX_PAGES:
            break
        if depth > max_depth:
            continue
        if url in visited:
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

            # 2. Crawl only internal links
            if not is_internal(start_url, link):
                continue

            # 3. Skip pagination / noisy patterns early
            if any(p in link for p in BLACKLIST_PATTERNS):
                continue

            # 4. Avoid re-queueing visited pages
            if link in visited:
                continue

            links.append(link)
            queue.append((link, depth + 1))

        pages[url] = links

    return pages