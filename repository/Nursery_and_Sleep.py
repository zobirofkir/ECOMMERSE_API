from fastapi import HTTPException, status
from models  import Nursery_and_Sleep
from database import SessionLocal
from schemas.schemas import Nursery_and_Sleeps


def create_Nursery_and_Sleep(create:Nursery_and_Sleeps):
    db = SessionLocal()
    create_Nursery = db.query(Nursery_and_Sleep).filter(Nursery_and_Sleep.Baby_cribs == create.Baby_cribs).first()
    if create_Nursery:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !!!")
    else:
        new_Nursery = Nursery_and_Sleep(
            Baby_cribs = create.Baby_cribs,
            Bassinets  = create.Bassinets,
            Changing_tables = create.Changing_tables,
            Baby_monitors = create.Baby_monitors,
            Swaddles_and_sleep_sacks = create.Swaddles_and_sleep_sacks,
            Mobiles_and_nightlights  = create.Mobiles_and_nightlights
        )
        db.add(new_Nursery)
        db.commit()
        db.refresh(new_Nursery)
        raise HTTPException(status_code=status.HTTP_201_CREATED, detail="This Nursery_and_Sleep has been created success")
    

def get_Nursery_and_Sleeping(id:int):
    db = SessionLocal()
    geting_Nursery_and_Sleep = db.query(Nursery_and_Sleep).filter(Nursery_and_Sleep.id == id).first()
    if geting_Nursery_and_Sleep:
        return {"This is Nursery_and_Sleep" :[
            {"Baby_cribs" :geting_Nursery_and_Sleep.Baby_cribs},
            {"Bassinets":geting_Nursery_and_Sleep.Bassinets},
            {"Changing_tables":geting_Nursery_and_Sleep.Changing_tables},
            {"Baby_monitors":geting_Nursery_and_Sleep.Baby_monitors},
            {"Swaddles_and_sleep_sacks":geting_Nursery_and_Sleep.Swaddles_and_sleep_sacks},
            {"Mobiles_and_nightlights":geting_Nursery_and_Sleep.Mobiles_and_nightlights}
        ]}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !!!")
    

def update_Nursery_and_Sleeping(id:int, update:Nursery_and_Sleeps):
    db = SessionLocal()
    update_Nursery = db.query(Nursery_and_Sleep).filter(Nursery_and_Sleep.id == id).first()
    if update_Nursery:
        update_Nursery.Baby_cribs == update.Baby_cribs
        update_Nursery.Bassinets == update.Bassinets
        update_Nursery.Changing_tables == update.Changing_tables
        update_Nursery.Baby_monitors == update.Baby_monitors
        update_Nursery.Swaddles_and_sleep_sacks == update.Swaddles_and_sleep_sacks
        update_Nursery.Mobiles_and_nightlights == update.Mobiles_and_nightlights
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail="updates success")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !!!")
    
def delete_Nursery_and_Sleeping(id:int):
    db = SessionLocal()
    deletd_Nur = db.query(Nursery_and_Sleep).filter(Nursery_and_Sleep.id == id).first()
    if deletd_Nur:
        db.delete(deletd_Nur)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail="deleted success")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !!!")