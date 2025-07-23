from session_store import SessionStore
import time

store = SessionStore()
store.set("abc123", {"user": "Alice"}, ttl=5)

print("Immediately:", store.get("abc123"))  # ✅ Should return data

print("Waiting 6 seconds...")
time.sleep(6)

print("After expiry:", store.get("abc123"))  # ❌ Should return None

