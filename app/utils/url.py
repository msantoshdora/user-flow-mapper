from urllib.parse import urljoin, urlparse

def normalize_url(base, link):
    return urljoin(base, link).split("#")[0]

def is_internal(start_url, link):
    return urlparse(start_url).netloc == urlparse(link).netloc
