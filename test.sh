#!/bin/sh

set -e
poetry run isort .
poetry run black .
poetry run flake8 --exclude=.venv .
poetry run pip-audit
