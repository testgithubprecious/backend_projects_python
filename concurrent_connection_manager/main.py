from connection_manager import ConnectionManager
import threading
import time

manager = ConnectionManager(max_active=3, max_queue=5)

def simulate_client(client_id):
    time.sleep(0.1 * client_id)  # Stagger arrivals
    manager.connect(client_id)

# Simulate 10 clients
for i in range(10):
    threading.Thread(target=simulate_client, args=(i + 1,)).start()

