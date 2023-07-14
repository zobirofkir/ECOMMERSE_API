from models import Description
from database import SessionLocal
from fastapi import HTTPException, status
from schemas.schemas import Descriptionss

def post_description(post:Descriptionss):
    db = SessionLocal()
    new_describe = db.query(Description).filter(Description.email == post.email).first()
    if new_describe:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This email has been already used !!!")
    else:    
        new_des = Description(username=post.username, email=post.email  ,descriptions=post.descriptions)
        db.add(new_des)
        db.commit()
        db.refresh(new_des)
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Description posted")
    


def get_description(id:int):
    db=SessionLocal()
    get_Describ = db.query(Description).filter(Description.id==id).first()
    if get_Describ:
        return {"This is description":[get_Describ.username ,get_Describ.descriptions]}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error !!!")


