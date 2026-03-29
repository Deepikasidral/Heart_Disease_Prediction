from pydantic import BaseModel

class User(BaseModel):
    Email: str
    age: int
    gender: str
    password: str