run:
	python3 app/app.py

install:
	pip install -e .['dev']

create_activate_venv:
	python3 -m venv .venv;source .venv/bin/activate


run-i:
	python3 -i app/app.py

tests:
	python3 tests/tests.py
