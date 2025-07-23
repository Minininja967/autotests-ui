from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


user_data = {
    "id": 1,
    "username": "username",
    "email": "user@gmail.com"
}

user = User(**user_data)
print(user)
print(user.is_active)

invalid_user_data = {
    "id": "one",
    "username": "username",
    "email": "user@gmail.com"
}

invalid_user =User(**invalid_user_data)
