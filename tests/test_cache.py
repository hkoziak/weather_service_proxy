from app.cache import PerKeyTTLCache
import time


def test_per_key_ttl_cache():
    cache = PerKeyTTLCache()
    cache.set("test", {"city": "TestCity", "condition": "Sunny", "temperature": "20°C"}, ttl=1)

    assert cache.get("test") is not None  

    time.sleep(1.1)
    assert cache.get("test") is None  