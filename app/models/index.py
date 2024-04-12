from pydantic import BaseModel, field_validator


class Index(BaseModel):
    longName: str
    regularMarketChangePercent: float
    regularMarketPrice: float
    regularMarketOpen: float

    @field_validator('*')
    def round_floats(cls, value):
        if isinstance(value, float):
            return format(value, '.2f')
        return value
