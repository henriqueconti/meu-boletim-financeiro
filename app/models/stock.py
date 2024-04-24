from pydantic import BaseModel, field_validator


class Stock(BaseModel):
    regularMarketChangePercent: float
    regularMarketPrice: float
    regularMarketPreviousClose: float
    symbol: str

    @field_validator('*')
    def round_floats(cls, value):
        if isinstance(value, float):
            return format(value, '.2f')
        return value
