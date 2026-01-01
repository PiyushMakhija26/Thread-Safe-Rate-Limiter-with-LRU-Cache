from collections import OrderedDict
from threading import Lock
from typing import Any, Optional

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.lock = Lock()

    def get(self, key: str) -> Optional[Any]:
        with self.lock:
            if key in self.cache:
                self.cache.move_to_end(key)
                return self.cache[key]
            return None

    def put(self, key: str, value: Any) -> Optional[str]:
        evicted = None
        with self.lock:
            if key in self.cache:
                self.cache.move_to_end(key)
            else:
                if len(self.cache) >= self.capacity:
                    evicted, _ = self.cache.popitem(last=False)
            self.cache[key] = value
        return evicted

    def __contains__(self, key: str) -> bool:
        with self.lock:
            return key in self.cache