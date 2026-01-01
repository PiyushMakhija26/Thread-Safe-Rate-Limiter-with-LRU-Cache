from dataclasses import dataclass
from typing import Optional
import time

@dataclass
class Request:
    user_id: str
    timestamp: float = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = time.time()