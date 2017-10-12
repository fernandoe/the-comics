runserver:
	python ./src/app.py

test:
	 pytest --cov

install:
	 pip install -r requirements.txt
