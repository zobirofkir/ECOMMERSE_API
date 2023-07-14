from repository.Nursery_and_Sleep import create_Nursery_and_Sleep, get_Nursery_and_Sleeping, update_Nursery_and_Sleeping, delete_Nursery_and_Sleeping
from fastapi import APIRouter
from models import Nursery_and_Sleep
from schemas.schemas import Nursery_and_Sleeps

rou = APIRouter(
    prefix="/api/Nursery_and_Sleeping",
    tags=["Nursery_and_Sleeping"]
)

@rou.post("/")
def post_api(create:Nursery_and_Sleeps):
    return create_Nursery_and_Sleep(create)

@rou.get("/Nursery_and_Sleep")
def get_api(id:int):
    return get_Nursery_and_Sleeping(id)

@rou.put("/update")
def update_api(id:int, update:Nursery_and_Sleeps):
    return update_Nursery_and_Sleeping(id, update)

@rou.delete("/delete")
def delete_api(id:int):
    return delete_Nursery_and_Sleeping(id)