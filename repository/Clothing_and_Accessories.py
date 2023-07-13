from models import Clothing_and_Accessories
from fastapi import HTTPException, status
from database import SessionLocal
from schemas.schemas import Clothing_and_Accessoriess


def create_Clothing_and_Accessories(poste:Clothing_and_Accessoriess):
    db = SessionLocal()
    post_Clothing = db.query(Clothing_and_Accessories).filter(Clothing_and_Accessories.Onesies_and_bodysuits == poste.Onesies_and_bodysuits).first()
    if post_Clothing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST , detail="This Clothing_and_Accessories has been already in this database !!!")

    else:
        new_Clothing = Clothing_and_Accessories(
            Onesies_and_bodysuits = poste.Onesies_and_bodysuits,
            Baby_pajamas = poste.Baby_pajamas,
            Socks_and_booties = poste.Socks_and_booties,
            Hats_and_mittens = poste.Hats_and_mittens,
            Bibs_and_burp_cloths = poste.Bibs_and_burp_cloths,
            Baby_blankets = poste.Baby_blankets
        )
        db.add(new_Clothing)
        db.commit()
        db.refresh(new_Clothing)
        raise HTTPException(status_code=status.HTTP_201_CREATED, detail="Clothing_and_Accessories has been created")


def get_Clothing_and_Accessories(id:int):
    db = SessionLocal()
    geting_Clothing = db.query(Clothing_and_Accessories).filter(Clothing_and_Accessories.id == id).first()
    if geting_Clothing:
        return {"This is Clothing_and_Accessories" :[
            {"Onesies_and_bodysuits" : geting_Clothing.Onesies_and_bodysuits},
            {"Baby_pajamas" : geting_Clothing.Baby_pajamas},
            {"Socks_and_booties" : geting_Clothing.Socks_and_booties},
            {"Hats_and_mittens" : geting_Clothing.Hats_and_mittens},
            {"Bibs_and_burp_cloths" : geting_Clothing.Bibs_and_burp_cloths},
            {"Baby_blankets" : geting_Clothing.Baby_blankets}
        ]}
    
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !!!")
    


def update_Clothing_and_Accessories(id:int, update:Clothing_and_Accessoriess):
    db = SessionLocal()
    update_Clothing = db.query(Clothing_and_Accessories).filter(Clothing_and_Accessories.id == id).first()
    if update_Clothing:
        update_Clothing.Onesies_and_bodysuits == update.Onesies_and_bodysuits
        update_Clothing.Baby_pajamas == update.Baby_pajamas
        update_Clothing.Socks_and_booties == update.Socks_and_booties
        update_Clothing.Hats_and_mittens == update.Hats_and_mittens
        update_Clothing.Bibs_and_burp_cloths == update.Bibs_and_burp_cloths
        update_Clothing.Baby_blankets == update.Baby_blankets
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail="updated success ")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST , detail="Error !")

def delete_Clothing_and_Accessories(id:int):
    db = SessionLocal()
    delete_Clothing_and_Accessories = db.query(Clothing_and_Accessories).filter(Clothing_and_Accessories.id == id).first()
    if delete_Clothing_and_Accessories:
        db.delete(delete_Clothing_and_Accessories)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Clothing_and_Accessories has been deleted")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !!!")
    



