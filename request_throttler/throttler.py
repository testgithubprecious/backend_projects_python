import time
from collections import defaultdict, deque

class RequestThrottler:
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window = window_seconds
        self.user_requests = defaultdict(deque)

    def is_allowed(self, user_id):
        now = time.time()
        queue = self.user_requests[user_id]

        # Remove old timestamps outside the window
        while queue and now - queue[0] > self.window:
            queue.popleft()

        if len(queue) < self.max_requests:
            queue.append(now)
            return True
        else:
            return False

