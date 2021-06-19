GRAPH_FILE = ./scraping/graph.json

.PHONY: install
install:
	@pip3 install pip-tools autopep8 pylint
	@pip-compile
	@pip3 install -r requirements.txt

run:
	@python3 scraping/app.py

visualize:
ifeq ($(shell test -e $(GRAPH_FILE) && echo -n yes),yes)
		$(MAKE) run
endif
	@cp scraping/graph.json frontend/src/assets/data.json
	@cd frontend
	@npm install --prefix ./frontend
	@npm run watch --prefix ./frontend