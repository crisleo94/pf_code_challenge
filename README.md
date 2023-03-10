# Requeriments
This project is built using [Pipenv](https://pipenv.pypa.io/en/latest/).
To start the virtual environment just clone the repo and run `pipenv shell`, this will create a new virtual environment with the Python version inside the `Pipfile` under `[requires]` (for this case `python_version = "3.9"`)

If for some reason you need a `requirements.txt` file you can obtain it by running: `pipenv requirements > requirements.txt`

You need to build and run the DB from the `Dockerfile`

# Preinsert DATA
There are 2 `JSON` files with default information:
```
seed_factory_data.json
seed_sprocket_types.json
```
To insert this information into the database you need to first have the container running and the inside the virtualenv execute `python insert_json.py` this will insert the data into the database

# Goal
Build a RESTful api that services requests for sprocket factory data and sprockets.

# TODO
- [ ] An endpoint that returns all sprocket factory data
- [ ] An endpoint that returns factory data for a given factory id
- [ ] An endpoint that returns sprockets for a given id
- [ ] An endpoint that will create new sprocket
- [ ] An endpoint that will update sprocket for a given id
- [ ] Add `.env` file