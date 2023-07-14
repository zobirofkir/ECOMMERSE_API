from repository.Toys_and_Entertainment import create_Toys_and_Entertainment, delete_Toys_and_Entertainment, update_Toys_and_Entertainment, get_Toys_and_Entertainment
from fastapi import APIRouter
from schemas.schemas import Toys_and_Entertainments 
from models import Toys_and_Entertainment

Toys = APIRouter(
    prefix="/api/Toys_and_Entertainment",
    tags=['Toys_and_Entertainment']
)

@Toys.post('/')
def post_api(create:Toys_and_Entertainments):
    return create_Toys_and_Entertainment(create)

@Toys.get('/Toys_and_Entertainments')
def get_api(id:int):
    return get_Toys_and_Entertainment(id)

@Toys.put('/update')
def update_api(id:int, update:Toys_and_Entertainments):
    return update_Toys_and_Entertainment(id, update)

@Toys.delete("/delete")
def delete_api(id:int):
    return delete_Toys_and_Entertainment(id)