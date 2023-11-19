# bioXChatGPT

Full stack application that:
- Allows users to get biology related answers in a chat interface
- queries new questions from chatgpt
- stores frequently asked questions in redis
- stores chat history in mongodb
- has a frontend built with reactjs
- and backend built with fastAPI

code samples
```
from pydantic import BaseModel, Field, ConfigDict
import uuid
from typing import List, Optional
#one to many relationship between chats and user.
# using document references
class User(BaseModel):
    id:Optional[str] = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    email: str
    avatar: str
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "avatar": "pic.next.cdn",
            }
        },
    )


class UserCollection(BaseModel):
    users: List[User]
```
