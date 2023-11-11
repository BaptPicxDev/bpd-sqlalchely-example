SHELL := /bin/bash
.SHELLFLAGS = -ec
.ONESHELL:
.SILENT:

.PHONY: help
help:
	grep -E '^\.PHONY: [a-zA-Z0-9_-]+ .*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: build-venv ## Create virtual environment and install requirements (local dev)
build-venv:
	echo "Creating python3 virtual environment with poetry"
	poetry config virtualenvs.in-project true
	if [ ! -f pyproject.toml ]; then
		echo "Generating pyproject.toml file."
		poetry init -n
	fi
	make check-dependencies
	poetry install --no-root

.PHONY: add-production-packages ## Add production package to pyproject.toml (from pypi.org) using poetry
add-production-packages:
	echo "Adding production packages"
	poetry add pandas
	poetry add numpy

.PHONY: add-dev-packages ## Add dev package to pyproject.toml(from pypi.org) using poetry
add-dev-packages:
	echo "Installing dev packages"
	poetry add --group dev pytest
	poetry add --group dev pytest-cov
	poetry add --group dev pytest-mock
	poetry add --group dev flake8
	poetry add --group dev pdoc3

.PHONY: check-dependencies ## Ensure that all dependencies are installed
check-dependencies:
	echo "Ensure dependencies are installed"
	poetry check

.PHONY: run-pytest ## Run pytest using pytest
run-pytest:
	echo "Running pytest"
	poetry run pytest -vv --cov=src/ tests/

.PHONY: run-flake8 ## Control the code quality
run-flake8:
	echo "Runnin flake8"
	poetry run flake8 --exit-zero --color auto src/ tests/

.PHONY: run-pdoc ## Generate documentation
run-pdoc:
	echo "Running pdoc"
	poetry run pdoc3 --force --html src/*.py

.PHONY: run ## Run main.py with production
run:
	poetry run python3 main.py

.PHONY: run-dev ## Run main.py with development
run-dev:
	poetry run python3 main.py --dev

.PHONY: clean-venv ## Clean virtual environment (local dev)
clean-venv:
	echo "Removing python3 virtual environment using poetry"

.PHONY: clean ## Clean the folder and subfolders
clean:
	echo "Cleaning folder"
	find . -maxdepth 1 -type f -name "*coverage*" -not -name "coverage.svg" -o -name "flake*" -delete
	find . -maxdepth 2 -type d -name .pytest_cache -o -name .venv -o -name docs -o -name __pycache__ -o -name html | xargs rm -rf

