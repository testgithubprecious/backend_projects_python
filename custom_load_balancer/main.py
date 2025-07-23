from load_balancer import RoundRobinBalancer, HashBasedBalancer

servers = ["Server-A", "Server-B", "Server-C"]

rr = RoundRobinBalancer(servers)
hb = HashBasedBalancer(servers)

print("🔁 Round Robin:")
for i in range(6):
    print(f"Request {i+1} → {rr.get_server()}")

print("\n🔐 Hash-Based (Sticky):")
clients = ["alice", "bob", "charlie", "alice", "bob"]
for client in clients:
    print(f"Client {client} → {hb.get_server(client)}")

