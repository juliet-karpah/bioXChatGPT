from pydantic import BaseModel
from typing import NamedTuple, List

class ChatUnit(NamedTuple):
    question: str
    answer: List[str]

class Chat(BaseModel):
    user_id: str
    title: str
    sections: List[ChatUnit]