install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=describe_stats test_*.py &&\
	pytest --nbval-lax describe_stats.ipynb

format:	
	black *.py 

lint:
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	#ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

#replace xxx with the .py (without the .py) file that you want to run
deploy:
	python -m describe_stats &&\
		jupyter notebook describe_stats.ipynb

#if u want a different run file that's different from deploy
run:
	python -m describe_stats &&\
		jupyter notebook describe_stats.ipynb
		
all: install lint test format deploy
