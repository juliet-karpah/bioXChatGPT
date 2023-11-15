from pydantic import BaseModel, Field
import uuid
from chats import Chat
from typing import List

class User(BaseModel):
    id:str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    email: str
    avatar: str
    chats: List[Chat.id]
