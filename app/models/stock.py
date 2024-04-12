from pydantic import BaseModel, field_validator


class Stock(BaseModel):
    regularMarketChangePercent: float
    regularMarketPrice: float
    regularMarketOpen: float
    symbol: str

    @field_validator('*')
    def round_floats(cls, value):
        if isinstance(value, float):
            return format(value, '.2f')
        return value
