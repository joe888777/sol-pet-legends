from typing import Union, Optional
from pydantic import BaseModel

class PetBase(BaseModel):
    name: str
    species: str
    exp: int

class PetCreate(PetBase):
    pass

class Pet(PetBase):
    id: int
    class Config:
        orm_mode = True

class PetUpdate(BaseModel):
    id: int
    name: str
    species: str
    exp: int

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    name: Optional[str]
    wallet_address: Optional[str]
    hashed_password: Optional[str]

class User(UserBase):
    id: int
    wallet_address: Optional[str] = ""
    pets: list[Pet] = []

    class Config:
        orm_mode = True
