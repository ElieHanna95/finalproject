.PHONY: test format lint run

test:
	pytest

format:
	black .

lint:
	pylint main1.py

run:
	python main1.py
