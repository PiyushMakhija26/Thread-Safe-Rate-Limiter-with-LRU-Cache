import streamlit as st
from rate_limiter import RateLimiter

st.title("Rate Limiter Simulator")

user_id = st.text_input("User ID")
max_requests = st.number_input("Max Requests", min_value=1, value=500)
num_requests = st.number_input("Number of Requests to Simulate", min_value=1, max_value=500, value=10)
time_window = st.number_input("Time Window (seconds)", min_value=1, value=60)

if st.button("Simulate Requests"):
    limiter = RateLimiter(max_requests, time_window, cache_capacity=10)
    results = []
    evicted_messages = []
    for i in range(num_requests):
        allowed, evicted = limiter.is_allowed(user_id)
        results.append(f"Request {i+1}: {'Allowed' if allowed else 'Blocked'}")
        if evicted:
            evicted_messages.append(f"Evicted user: {evicted}")
    current_count = limiter.get_current_count(user_id)
    st.write("Results:")
    for res in results:
        st.write(res)
    st.write(f"Current rate status: {current_count} requests in window")
    if evicted_messages:
        for msg in evicted_messages:
            st.write(msg)
    else:
        st.write("No LRU eviction occurred")