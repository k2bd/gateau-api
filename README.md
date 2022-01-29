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
This will create a new tag, and also update the appropriate major version tag (`v1`, `v2`, ...).

Updating the major version tags will cause Cloud Build to create or update that version's deployment automatically and host it at e.g. `v1.(your configured domain)`. You may need to configure your domain's DNS if you're creating an endpoint for a new major version and you use an external provider. See the domain mappings page linked [here](https://cloud.google.com/run/docs/mapping-custom-domains#map) for instructions.
