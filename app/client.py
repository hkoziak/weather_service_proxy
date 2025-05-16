import httpx
from app.schemas import WeatherResponse
from app.config import WEATHER_API_FORMAT


async def fetch_weather_data(city: str) -> WeatherResponse:
    url = WEATHER_API_FORMAT.format(city=city)
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, timeout=5.0)
        if resp.status_code != 200:
            raise ValueError("Bad response from weather provider")

        content = resp.text.strip()  
        parts = content.split(":")
        if len(parts) != 2 or "," not in parts[1]:
            raise ValueError("Unexpected response format")

        condition, temperature = parts[1].split(",")
        return WeatherResponse(city=parts[0], condition=condition.strip(), temperature=temperature.strip())
