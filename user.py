from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr
    userid: int

    def model(self):
        return {
            "name": self.name,
            "email": self.email,
            "userid": self.userid
        }
