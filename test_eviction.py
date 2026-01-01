from rate_limiter import RateLimiter

def test_eviction():
    limiter = RateLimiter(max_requests=1, time_window=60, cache_capacity=2)
    users = ["user1", "user2", "user3"]

    print("Simulating requests for multiple users with cache capacity 2")
    print("Max requests: 1 per 60 seconds")
    print()

    for user in users:
        allowed, evicted = limiter.is_allowed(user)
        print(f"Request for {user}: {'Allowed' if allowed else 'Blocked'}")
        if evicted:
            print(f"LRU Eviction: Evicted {evicted}")
        print(f"Current cache: {list(limiter.cache.cache.keys())}")
        print()

if __name__ == "__main__":
    test_eviction()