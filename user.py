from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr
    userid: int


user = User(name="Alice", email="kyhrishi@gmail.com", userid=1)
print(user.model)
