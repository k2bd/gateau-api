# Python + Poetry REST API with FastAPI, hosted on GCP

## Getting started from the template
1. Create and test your API. Your app under `gateau_api.api:app` will be hosted on CloudRun when it's deployed.
1. Change your Cloud Run configuration in `cloudbuild.yaml`. By default, it will deploy an API that can be invoked with no authentication.
1. Configure Cloud Build in your GCP project to deploy from `cloudbuild.yaml` on a new tag push.
1. When you're ready to release the first version, run the release GitHub action.
1. Remove this section from `README.md`.
1. Happy hacking!

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
