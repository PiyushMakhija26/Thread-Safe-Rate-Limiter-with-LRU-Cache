import unittest
from rate_limiter import RateLimiter
import time

class TestRateLimiter(unittest.TestCase):
    def test_allow_within_limit(self):
        limiter = RateLimiter(3, 10, 10)
        user = "user1"
        for _ in range(3):
            allowed, _ = limiter.is_allowed(user)
            self.assertTrue(allowed)
        allowed, _ = limiter.is_allowed(user)
        self.assertFalse(allowed)

    def test_time_window(self):
        limiter = RateLimiter(2, 1, 10)  # 2 per 1 second
        user = "user2"
        limiter.is_allowed(user)
        limiter.is_allowed(user)
        allowed, _ = limiter.is_allowed(user)
        self.assertFalse(allowed)
        time.sleep(1.1)
        allowed, _ = limiter.is_allowed(user)
        self.assertTrue(allowed)

    def test_lru_eviction(self):
        limiter = RateLimiter(1, 60, 2)  # capacity 2
        user1 = "user1"
        user2 = "user2"
        user3 = "user3"
        limiter.is_allowed(user1)
        limiter.is_allowed(user2)
        _, evicted = limiter.is_allowed(user3)
        self.assertEqual(evicted, user1)  # assuming LRU

if __name__ == '__main__':
    unittest.main()