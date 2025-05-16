import time
from threading import Lock
from typing import Optional
from app.schemas import WeatherResponse


class PerKeyTTLCache:
    def __init__(self):
        self._store = {}
        self._lock = Lock()

    def set(self, key: str, value: dict, ttl: int):
        expire_at = time.time() + ttl
        with self._lock:
            self._store[key] = (value, expire_at)

    def get(self, key: str) -> Optional[WeatherResponse]:
        with self._lock:
            item = self._store.get(key)
            if not item:
                return None
            value, expire_at = item
            if time.time() > expire_at:
                del self._store[key]
                return None
            return WeatherResponse(**value)

weather_cache = PerKeyTTLCache()