from pydantic import BaseModel, validator


class Index(BaseModel):
    longName: str
    regularMarketChangePercent: float
    regularMarketPrice: float
    regularMarketPreviousClose: float

    @validator('*')
    def round_floats(cls, value):
        if isinstance(value, float):
            return format(value, '.2f')
        return value
