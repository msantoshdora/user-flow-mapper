from fastapi import FastAPI
from app.api.crawl import router as crawl_router

app = FastAPI(title="Website Crawler API", version="1.0")

app.include_router(crawl_router, prefix="/api")
