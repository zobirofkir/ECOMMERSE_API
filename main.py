from fastapi import FastAPI
from routers.categorys import router

app = FastAPI()

app.include_router(router)