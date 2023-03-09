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
### You can see the documentation of the api in the following path
http://host:8000/docs
![image](https://user-images.githubusercontent.com/50085428/223954520-32392d34-a615-40d7-a373-77867c2b1f92.png)
