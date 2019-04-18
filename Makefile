.PHONY: test

help:
	@echo
	@echo "🐛 DEBUG"
	@echo
	@echo "repl:    	debug using bpython"
	@echo
	@echo "📊 CODE QUALITY"
	@echo
	@echo "cov:     	view HTML coverage report in browser"
	@echo "fmt:     	auto format code using Black"
	@echo "lint:    	lint using flake8"
	@echo "test:    	run unit tests, view basic coverage report in terminal"
	@echo
	@echo "📦 DEPENDENCIES"
	@echo
	@echo "freeze:   	freeze dependencies into requirements.txt"
	@echo "install:   	install dependencies from requirements.txt"
	@echo "reset:   	remove any installed pkg *not* in requirements.txt"
	@echo

cov:test
	coverage html; open htmlcov/index.html

fmt:
	black src test

lint:
	flake8 src test

pipfr:
	pip freeze > requirements.txt

pipin:
	pip install -r requirements.txt

piprs:
	@echo "🔍 - DISCOVERING UNSAVED PACKAGES\n"
	pip freeze > pkgs-to-rm.txt
	@echo
	@echo "📦 - UNINSTALL ALL PACKAGES\n"
	pip uninstall -y -r pkgs-to-rm.txt
	@echo
	@echo "♻️  - REINSTALL SAVED PACKAGES\n"
	pip install -r requirements.txt
	@echo
	@echo "🗑  - UNSAVED PACKAGES REMOVED\n"
	diff pkgs-to-rm.txt requirements.txt | grep '<'
	@echo
	rm pkgs-to-rm.txt
	@echo

test:
	coverage run --source='src' -m pytest -v && coverage report -m
