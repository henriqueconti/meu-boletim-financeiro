from pydantic import BaseModel


class News(BaseModel):
    title: str
    url: str
    description: str
    content: str
    publishedAt: str
