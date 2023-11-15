from pydantic import BaseModel
from typing import NamedTuple, List

class ChatUnit(NamedTuple):
    id: str
    question: str
    answer: List[str]

class Chat(BaseModel):
    id: str
    user_id: str
    title: str
    chatUnits: List[ChatUnit.id]