from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..database import get_db
from .. import schemas, models
from sqlalchemy.orm import Session
from .. import utils, oauth2


router = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.user_email == user_credentials.username).first()

    # USER AUTHENTICATION
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    if not utils.verify(user_credentials.password, user.user_password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    # USER AUTHORIZATION

    # create token
    access_token = oauth2.create_access_token(data={"user_id": user.user_id})

    # return token
    return {"access_token": access_token, "token_type": "bearer"}
