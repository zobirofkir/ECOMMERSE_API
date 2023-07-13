from repository.Bathing_and_Grooming import create_Bathing_and_Grooming, get_Bathing_and_Grooming, update_Bathing_and_Grooming, delete_category
from fastapi import APIRouter
from schemas.schemas import Bathing_and_Groomings


ruter = APIRouter(
    prefix='/api/Bathing_and_Grooming',
    tags=['Bathing_and_Grooming']
)

@ruter.post('/')
def created(cat:Bathing_and_Groomings):
    return create_Bathing_and_Grooming(cat)



@ruter.get('/get')
def get_id(id:int):
    return get_Bathing_and_Grooming(id)

@ruter.put('/update')
def update_id(id:int, update:Bathing_and_Groomings):
    return update_Bathing_and_Grooming (id, update)




@ruter.delete('/delete')
def deletd_by_id(id:int):
    return delete_category(id)