
class TrieNode:
    def __init__(self):
        self.children = {}
        self.ip_address = None  # Store IP if it's a full domain

class DNSResolver:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, domain, ip):
        parts = domain.strip().split('.')[::-1]  # Reverse domain parts
        node = self.root
        for part in parts:
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]
        node.ip_address = ip

    def resolve(self, domain):
        parts = domain.strip().split('.')[::-1]
        node = self.root
        for part in parts:
            if part not in node.children:
                return None
            node = node.children[part]
        return node.ip_address

