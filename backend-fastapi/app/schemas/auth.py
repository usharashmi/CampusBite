from pydantic import BaseModel, EmailStr


class RegisterSchema(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    phone: str


class LoginSchema(BaseModel):
    email: EmailStr
    password: str