from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.post("/pets/", response_model=schemas.Pet)
def create_pet(pet: schemas.PetCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_pet(db, pet, user_id)

@app.put("/pets/{pet_id}", response_model=schemas.Pet)
def update_pet(pet_id: int, pet: schemas.PetUpdate, db: Session = Depends(get_db)):
    return crud.update_pet(db, pet_id, pet)

@app.get("/pet/{pet_id}", response_model=schemas.Pet)
def update_pet(pet_id: int, pet: schemas.PetUpdate, db: Session = Depends(get_db)):
    return crud.update_pet(db, pet_id, pet)

@app.get("/pets/", response_model=list[schemas.Pet])
def list_pets(user_id: int, db: Session = Depends(get_db)):
    return crud.list_pets(db, user_id)