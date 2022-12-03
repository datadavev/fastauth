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
4. To deploy to [deta](https://deta.sh):
   1. From the root folder of the repo 
   2. `deta new --python --name=fastauth fastauth`
   3. Register the new deta url as an ORCID endpoint at [ORCID developer tools](https://orcid.org/developer-tools)
   4. Create a file `fastauth/.env` like `fastauth/sample.env` with values form the ORCID registration
   5. `cd fastauth`
   6. `deta update -e .env`
   7. Visit the url provided by deta

There's currently a demo on deta at: https://fc845o.deta.dev
