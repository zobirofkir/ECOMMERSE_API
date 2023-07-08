from fastapi import HTTPException, status
from database import Base, SessionLocal
from models import Diapering_and_Changing
from schemas.schemas import Diapering_Changings

def create_category_1(cate:Diapering_Changings):
    db = SessionLocal()
    existing_category = db.query(Diapering_and_Changing).filter(Diapering_and_Changing.Disposable_diapers == cate.Disposable_diapers).first()
    if existing_category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This category has been already existin in this database !")
    else:
        new_category = Diapering_and_Changing(
            Disposable_diapers = cate.Disposable_diapers,
            Cloth_diapers =cate.Cloth_diapers,
            Diaper_rash_creams = cate.Diaper_rash_creams,
            Changing_mats_or_pads = cate.Changing_mats_or_pads,
            Diaper_bags = cate.Diaper_bags
        )

        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return HTTPException(status_code=status.HTTP_201_CREATED, detail="Success")
    

def get_category_2(id:int):
    db = SessionLocal()
    geting_category = db.query(Diapering_and_Changing).filter(Diapering_and_Changing.id ==id).first()
    if geting_category:
        return {"This is all category":[
            {"Disposable_diapers":geting_category.Disposable_diapers},
            {"Cloth_diapers":geting_category.Cloth_diapers},
            {"Diaper_rash_creams":geting_category.Diaper_rash_creams},
            {"Changing_mats_or_pads":geting_category.Changing_mats_or_pads},
            {"Diaper_bags":geting_category.Diaper_bags}
        ]}
    
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not found This category !")