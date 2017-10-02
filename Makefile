runserver:
	python ./source/app.py

test:
	 PYTHONPATH=. pytest --cov
