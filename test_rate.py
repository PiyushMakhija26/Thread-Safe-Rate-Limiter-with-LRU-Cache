from rate_limiter import RateLimiter
import time

def test_rate_limiting():
    limiter = RateLimiter(max_requests=2, time_window=5, cache_capacity=10)
    user = "test_user"

    print("Testing rate limiting: 2 requests per 5 seconds")
    print()

    for i in range(4):
        allowed, evicted = limiter.is_allowed(user)
        print(f"Request {i+1}: {'Allowed' if allowed else 'Blocked'}")
        if evicted:
            print(f"Evicted: {evicted}")
        time.sleep(1)  # 1 second between requests

    print()
    print("Waiting 6 seconds for window to reset...")
    time.sleep(6)

    allowed, evicted = limiter.is_allowed(user)
    print(f"After reset: {'Allowed' if allowed else 'Blocked'}")

if __name__ == "__main__":
    test_rate_limiting()