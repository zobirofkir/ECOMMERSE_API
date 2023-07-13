from fastapi import FastAPI
from routers.Diapering_and_Changing import router
from routers.Feeding_and_Nursing import routers
from routers.Bathing_and_Groominge import ruter
from routers.Clothing_and_Accessories import roter


app = FastAPI()

app.include_router(router)
app.include_router(routers)
app.include_router(ruter)
app.include_router(roter)