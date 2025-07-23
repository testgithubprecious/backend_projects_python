import time
import heapq
import threading


class SessionStore:
    def __init__(self):
        self.sessions = {}  # session_id -> (data, expiry_time)
        self.expiry_heap = []  # Min-heap of (expiry_time, session_id)
        self.lock = threading.Lock()
        self._start_cleaner()

    def set(self, session_id, data, ttl):
        expiry = time.time() + ttl
        with self.lock:
            self.sessions[session_id] = (data, expiry)
            heapq.heappush(self.expiry_heap, (expiry, session_id))

    def get(self, session_id):
        with self.lock:
            if session_id not in self.sessions:
                return None
            data, expiry = self.sessions[session_id]
            if time.time() > expiry:
                del self.sessions[session_id]
                return None
            return data

    def _expire_sessions(self):
        while True:
            with self.lock:
                now = time.time()
                while self.expiry_heap and self.expiry_heap[0][0] <= now:
                    _, sid = heapq.heappop(self.expiry_heap)
                    if sid in self.sessions and self.sessions[sid][1] <= now:
                        del self.sessions[sid]
            time.sleep(1)  # Run every second

    def _start_cleaner(self):
        thread = threading.Thread(target=self._expire_sessions, daemon=True)
        thread.start()

