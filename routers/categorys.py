from fastapi import APIRouter
from repository.category import create_category_1, get_category_2
from schemas.schemas import Diapering_Changings

router = APIRouter(
    prefix='/api/category',
    tags=['Catefory']
)


@router.post('/')
def posted_created(cate:Diapering_Changings):
    return create_category_1(cate)



@router.get('/category')
def catego(id:int):
    return get_category_2(id)