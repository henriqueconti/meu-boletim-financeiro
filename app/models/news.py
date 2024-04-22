from pydantic import BaseModel


class News(BaseModel):
    title: str
    url: str
    publishedAt: str
