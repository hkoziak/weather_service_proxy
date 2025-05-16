from pydantic import BaseModel
from typing import Optional


class WeatherRequest(BaseModel):
    city: str
    disable_cache: Optional[bool] = False
    ttl: Optional[int] = None  #seconds


class WeatherResponse(BaseModel):
    city: str
    condition: str
    temperature: str
