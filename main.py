from fastapi import FastAPI
from routers.Diapering_and_Changing import router
from routers.Feeding_and_Nursing import routers
from routers.Bathing_and_Groominge import ruter
from routers.Clothing_and_Accessories import roter
from routers.Nursery_and_Sleep import rou
from routers.Travel_and_Transportation import Travel
from routers.Toys_and_Entertainment import Toys
from routers.Description import Descriptionse
from routers.Product import prod

app = FastAPI()

app.include_router(router)
app.include_router(routers)
app.include_router(ruter)
app.include_router(roter)
app.include_router(rou)
app.include_router(Travel)
app.include_router(Toys)
app.include_router(prod)
app.include_router(Descriptionse)
