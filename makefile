run:
	python3 src

install:
	pip install -e .['dev']

create_activate_venv:
	python3 -m venv .venv
	source .venv/bin/activate


run-i:
	python3 -i src/app

tests:
	python3 discord-bot.tests
