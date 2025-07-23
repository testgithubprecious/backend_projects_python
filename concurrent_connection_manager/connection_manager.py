import threading
import time
from queue import Queue

class ConnectionManager:
    def __init__(self, max_active, max_queue):
        self.active_limit = threading.Semaphore(max_active)
        self.waiting_queue = Queue(maxsize=max_queue)
        self.lock = threading.Lock()

    def connect(self, client_id):
        if self.active_limit.acquire(blocking=False):
            self._handle_client(client_id)
        elif not self.waiting_queue.full():
            self.waiting_queue.put(client_id)
            self._log(f"Client {client_id} queued.")
        else:
            self._log(f"Client {client_id} rejected: queue full.")

    def _handle_client(self, client_id):
        def task():
            self._log(f"Client {client_id} connected.")
            time.sleep(2)  # simulate work
            self._log(f"Client {client_id} disconnected.")
            self.active_limit.release()

            if not self.waiting_queue.empty():
                next_client = self.waiting_queue.get()
                self.connect(next_client)

        threading.Thread(target=task).start()

    def _log(self, message):
        with self.lock:
            print(message)

