from fastapi import APIRouter 
from openai import OpenAI
from settings import settings


router = APIRouter(prefix="/openai")
print("ai", settings.OPENAI_API_KEY)
client = OpenAI(api_key="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")
# client = OpenAI(api_key=settings.OPENAI_API_KEY)


@router.get("/")
def ask_question():
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
    ]
    )
    return response