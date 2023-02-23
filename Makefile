.PHONY: test
test:
	poetry run python -m pytest --doctest-modules

.PHONY: fmt
fmt:
	isort .
	black .
