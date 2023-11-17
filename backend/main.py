from fastapi import FastAPI
from app.routes import users
from app.routes import openai as openai_router
import motor.motor_asyncio as client
from settings import settings

app = FastAPI(title="BioXChat API")

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = client.AsyncIOMotorClient(settings.DB_URL)
    app.mongodb = app.mongodb_client[settings.DB_NAME[0]]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(users.router, tags=["users"], prefix="/api/v1")
app.include_router(openai_router.router, tags=["openai"], prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Hello World"}
