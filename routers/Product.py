from fastapi import APIRouter
from repository.Product import post_Product, get_product, update_product, delete_product
from schemas.schemas import Productss
from models import Product

prod = APIRouter(
    prefix="/api/Product",
    tags=["Product"]
)

@prod.post('/')
def post_api(create:Productss):
    return post_Product(create)

@prod.get('/Product')
def get_api(id:int):
    return get_product(id)

@prod.put('/update')
def update_api(id:int, update:Productss):
    return update_product(id, update)

@prod.delete("/delete")
def delete_api(id:int):
    return delete_product(id)