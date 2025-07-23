from dns_trie import DNSResolver

resolver = DNSResolver()

# Insert domains
resolver.insert("google.com", "8.8.8.8")
resolver.insert("mail.google.com", "8.8.4.4")
resolver.insert("openai.com", "1.1.1.1")

# Resolve
print(resolver.resolve("google.com"))       # 8.8.8.8
print(resolver.resolve("mail.google.com"))  # 8.8.4.4
print(resolver.resolve("openai.com"))       # 1.1.1.1
print(resolver.resolve("chat.openai.com"))  # None

