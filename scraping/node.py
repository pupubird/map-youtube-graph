class Node:
    def __init__(self, link, title, peers=None) -> None:
        self.link = link
        self.title = title
        if peers == None:
            self.peers = set()
        else:
            self.peers = peers
