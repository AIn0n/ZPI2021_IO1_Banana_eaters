test:
	python3 -m unittest tests/test.py

precommit:
	pip freeze > requirements.txt
	python3 -m black *.py

run:
	streamlit run src/app.py
