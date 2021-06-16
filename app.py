from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from graph import Graph
from node import Node
import json

options = Options()
options.add_extension('./ublock.crx')

driver = webdriver.Chrome('./chromedriver', options=options)

start_node = None


def recurse(link, current_node, depth):
    if depth > 3:
        return
    print("Accessing link", link, end=" ")
    if link == start_node.link and len(start_node.peers) != 0:
        return
    # Expand the graph
    driver.get(link)
    suggestions = driver.find_elements_by_css_selector('.iv-click-target')
    print(f"Has {len(suggestions)} amount of peers")
    peers = []

    for suggestion in suggestions:
        link = suggestion.get_attribute('href')
        title = suggestion.find_element_by_css_selector(
            '.iv-card-primary-link').get_property('innerText')
        new_node = Node(link=link, title=title, peers=set([current_node]))
        current_node.peers.add(new_node)
        peers.append(new_node)

    for peer in peers:
        recurse(peer.link, peer, depth + 1)


start_node_link = 'https://www.youtube.com/watch?v=6TEwVDNA7bI'
start_node_title = 'Diagnose Your Backend and Improve the Frontend User Experience with DevTools Waterfall (Deep Dive)'
start_node = Node(link=start_node_link, title=start_node_title)
recurse(start_node_link, start_node, 1)

driver.close()

graph = Graph(start_node=start_node)
output = graph.ouput_to_json()

with open("graph.json", 'w') as f:
    f.writelines(json.dumps(output, indent=2))
