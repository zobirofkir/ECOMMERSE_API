from fastapi import HTTPException, status
from schemas.schemas import Feeding_and_Nursings
from models import Feeding_and_Nursing
from database import SessionLocal

def create_feeding(pos:Feeding_and_Nursings):
    db = SessionLocal()
    existing_feeding = db.query(Feeding_and_Nursing).filter(Feeding_and_Nursing.Baby_bottles == pos.Baby_bottles).first()
    if existing_feeding:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This Feeding_and_Nursing has been already existing in this database !")
    else:
        new_feeding = Feeding_and_Nursing(
            Baby_bottles = pos.Baby_bottles,
            Breast_pumps = pos.Breast_pumps,
            Formula_milk  = pos.Formula_milk,
            Nursing_pillows = pos.Nursing_pillows,
            Bottle_sterilizers = pos.Baby_bottles,
            Baby_food_makers = pos.Baby_food_makers
        )
        db.add(new_feeding)
        db.commit()
        db.refresh(new_feeding)
        return HTTPException(status_code=status.HTTP_200_OK, detail="This Feeding_and_Nursing has been created success")


def geting_feeding(id:int):
    db = SessionLocal()
    get_feedings = db.query(Feeding_and_Nursing).filter(Feeding_and_Nursing.id == id).first()
    if get_feedings:
        return {"This is Feeding_and_Nursing " :[
            {"Baby_bottles":get_feedings.Baby_bottles},
            {"Breast_pumps":get_feedings.Breast_pumps},
            {"Formula_milk":get_feedings.Formula_milk},
            {"Nursing_pillows":get_feedings.Nursing_pillows},
            {"Bottle_sterilizers":get_feedings.Bottle_sterilizers},
            {"Baby_food_makers":get_feedings.Baby_food_makers}
        ]}
    
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not found anything in Feeding_and_Nursing ! ")
    

def update_feeding(upd:Feeding_and_Nursings, id:int):
    db = SessionLocal()
    updated_Feeding_and_Nursings = db.query(Feeding_and_Nursing).filter(Feeding_and_Nursing.id == id).first()
    if updated_Feeding_and_Nursings:
        updated_Feeding_and_Nursings.Baby_bottles == upd.Baby_bottles
        updated_Feeding_and_Nursings.Breast_pumps == upd.Breast_pumps
        updated_Feeding_and_Nursings.Formula_milk == upd.Formula_milk
        updated_Feeding_and_Nursings.Nursing_pillows == upd.Nursing_pillows
        updated_Feeding_and_Nursings.Bottle_sterilizers == upd.Bottle_sterilizers
        updated_Feeding_and_Nursings.Baby_food_makers == upd.Baby_food_makers
        
        db.commit()
        
        return HTTPException(status_code=status.HTTP_200_OK, detail="updated ")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !")
    

def delete_Feeding_and_Nursing(id:int):
    db = SessionLocal()
    deleted_Feeding_and_Nursing = db.query(Feeding_and_Nursing).filter(Feeding_and_Nursing.id == id).first()
    if deleted_Feeding_and_Nursing:
        db.delete(deleted_Feeding_and_Nursing)
        db.commit()
        return HTTPException(status_code=status.HTTP_200_OK, detail="Has been deleted")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Error delete !")
    
    