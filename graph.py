class Graph:
    def __init__(self, start_node) -> None:
        self.start_node = start_node
        self.nodes = set()
        self.traverse_inorder(self.start_node)

    def traverse_inorder(self, node):
        if node.link in [n.link for n in self.nodes]:
            return
        self.nodes.add(node)
        for n in node.peers:
            self.traverse_inorder(n)

    def ouput_to_json(self):
        data = {
            "nodes": [
                {
                    "id": node.link,
                    "name": node.title,
                    "color": "black",
                    "textHeight": 5
                }
                for node in self.nodes
            ],
            "links": [
                {
                    "source": node.link,
                    "target": p.link
                }
                for node in self.nodes
                for p in node.peers
            ]
        }
        return data
