from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from db.database import Session, engine
from schemas import SignUpModel
from db.models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT
from schemas import LogInModel
from fastapi.encoders import jsonable_encoder

auth_router=APIRouter(prefix="/auth", tags=["auth"])
session=Session(bind=engine)

#1️⃣
@auth_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user:SignUpModel):
    """
        ## Crea un usuario
    """
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

#LogIn
@auth_router.post("/login", status_code=200)
async def login(user:LogInModel, Authorize:AuthJWT=Depends()):
    """
        ## Loggea un usuario
    """
    db_user=session.query(User).filter(User.username==user.username).first()
    if(db_user and check_password_hash(db_user.password, user.password)):
        acces_token=Authorize.create_access_token(subject=db_user.username)
        refresh_token=Authorize.create_refresh_token(subject=db_user.username)
        response={
            "access":acces_token,
            "refresh":refresh_token
        }
        return jsonable_encoder(response)
    raise HTTPException(status_code=HTTPException_400_BAD_REQUEST,
        detail="Invalid username or password")

#2️⃣Refresh token
@auth_router.get("/refresh")
async def refresh_token(Authorize:AuthJWT=Depends()):
    """
        ## Nos da un token de refresh
    """
    try:
        Authorize.jwt_refresh_token_required()
    except Exception as e:
        raise HTTPException(status_code=HTTPException_401_UNAUTHORIZED,
        detail="Provide a valid refresh token")
    current_user=Authorize.get_jwt_subject()
    access_token=Authorize.create_access_token(subject=current_user)
    return jsonable_encoder({"access":access_token})
