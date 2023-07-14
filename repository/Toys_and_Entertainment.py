from models import Toys_and_Entertainment
from schemas.schemas import Toys_and_Entertainments
from fastapi import HTTPException, status
from database import SessionLocal


def create_Toys_and_Entertainment(create:Toys_and_Entertainments):
    db = SessionLocal()
    create_Toys = db.query(Toys_and_Entertainment).filter(Toys_and_Entertainment.Rattles_and_teethers == create.Rattles_and_teethers).first()
    if create_Toys:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Error !!!")
    else:
        new_Toys = Toys_and_Entertainment(
            Rattles_and_teethers = create.Rattles_and_teethers,
            Soft_toys  = create.Soft_toys,
            Activity_gyms = create.Activity_gyms,
            Musical_toys = create.Musical_toys,
            Books_for_infants  = create.Books_for_infants,
            Stacking_toys = create.Stacking_toys
        )

        db.add (new_Toys)
        db.commit()
        db.refresh(new_Toys)
        raise HTTPException(status_code=status.HTTP_201_CREATED, detail="Created")
    



def get_Toys_and_Entertainment(id:int):
    db=SessionLocal()
    get_Toys = db.query(Toys_and_Entertainment).filter(Toys_and_Entertainment.id == id).first()
    if get_Toys:
        return {"Toys_and_Entertainment": [
            {"Rattles_and_teethers":get_Toys.Rattles_and_teethers},
            {"Soft_toys":get_Toys.Soft_toys},
            {"Activity_gyms":get_Toys.Activity_gyms},
            {"Musical_toys":get_Toys.Musical_toys},
            {"Books_for_infants":get_Toys.Books_for_infants},
            {"Stacking_toys":get_Toys.Stacking_toys}
        ]}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !!!")
    

def update_Toys_and_Entertainment(id:int, update:Toys_and_Entertainments):
    db = SessionLocal()
    update_toys = db.query(Toys_and_Entertainment).filter(Toys_and_Entertainment.id == id).first()
    if update_toys:
        update_toys.Rattles_and_teethers == update.Rattles_and_teethers
        update_toys.Soft_toys ==update.Soft_toys
        update_toys.Activity_gyms == update.Activity_gyms
        update_toys.Musical_toys == update.Musical_toys
        update_toys.Books_for_infants==update.Books_for_infants
        update_toys.Stacking_toys==update.Stacking_toys
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail="updated")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !!!")
    


def delete_Toys_and_Entertainment(id:int):
    db = SessionLocal()
    delete_toys = db.query(Toys_and_Entertainment).filter(Toys_and_Entertainment.id == id).first()
    if delete_toys:
        db.delete(delete_toys)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Deleted")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !!!")