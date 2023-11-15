from pydantic import BaseModel
from typing import NamedTuple, List
#one to many relation between chatunit and chat model.
# using the embedded documents because the chat units are frequently accessed with chat better performance for read operations.
class ChatUnit(NamedTuple):
    question: str
    answer: List[str]

class Chat(BaseModel):
    id: str
    user_id: str
    title: str
    chat_units: List[ChatUnit]