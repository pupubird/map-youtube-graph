# Map youtube graph

A simple script to map all the referenced videos using "card suggestion" any of the youtube channel as a graph, example shown in `graph.json`

## Getting started

To get this project up and running, you need to download [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) of your OS at your root directory.

Then, simply change parameters at `scraping/app.py` of your preferences.

Run `make run` to start the scraping, it will generate `graph.json` at the root directory.

To visualize, run `make visualize`
