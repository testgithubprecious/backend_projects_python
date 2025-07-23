class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None
        self.is_variable = False
        self.variable_name = None
        self.is_wildcard = False

class CustomRouter:
    def __init__(self):
        self.root = RouteTrieNode()

    def add_route(self, path, handler):
        parts = self._split_path(path)
        node = self.root
        for part in parts:
            key = part
            if part.startswith(":"):
                key = ":"
            elif part.startswith("*"):
                key = "*"
            if key not in node.children:
                child = RouteTrieNode()
                if part.startswith(":"):
                    child.is_variable = True
                    child.variable_name = part[1:]
                elif part.startswith("*"):
                    child.is_wildcard = True
                    child.variable_name = part[1:]
                node.children[key] = child
            node = node.children[key]
        node.handler = handler

    def match(self, path):
        parts = self._split_path(path)
        params = {}
        handler = self._match_helper(self.root, parts, 0, params)
        return handler, params

    def _match_helper(self, node, parts, index, params):
        if index == len(parts):
            return node.handler if node.handler else None

        part = parts[index]

        if part in node.children:
            handler = self._match_helper(node.children[part], parts, index + 1, params)
            if handler:
                return handler

        if ":" in node.children:
            var_node = node.children[":"]
            params[var_node.variable_name] = part
            handler = self._match_helper(var_node, parts, index + 1, params)
            if handler:
                return handler

        if "*" in node.children:
            wild_node = node.children["*"]
            remaining = "/".join(parts[index:])
            params[wild_node.variable_name] = remaining
            return wild_node.handler

        return None

    def _split_path(self, path):
        return [p for p in path.strip("/").split("/") if p]

