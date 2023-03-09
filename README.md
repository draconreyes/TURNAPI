# TURNAPI

Basic API to manage turns

## Installation

### Pip

```bash
$ python -m venv venv
$ venv/Scripts/activate
$ pip install -r requirements.txt
```

## Environment variables
### Using environment variables depending on the value that these variables can take in your case you can guide yourself on the variables to use by looking at the .env_example file

## Run project with uvicorn
```bash
$ uvicorn config:app --reload
```
### Run test of the project

```bash
$ python -m unittest discover -s app/core/tests/
```
### Run Flake8
```bash
$ flake8  --exclude venv
```
