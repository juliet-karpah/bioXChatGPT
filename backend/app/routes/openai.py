from fastapi import APIRouter 
from openai import OpenAI
from settings import settings


router = APIRouter(prefix="/openai")
client = OpenAI(api_key=settings.OPENAI_API_KEY)


@router.get("/")
def ask_question():
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Who won the world series in 2020?"},
    ]
    )
    return response