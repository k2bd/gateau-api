# Gateau API

[![CI](https://github.com/k2bd/gateau-api/actions/workflows/ci.yml/badge.svg)](https://github.com/k2bd/gateau-api/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/k2bd/gateau-api/branch/main/graph/badge.svg?token=RNU7U9OTEZ)](https://codecov.io/gh/k2bd/gateau-api)

## Developing

Install [Poetry](https://python-poetry.org/) and `poetry install` the project

### Useful Commands

Note: if Poetry is managing a virtual environment for you, you may need to use `poetry run poe` instead of `poe`

- `poe autoformat` - Autoformat code
- `poe lint` - Linting
- `poe test` - Run Tests
- `poe local-server` - Run your API locally

### Releasing

Release a new version by running the release action on GitHub.
Cloud Build will automatically run a new deployment using `cloudbuild.yaml`.
