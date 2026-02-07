from app.core.heuristics import detect_global_nav
from app.utils.hashing import page_id

def build_user_flow(start_url: str, pages: dict):
    global_links = detect_global_nav(pages)

    nodes = {}
    edges = []

    for src, links in pages.items():
        src_id = page_id(src)
        nodes[src_id] = src

        for dst in links:
            if dst in global_links:
                continue  # 🔥 noise removal
            edges.append({
                "from": src_id,
                "to": page_id(dst)
            })

    return {
        "start_url": start_url,
        "nodes": [{"id": k, "label": v} for k, v in nodes.items()],
        "edges": edges,
        "global_navigation": list(global_links)
    }
