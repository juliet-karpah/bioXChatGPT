from fastapi import FastAPI
from app.routes import users
from motor.motor_asyncio import AsyncIOMotorClient
import settings

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
    app.mongodb = app.mongodb_client[settings.DB_NAME]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(users.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Hello World"}
