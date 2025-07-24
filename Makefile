.PHONY: test format lint run

test:
	pytest Test_main1.py
venv:
	python -m venv venv
	.venv\Scripts\activate


format:
	black .

lint:
	pylint main1.py

run:
	python main1.py
