from fastapi import APIRouter
from repository.Diapering_and_Changing import create_category_1, get_category_2, update_category, delete_categoey
from schemas.schemas import Diapering_Changings

router = APIRouter(
    prefix='/api/Diapering_and_Changing',
    tags=['Diapering_and_Changing']
)


@router.post('/')
def posted_created(cate:Diapering_Changings):
    return create_category_1(cate)



@router.get('/category')
def catego(id:int):
    return get_category_2(id)


@router.put('/update')
def updated_cat(upd:Diapering_Changings, id:int):
    return update_category(upd, id)


@router.delete('/delete')
def deleted_cat(id:int):
    return delete_categoey(id)


