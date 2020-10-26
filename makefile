install:
	pip install -e .['dev']

create_activate_venv:
	python3 -m venv .venv
	source .venv/bin/activate

run:
	python3 src/app