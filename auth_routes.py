from fastapi import APIRouter, status
from db.database import Session, engine
from schemas import SignUpModel
from db.models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash

auth_router=APIRouter(prefix="/auth", tags=["auth"])
session=Session(bind=engine)

#1️⃣
@auth_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user:SignUpModel):
    db_email=session.query(User).filter(User.email==user.email).first()
    if(db_email is not None):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="User email already exists")
    db_username=session.query(User).filter(User.username==user.username).first()
    if(db_username is not None):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="User username already exists")
    new_user=User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        is_active=user.is_active,
        is_staff=user.is_staff
    )
    session.add(new_user)
    session.commit()
    return(new_user)

"""
1) En mi microservicio anterior use use un response model de platillo al mandar un nuevo platillo
    eso esta bien si el platillo si se manda, sin emabrgo, si encuentra que el nombre o el id
    ya esta en uso entonces devuelve un error htpp, sin embargo el response model es de tipo platillo.
    Lo mejor es quitar el response model
"""