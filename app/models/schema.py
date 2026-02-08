from pydantic import BaseModel
from typing import List

class CrawlRequest(BaseModel):
    start_url: str
    max_depth: int = 3
    include_auth: bool = False

class Node(BaseModel):
    id: str
    label: str

from pydantic import BaseModel, Field
from pydantic import ConfigDict

class Edge(BaseModel):
    from_: str = Field(alias="from")
    to: str

    model_config = ConfigDict(
        populate_by_name=True
    )



class CrawlResponse(BaseModel):
    start_url: str
    nodes: List[Node]
    edges: List[Edge]
    global_navigation: List[str]
