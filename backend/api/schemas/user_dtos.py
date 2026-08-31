from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str 
    user_email: str 

class UserCreate(UserBase):
    pass 

class UserUpdatePartial(UserBase):
    username: str | None 
    user_email: str | None 

class User(UserBase):
    model_config = ConfigDict(
        from_attributes=True
    )
    id: int 