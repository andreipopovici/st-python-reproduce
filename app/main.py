from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from supertokens_python import (
    InputAppInfo,
    SupertokensConfig,
    get_all_cors_headers,
    init,
)
from supertokens_python.framework.fastapi import get_middleware
from supertokens_python.recipe import emailpassword, session

init(
    framework="fastapi",
    mode="asgi",
    app_info=InputAppInfo(
        app_name="st-python-reproduce",
        api_domain="http://localhost:8000",
        website_domain="http://localhost:3000",
        api_base_path="/auth",
        website_base_path="/auth",
    ),
    supertokens_config=SupertokensConfig(
        connection_uri="http://supertokens:3567",
        api_key="test-key-that-is-long-enough-to-use",
    ),
    recipe_list=[emailpassword.init(), session.init()],
)


app = FastAPI()
app.add_middleware(get_middleware())
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)


@app.get("/")
async def read_main():
    return {"message": "Hello World"}
