from fastapi import APIRouter
from app.models.schema import CrawlRequest, CrawlResponse
from app.core.crawler import crawl_site
from app.core.flow_mapper import build_user_flow

router = APIRouter()

@router.post("/crawl", response_model=CrawlResponse)
def crawl(req: CrawlRequest):
    pages = crawl_site(
        start_url=req.start_url,
        max_depth=req.max_depth
    )
    return build_user_flow(req.start_url, pages)
