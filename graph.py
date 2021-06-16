class Graph:
    def __init__(self, start_node) -> None:
        self.start_node = start_node
        self.nodes = set()
        self.traverse_inorder(self.start_node)

    def traverse_inorder(self, node):
        if node.link in [node.link for node in self.nodes]:
            return
        self.nodes.add(node)
        for n in node.peers:
            self.traverse_inorder(n)

    def ouput_to_json(self):
        return [{
            "title": node.title,
            "link": node.link,
            "peers": [p.link for p in node.peers]
        } for node in self.nodes]
