## Weather Proxy API

A FastAPI-based  proxy that fetches weather data from an external server (`wttr.in`) and caches results with custom cache time to minimize calls.

---

##  Main features

- Proxy for weather requests using [wttr.in](https://wttr.in/)
- Optional cache bypass 
- Configurable cache expiration per request
- Swagger API doc

---

## API 

### **POST** `/weather`

Weather data for a city, with optional caching control.

#### Request Payload

```
{
  "city": "Kyiv",
  "disable_cache": false,
  "ttl": 600
}
```

"city" string is required, rest are optional - "disable_cache" is false by default and "ttl" is 3600.

## Design / Architecture choices

The project itself doesn't have a complex "architecture" to say so, it has two main components - caching mechanism and app in general. 
- For app I chose FastAPI because it doesn't have a lot of overhead and keeps the app itself lightweight, also because of the general features of the framework. 
- For testing I used pytest because of the convenient testing structure that it enhances. 
- Cache was implemented from scratch. Main point for it was thread-safe implementation and per-key caching settings.

Project file structure follows clean and convenient pattern to make adding of the new code easy. 

## Launching app and tests

Local (venv) run from the core project folder (weather_service_proxy): 
```
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Docker run from the core project folder (weather_service_proxy):

```
docker build -t weather-api .
docker run -p 8000:8000 weather-api
```

Testing (from the core project folder): ```pytest```

Swagger UI - http://localhost:8000/docs .
