
lint:
	flake8 --show-source langoustine
	flake8 --show-source tests
	isort --check-only -rc langoustine --diff
	isort --check-only -rc tests --diff

test:
	pytest tests

install-dev:
	pip install -U -r requirements/dev.txt

install-ci:
	pip install -U -r requirements/ci.txt
