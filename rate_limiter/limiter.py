from .cache import LRUCache
from .utils import current_time
from typing import List, Optional

class RateLimiter:
    def __init__(self, max_requests: int, time_window: int, cache_capacity: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.cache = LRUCache(cache_capacity)

    def is_allowed(self, user_id: str) -> tuple[bool, Optional[str]]:
        now = current_time()
        timestamps = self.cache.get(user_id)
        if timestamps is None:
            timestamps = []
        # Remove old timestamps
        timestamps = [t for t in timestamps if now - t < self.time_window]
        allowed = len(timestamps) < self.max_requests
        if allowed:
            timestamps.append(now)
        evicted = self.cache.put(user_id, timestamps)
        return allowed, evicted

    def get_current_count(self, user_id: str) -> int:
        now = current_time()
        timestamps = self.cache.get(user_id)
        if timestamps is None:
            return 0
        timestamps = [t for t in timestamps if now - t < self.time_window]
        return len(timestamps)