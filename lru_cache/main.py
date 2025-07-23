from lru_cache import LRUCache

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # ✅ 1
cache.put(3, 3)         # ❌ evicts key 2
print(cache.get(2))    # ❌ -1
cache.put(4, 4)         # ❌ evicts key 1
print(cache.get(1))    # ❌ -1
print(cache.get(3))    # ✅ 3
print(cache.get(4))    # ✅ 4

