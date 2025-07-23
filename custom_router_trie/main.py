from trie_router import CustomRouter
import handlers

router = CustomRouter()
router.add_route("/user/:id", handlers.user_profile)
router.add_route("/files/*path", handlers.file_server)

# Try some test routes
paths = [
    "/user/42",
    "/files/images/2025/banner.png",
    "/files/docs/readme.txt",
    "/user",
    "/unknown"
]

for path in paths:
    handler, params = router.match(path)
    if handler:
        print(f"Path: {path} -> {handler(params)}")
    else:
        print(f"Path: {path} -> 404 Not Found")

