# FastAuth

Simple OAuth login with thrid party authentication provider.

To deploy:

1. Clone me
2. `cd` to `fastauth`
3. Create a file `fastauth/.env` like `fastauth/sample.env` with values from your [ORCID developer tools](https://orcid.org/developer-tools).
4. To run locally:
   1. `poetry install`
   2. `cd fastauth`
   3. `poetry run uvicorn main:app --reload`
   4. visit http://localhost:8000
5. To deploy to [deta](https://deta.sh):
   1. From the root folder of the repo 
   2. `deta new --python --name=fastauth fastauth`
   3. Visit the url provided by deta

