import time
from collections import deque
from threading import Lock

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window = window_seconds
        self.user_requests = {}  # user_id -> deque of timestamps
        self.lock = Lock()

    def is_allowed(self, user_id: str) -> bool:
        now = time.time()
        with self.lock:
            if user_id not in self.user_requests:
                self.user_requests[user_id] = deque()

            q = self.user_requests[user_id]

            # Clean old timestamps
            while q and now - q[0] > self.window:
                q.popleft()

            if len(q) < self.max_requests:
                q.append(now)
                return True
            else:
                return False

