from fastapi import FastAPI
from routers.Diapering_and_Changing import router
from routers.Feeding_and_Nursing import routers

app = FastAPI()

app.include_router(router)
app.include_router(routers)