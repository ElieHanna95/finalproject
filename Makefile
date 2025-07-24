.PHONY: test format lint run

test:
	pytest Test_main1.py

format:
	black .

lint:
	pylint main1.py

run:
	python main1.py
