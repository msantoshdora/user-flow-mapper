# core/heuristics.py
def detect_global_nav(pages: dict, threshold=0.6):
    """
    A link appearing on >60% pages is treated as global navigation
    """
    from collections import Counter

    counter = Counter()
    total_pages = len(pages)

    for links in pages.values():
        counter.update(set(links))

    return {
        link
        for link, count in counter.items()
        if count / total_pages >= threshold
    }
