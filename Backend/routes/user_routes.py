from fastapi import APIRouter, HTTPException
from db import users_collection
from models.user import User
from utils.hash import hash_password, verify_password

router = APIRouter()

# Register User
@router.post("/register")
def register_user(user: User):
    existing = users_collection.find_one({"Email": user.Email})
    
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)

    users_collection.insert_one(user_dict)

    return {"message": "User registered successfully"}

# Login User
@router.post("/login")
def login_user(user: User):
    db_user = users_collection.find_one({"Email": user.Email})

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid password")

    return {
        "message": "Login successful",
        "user_id": str(db_user["_id"])   # ✅ ADD THIS LINE
    }