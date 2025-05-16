from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_weather_success(monkeypatch):
    async def mock_fetch(city: str):
        from app.schemas import WeatherResponse
        return WeatherResponse(city=city, condition="Sunny", temperature="+20°C")

    monkeypatch.setattr("app.main.fetch_weather_data", mock_fetch)

    response = client.post("/weather", json={"city": "Kyiv"})
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == "Kyiv"
    assert data["condition"] == "Sunny"
    assert data["temperature"] == "+20°C"