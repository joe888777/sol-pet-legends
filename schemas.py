from typing import List, Union
from pydantic import BaseModel

class PetBase(BaseModel):
    name: str
    species: str

class PetCreate(PetBase):
    pass

class Pet(PetBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    pets: List[Pet] = []

    class Config:
        orm_mode = True
