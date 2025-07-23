from throttler import RequestThrottler
import time

throttler = RequestThrottler(max_requests=5, window_seconds=10)

user = "alice"

for i in range(7):
    if throttler.is_allowed(user):
        print(f"[{i}] Request allowed")
    else:
        print(f"[{i}] 🚫 Throttled")
    time.sleep(1)

