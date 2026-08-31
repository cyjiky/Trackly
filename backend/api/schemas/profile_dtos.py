from pydantic import BaseModel, ConfigDict


class ProfileBase(BaseModel):
    first_name: str | None 
    second_name: str | None 
    bio: str | None 
    user_id: int

class ProfileCreate(ProfileBase):
    pass 

class ProfileUpdatePartial(ProfileBase):
    pass 

class Profile(ProfileBase):
    model_config = ConfigDict(
        from_attributes=True
    )
    id: int 