from pydantic import BaseModel
from typing import List, Optional

class Chunk(BaseModel):
    id: str
    appendix: str
    page_start: int
    page_end: int
    text: str
