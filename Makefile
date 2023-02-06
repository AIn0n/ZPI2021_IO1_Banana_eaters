test:
	python3 -m unittest tests/test.py

precommit:
	pip freeze > requirements.txt
	python3 -m black .

run:
	streamlit run src/app.py
