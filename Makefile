.PHONY: test
test:
	poetry run python -m pytest --doctest-modules
