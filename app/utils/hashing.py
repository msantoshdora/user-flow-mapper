import hashlib

def page_id(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()[:8]
