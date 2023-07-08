from repository.Feeding_and_Nursing import create_feeding, geting_feeding, update_feeding, delete_Feeding_and_Nursing
from fastapi import APIRouter
from schemas.schemas import Feeding_and_Nursings



routers = APIRouter(
    prefix="/api/Feeding_and_Nursing",
    tags=["Feeding_and_Nursing"]
)


@routers.post('/')
def created_feeding(pos:Feeding_and_Nursings):
    return create_feeding(pos)

@routers.get("/get")
def geting_data_feeding(id:int):
    return geting_feeding(id)

@routers.put("/update")
def updated(upd:Feeding_and_Nursings, id:int):
    return update_feeding(upd, id)

@routers.delete("/delete")
def deleted(id:int):
    return delete_Feeding_and_Nursing(id)