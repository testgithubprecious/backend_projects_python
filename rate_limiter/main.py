from rate_limiter import RateLimiter
import time

limiter = RateLimiter(max_requests=5, window_seconds=10)
user = "user_1"

print("🔁 Sending 7 rapid requests:")
for i in range(7):
    allowed = limiter.is_allowed(user)
    status = "✅ ALLOWED" if allowed else "❌ BLOCKED"
    print(f"Request {i+1}: {status}")
    time.sleep(1)

print("\n⏳ Waiting 10s to reset...")
time.sleep(10)

print("🔁 Sending again:")
for i in range(3):
    print(f"Request {i+1}: {'✅ ALLOWED' if limiter.is_allowed(user) else '❌ BLOCKED'}")

