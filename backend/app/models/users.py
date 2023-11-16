from pydantic import BaseModel, Field
import uuid
from typing import List
#one to many relationship between chats and user.
# using document references
class User(BaseModel):
    id:str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    email: str
    avatar: str


class UserCollection(BaseModel):
    users: List[User]
