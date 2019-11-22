.PHONY: test

help:
	@echo
	@echo "🛠 UTILS"
	@echo
	@echo "repl:      open REPL with bpython"
	@echo
	@echo "📊 CODE QUALITY"
	@echo
	@echo "test:      run unit tests, view basic coverage report in terminal"
	@echo "cov:       view HTML coverage report in browser"
	@echo "fmt:       auto-format using Black"
	@echo "lint:      lint using flake8"
	@echo
	@echo "📦 DEPENDENCIES"
	@echo
	@echo "install:   install dependencies from requirements.txt"
	@echo "purge:     remove any installed pkg *not* in requirements.txt"
	@echo "freeze:    freeze dependencies into requirements.txt"
	@echo

#
# 🛠 UTILS
#

repl:
	source venv/bin/activate; bpython

#
# 📊 CODE QUALITY
#

test:
	coverage run --source='src' -m pytest -v && coverage report -m

cov:
	coverage html; open htmlcov/index.html

fmt:
	black src test

lint:
	flake8 src test

#
# 📦 DEPENDENCIES
#

install:
	pip install -r requirements.txt

purge:
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

freeze:
	pip freeze > requirements.txt
