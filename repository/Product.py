from fastapi import HTTPException, status
from schemas.schemas import Productss
from models import Product
from database import SessionLocal


def post_Product(create:Productss):
    db = SessionLocal()
    post_pro = db.query(Product).filter(Product.name == create.name).first()
    if post_pro:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This product name has been already used !!!")
    else:
        new_prod = Product(
            name = create.name,
            category = create.category,
            photos = create.photos,
            video = create.video,
            prix = create.prix
        )
        db.add(new_prod)
        db.commit()
        db.refresh(new_prod)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This product has been created")
    
def get_product(id:int):
    db = SessionLocal()
    get_pro = db.query(Product).filter(Product.id==id).first()
    if get_pro:
        return {"All product":[
            {"name":get_pro.name},
            {"category":get_pro.category},
            {"photos":get_pro.photos},
            {"video":get_pro.video},
            {"prix":get_pro.prix}
        ]}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not found !!!")
    

def update_product(id:int, update:Productss):
    db = SessionLocal()
    update_pro = db.query(Product).filter(Product.id==id).first()
    if update_pro:
        update_pro.name == update.name
        update_pro.category == update.category
        update_pro.photos == update.photos
        update_pro.video ==update.video
        update_pro.prix == update.prix
        raise HTTPException(status_code=status.HTTP_200_OK, detail="updated")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !")
    
def delete_product(id:int):
    db = SessionLocal()
    delete_pro = db.query(Product).filter(Product.id==id).first()
    if delete_pro:
        db.delete(delete_pro)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Product deleted")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !!!")
                            

