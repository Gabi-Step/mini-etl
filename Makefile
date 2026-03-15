.PHONY: setup run

setup:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv sync

run:
	uv run flask --app mini_etl init-db
	uv run flask --app mini_etl load-demo-data
	uv run flask --app mini_etl run --debug