from sqlalchemy.orm import Session
import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        for attr, value in user.dict().items():
            setattr(db_user, attr, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def create_pet(db: Session, pet: schemas.PetCreate, user_id: int):
    db_pet = models.Pet(**pet.dict(), owner_id=user_id)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

def update_pet(db: Session, pet_id: int, pet: schemas.PetUpdate):
    db_pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    if db_pet:
        for attr, value in pet.dict().items():
            setattr(db_pet, attr, value)
        db.commit()
        db.refresh(db_pet)
    return db_pet

def get_pet(db: Session, pet_id: int):
    return db.query(models.Pet).filter(models.Pet.id == pet_id).first()

def list_pets(db: Session, owner_id: int):
    return db.query(models.Pet).filter(models.Pet.owner_id == owner_id)
