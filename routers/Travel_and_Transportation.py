from repository.Travel_and_Transportation import create_Travel_and_Transportation, get_Travel_and_Transportation, update_Travel_and_Transportation, delete_Travel_and_Transportation
from fastapi import APIRouter
from models import Travel_and_Transportation
from schemas.schemas import Travel_and_Transportations


Travel = APIRouter(
    prefix='/api/Travel_and_Transportation',
    tags=['Travel_and_Transportation']
)

@Travel.post('/')
def post_api(create:Travel_and_Transportations):
    return create_Travel_and_Transportation(create)


@Travel.get('/Travel_and_Transportations')
def get_api(id:int):
    return get_Travel_and_Transportation(id)

@Travel.put('/update')
def update_api(id:int, update:Travel_and_Transportations):
    return update_Travel_and_Transportation(id, update)

@Travel.delete('/delete')
def delete_api(id:int):
    return delete_Travel_and_Transportation(id)