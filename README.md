# FastAuth

Simple OAuth login with thrid party authentication provider.

To deploy:

1. Clone me
2. `cd` to `fastauth`
3. To run locally:
   1. Register the address `http://localhost:8000` as an ORCID endpoint at [ORCID developer tools](https://orcid.org/developer-tools)
   1. Create a file `fastauth/.env` like `fastauth/sample.env` with values ORCID registration
   2. `poetry install`
   3. `cd fastauth`
   4. `poetry run uvicorn main:app --reload`
   5. visit http://localhost:8000

