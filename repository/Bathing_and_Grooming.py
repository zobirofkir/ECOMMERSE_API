from database import Base, SessionLocal
from models import Bathing_and_Grooming
from schemas.schemas import Bathing_and_Groomings
from fastapi import HTTPException, status

def create_Bathing_and_Grooming(cat:Bathing_and_Groomings):
    db = SessionLocal()
    existing_Bathing_and_Grooming = db.query(Bathing_and_Grooming).filter(Bathing_and_Grooming.Baby_bathtubs==cat.Baby_bathtubs).first()
    if existing_Bathing_and_Grooming:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bathing_and_Grooming has been already in database !")
    else:

        new_Bathing_and_Grooming = Bathing_and_Grooming(
            Baby_bathtubs =cat.Baby_bathtubs,
            Baby_shampoo_and_body_wash = cat.Baby_shampoo_and_body_wash,
            Hooded_towels = cat.Hooded_towels,
            Baby_brushes_and_combs = cat.Baby_brushes_and_combs,
            Nail_clippers = cat.Nail_clippers,
            Baby_lotion_and_oil =cat.Baby_lotion_and_oil
    
        )

        db.add(new_Bathing_and_Grooming)
        db.commit()
        db.refresh(new_Bathing_and_Grooming)
        return HTTPException(status_code=status.HTTP_201_CREATED, detail="Bathing_and_Grooming has been created")
    
    

def get_Bathing_and_Grooming(id:int):
     db = SessionLocal()
     geting_Bathing_and_Grooming = db.query(Bathing_and_Grooming).filter(Bathing_and_Grooming.id == id).first()
     if geting_Bathing_and_Grooming:
          return {"This is all Bathing_and_Grooming":[
               {"Baby_bathtubs":geting_Bathing_and_Grooming.Baby_bathtubs},
               {"Baby_shampoo_and_body_wash":geting_Bathing_and_Grooming.Baby_shampoo_and_body_wash},
               {"Hooded_towels":geting_Bathing_and_Grooming.Hooded_towels},
               {"Baby_brushes_and_combs":geting_Bathing_and_Grooming.Baby_brushes_and_combs},
               {"Nail_clippers":geting_Bathing_and_Grooming.Nail_clippers},
               {"Baby_lotion_and_oil":geting_Bathing_and_Grooming.Baby_lotion_and_oil}
          ]}
     else:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found !")
     


def update_Bathing_and_Grooming(id:int, update:Bathing_and_Groomings):
     db=SessionLocal()
     update_Bathing_and_Grooming = db.query(Bathing_and_Grooming).filter(Bathing_and_Grooming.id==id).first()
     if update_Bathing_and_Grooming:
          update_Bathing_and_Grooming.Baby_bathtubs == update.Baby_bathtubs
          update_Bathing_and_Grooming.Baby_shampoo_and_body_wash == update.Baby_shampoo_and_body_wash
          update_Bathing_and_Grooming.Hooded_towels == update.Hooded_towels
          update_Bathing_and_Grooming.Baby_brushes_and_combs == update.Baby_brushes_and_combs
          update_Bathing_and_Grooming.Nail_clippers == update.Nail_clippers
          update_Bathing_and_Grooming.Baby_lotion_and_oil == update.Baby_lotion_and_oil

          db.commit()
          raise HTTPException(status_code=status.HTTP_200_OK, detail="updated success")
     
     else:
          raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !!!")
     

def delete_category(id:int):
     db = SessionLocal()
     delete_Bathing_and_Groomings = db.query(Bathing_and_Grooming).filter(Bathing_and_Grooming.id == id).first()
     if delete_Bathing_and_Groomings:
          db.delete(delete_Bathing_and_Groomings)
          db.commit()
          raise HTTPException(status_code=status.HTTP_200_OK, detail="deleted success")
     else:
          raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not Found !!")
     