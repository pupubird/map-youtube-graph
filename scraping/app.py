from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from node import Node
import json


UBLOCK_PATH = './ublock.crx'
CHROME_DRIVER_PATH = './chromedriver'
CHANNEL_NAME = "Hussein Nasser"
YOUTUBE_WATCH_SUFFIX = "youtube.com/watch"
CARD_A_TAG_CSS_CLASS = '.iv-click-target'
CARD_TITLE_TAG_CSS_CLASS = '.iv-card-primary-link'
CARD_CHANNEL_NAME_TAG_CSS_CLASS = '.iv-card-meta-info > li:first-child'
START_LINK = 'https://www.youtube.com/watch?v=6TEwVDNA7bI'
START_LINK_TITLE = 'Diagnose Your Backend and Improve the Frontend User Experience with DevTools Waterfall (Deep Dive)'

options = Options()
options.add_extension(UBLOCK_PATH)

driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)

start_node = None
nodes = set()


def recurse(link, current_node):
    """A recursion to build all the nodes with peers"""
    print("Accessing link", link, end=" ")
    # If self-referencing is happening, ignore this node
    if link == start_node.link and len(start_node.peers) != 0:
        return
    # Expand the graph
    driver.get(link)
    # Only scrape this channel videos
    if CHANNEL_NAME not in driver.page_source:
        return
    suggestions = driver.find_elements_by_css_selector(CARD_A_TAG_CSS_CLASS)
    print(f"Has {len(suggestions)} amount of peers")
    peers = []
    nodes.add(current_node)
    for suggestion in suggestions:
        link = suggestion.get_attribute('href')
        # Some urls might not necessarily be a youtube video, catching edge cases
        if YOUTUBE_WATCH_SUFFIX not in link:
            continue
        title = suggestion.\
            find_element_by_css_selector(CARD_TITLE_TAG_CSS_CLASS).\
            get_property('innerText')
        channel = suggestion.find_element_by_css_selector(
            CARD_CHANNEL_NAME_TAG_CSS_CLASS).get_property('innerText')
        if CHANNEL_NAME not in channel:
            continue
        # Build new node and add current node as peer
        new_node = Node(link=link, title=title, peers=set([current_node]))
        current_node.peers.add(new_node)
        peers.append(new_node)

    for peer in peers:
        if peer.link in [n.link for n in nodes]:
            continue
        # Call this recursion on each new built node
        recurse(peer.link, peer)


start_node = Node(link=START_LINK, title=START_LINK_TITLE)
recurse(START_LINK, start_node)

driver.close()

with open("graph.json", 'w') as f:
    f.writelines(json.dumps({
        "nodes": [
            {
                "id": node.link,
                "name": node.title,
                "color": "black",
                "textHeight": 5
            }
            for node in nodes
        ],
        "links": [
            {
                "source": node.link,
                "target": p.link
            }
            for node in nodes
            for p in node.peers
        ]
    }, indent=2))
