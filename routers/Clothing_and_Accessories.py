from repository.Clothing_and_Accessories import create_Clothing_and_Accessories, get_Clothing_and_Accessories, update_Clothing_and_Accessories, delete_Clothing_and_Accessories
from fastapi import APIRouter
from schemas.schemas import Clothing_and_Accessoriess


roter = APIRouter(
    prefix="/api/Clothing_and_Accessories",
    tags=["Clothing_and_Accessories"]
)

@roter.post("/")
def created_api(poste:Clothing_and_Accessoriess):
    return create_Clothing_and_Accessories(poste)

@roter.get('/Clothing_and_Accessories')
def get_api(id:int):
    return get_Clothing_and_Accessories(id)

@roter.put("/update")
def update_api(id:int, update:Clothing_and_Accessoriess):
    return update_Clothing_and_Accessories(id, update)


@roter.delete("/delete")
def delete_api(id:int):
    return delete_Clothing_and_Accessories(id)