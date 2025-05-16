from fastapi import FastAPI, HTTPException
from app.schemas import WeatherRequest, WeatherResponse
from app.cache import weather_cache
from app.client import fetch_weather_data
from app.config import DEFAULT_TTL

app = FastAPI()


@app.post("/weather", response_model=WeatherResponse)
async def get_weather(payload: WeatherRequest):
    cache_key = payload.city.lower()

    if not payload.disable_cache:
        cached = weather_cache.get(cache_key)
        if cached:
            return cached

    try:
        response = await fetch_weather_data(payload.city)
    except Exception:
        raise HTTPException(status_code=502, detail="Weather service unavailable")

    weather_cache.set(cache_key, response.model_dump(), ttl=payload.ttl or DEFAULT_TTL)
    return response
