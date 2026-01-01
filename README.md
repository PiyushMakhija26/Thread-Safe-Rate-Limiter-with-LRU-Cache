# Thread-Safe Rate Limiter with LRU Cache

A simple, thread-safe rate limiter implementation using a sliding window and an LRU cache for efficient user data management. Includes a Streamlit web UI for easy testing and simulation.

## Features

- **Thread-Safe LRU Cache**: Evicts least recently used users when capacity is exceeded.
- **Sliding Window Rate Limiting**: Allows up to N requests per time window per user.
- **Streamlit UI**: Simple web interface to simulate requests and visualize results.
- **Unit Tests**: Comprehensive tests for rate limiting and LRU eviction.

## Architecture

```
rate_limiter/
├── rate_limiter/
│   ├── __init__.py
│   ├── cache.py        # Thread-safe LRU cache
│   ├── limiter.py      # Rate limiting logic
│   ├── models.py       # Data models
│   └── utils.py        # Utilities
├── app.py              # Streamlit UI
├── tests/
│   └── test_limiter.py # Unit tests
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd rate_limiter
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Streamlit App

```bash
streamlit run app.py
```

Open http://localhost:8501 in your browser. Enter:
- **User ID**: Identifier for the user
- **Max Requests**: Maximum requests allowed in the time window
- **Number of Requests to Simulate**: How many requests to test (up to 500)
- **Time Window**: Window duration in seconds

Click "Simulate Requests" to see allowed/blocked status, current rate, and LRU eviction messages.

### Running Tests

```bash
python -m unittest tests.test_limiter
```

## Example

With Max Requests = 5, Time Window = 60, simulating 10 requests:
- Requests 1-5: Allowed
- Requests 6-10: Blocked
- Current rate: 5 requests in window

## License

MIT License