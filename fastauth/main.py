"""
A FastAPI application demonstrating OAuth2 login using ORCID
"""

import json

import authlib.integrations.starlette_client
import fastapi
import fastapi.middleware.cors
import fastapi.requests
import fastapi.responses
import fastapi.staticfiles
import fastapi.templating
import starlette.config
import starlette.middleware.sessions

app = fastapi.FastAPI()
app.mount("/static", fastapi.staticfiles.StaticFiles(directory="static"), name="static")
templates = fastapi.templating.Jinja2Templates(directory="templates")
config = starlette.config.Config(".env")

app.add_middleware(
    starlette.middleware.sessions.SessionMiddleware,
    secret_key=config("APPLICATION_KEY", default="some-random-string"),
)
app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth = authlib.integrations.starlette_client.OAuth(config)
oauth.register(
    name="ORCID",
    server_metadata_url="https://orcid.org/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)


@app.get("/", response_class=fastapi.responses.HTMLResponse)
async def homepage(request: fastapi.requests.Request):
    user = request.session.get("user", None)
    return templates.TemplateResponse("index.html", {"request": request, "user": user})


@app.route("/login")
async def login(request: fastapi.requests.Request):
    # absolute url for callback
    # we will define it below
    redirect_uri = request.url_for("auth")
    return await oauth.ORCID.authorize_redirect(request, redirect_uri)


@app.route("/auth")
async def auth(request: fastapi.requests.Request):
    try:
        token = await oauth.ORCID.authorize_access_token(request)
    except authlib.integrations.starlette_client.OAuthError as error:
        return fastapi.responses.HTMLResponse(f"<h1>{error.error}</h1>")
    # <=0.15
    # user = await oauth.google.parse_id_token(request, token)
    user = token.get("userinfo")
    if user is not None:
        user = dict(user)
        user["access_token"] = token.get("access_token")
        user["token_type"] = token.get("token_type")
        request.session["user"] = user
    return fastapi.responses.RedirectResponse(url="/")


@app.get("/logout")
async def logout(request: fastapi.requests.Request):
    request.session.pop("user", None)
    return fastapi.responses.RedirectResponse(url="/")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
