from fastapi import APIRouter, Depends, status, HTTPException
from schema import showUser
from schema import user as userSchema
from engine.loadb import load
from models import user as userModel
from sqlalchemy.orm import Session
from typing import Dict, List

router = APIRouter(
    tags=["user"]
)


@router.post("/user", response_model=showUser.ShowUser,
             status_code=status.HTTP_201_CREATED)
def create_user(request: userSchema.User, db: Session = Depends(load)):
    new_user = userModel.Users(name=request.name, phone=request.phone,
                               email=request.email, address=request.address, password=request.password)
    data = db.all(userModel.Users)
    phone = request.phone
    email = userModel.Users.email
    print(data)
    print("...................")
    print(phone)

    if phone in data:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"user with phone {phone} exists")
    if email in data:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"user with email {email} exists")
    db.new(new_user)
    db.save()
    return new_user
