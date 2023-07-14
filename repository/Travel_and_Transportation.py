from fastapi import HTTPException, status
from models import Travel_and_Transportation
from schemas.schemas import Travel_and_Transportations
from database import SessionLocal

def create_Travel_and_Transportation(create:Travel_and_Transportations):
    db = SessionLocal()
    create_Travel = db.query(Travel_and_Transportation).filter(Travel_and_Transportation.Strollers == create.Strollers).first()
    if create_Travel:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !!!")
    else:
        new_Travel_and_Transportation = Travel_and_Transportation(
            Strollers = create.Strollers,
            Car_seats = create.Car_seats,
            Baby_carriers = create.Baby_carriers,
            Diaper_backpacks = create.Diaper_backpacks,
            Travel_cribs = create.Travel_cribs,
            Portable_high_chairs = create.Portable_high_chairs
        )

        db.add(new_Travel_and_Transportation)
        db.commit()
        db.refresh(new_Travel_and_Transportation)
        raise HTTPException(status_code=status.HTTP_201_CREATED, detail="created")
    


def get_Travel_and_Transportation(id:int):
    db = SessionLocal()
    geting_Travel = db.query(Travel_and_Transportation).filter(Travel_and_Transportation.id == id).first()
    if geting_Travel:
        return {"This is Travel_and_Transportation": [
            {"Strollers" : geting_Travel.Strollers},
            {"Car_seats":geting_Travel.Car_seats},
            {"Baby_carriers":geting_Travel.Baby_carriers},
            {"Diaper_backpacks":geting_Travel.Diaper_backpacks},
            {"Travel_cribs":geting_Travel.Travel_cribs},
            {"Portable_high_chairs":geting_Travel.Portable_high_chairs}
        ]}
    
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !!!")
    
    
def update_Travel_and_Transportation(id:int, update:Travel_and_Transportations):
    db = SessionLocal()
    update_Travel_and_Transportation = db.query(Travel_and_Transportation).filter(Travel_and_Transportation.id == id).first()
    if update_Travel_and_Transportation:
        update_Travel_and_Transportation.Strollers == update.Strollers
        update_Travel_and_Transportation.Car_seats == update.Car_seats
        update_Travel_and_Transportation.Baby_carriers == update.Baby_carriers
        update_Travel_and_Transportation.Diaper_backpacks == update.Diaper_backpacks
        update_Travel_and_Transportation.Travel_cribs == update.Travel_cribs
        update_Travel_and_Transportation.Portable_high_chairs == update.Portable_high_chairs

        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Travel_and_Transportation has been updated")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !!!")
    

def delete_Travel_and_Transportation(id:int):
    db = SessionLocal()
    delete_Travel = db.query(Travel_and_Transportation).filter(Travel_and_Transportation.id == id).first()
    if delete_Travel:
        db.delete(delete_Travel)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Travel_and_Transportation has been deleted")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error !!!')
    
