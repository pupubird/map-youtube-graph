.PHONY: install
install:
	@pip3 install pip-tools autopep8 pylint
	@pip-compile
	@pip3 install -r requirements.txt

run:
	@python3 app.py

visualize:
	@cp graph.json frontend/src/assets/data.json
	@cd frontend
	@npm install --prefix ./frontend
	@npm run watch --prefix ./frontend