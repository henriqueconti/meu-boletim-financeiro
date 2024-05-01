from pydantic import BaseModel, validator


class Stock(BaseModel):
    regularMarketChangePercent: float
    regularMarketPrice: float
    regularMarketPreviousClose: float
    symbol: str

    @validator('*')
    def round_floats(cls, value):
        if isinstance(value, float):
            return format(value, '.2f')
        return value
