from repository.Description import post_description, get_description
from models import Description
from schemas.schemas import Descriptionss
from fastapi import APIRouter

Descriptionse = APIRouter(
    prefix='/api/Description',
    tags=['Description']
)

@Descriptionse.post('/')
def post_api (post:Descriptionss):
    return post_description(post)

@Descriptionse.get('/Description')
def get_api(id:int):
    return get_description(id)