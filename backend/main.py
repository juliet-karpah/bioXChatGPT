from fastapi import FastAPI
from app.routes import users

app = FastAPI()


app.include_router(users.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Hello World"}
