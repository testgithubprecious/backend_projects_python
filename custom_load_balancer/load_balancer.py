class RoundRobinBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server


class HashBasedBalancer:
    def __init__(self, servers):
        self.servers = servers

    def get_server(self, client_id):
        index = hash(client_id) % len(self.servers)
        return self.servers[index]

