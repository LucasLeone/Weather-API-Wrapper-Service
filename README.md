# Weather API Wrapper Service

Third-party API integration, caching strategy, environment variable management.

API to check the Argentine weather.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Project

- First step is build the docker container with this command:

      $ docker compose -f docker-compose.local.yml build

- Then, do you have to run it:

      $ docker compose -f docker-compose.local.yml up

### Trying API

- For try the API, do you have to make a request to the endpoint:

      '[POST] http://127.0.0.1:8000/api/weather/'

- With a JSON like:

      '{"postal_code": "5900"}'


