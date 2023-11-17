from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.models.users import UserCollection, User
from bson import ObjectId

router = APIRouter(prefix="/users")


@router.get("/", response_description="List All Users")
async def get_users(request: Request):
    """
    Get a List of all the Users
    """
    users = []
    query = await request.app.mongodb["users"].find().to_list(length=100)
    for doc in query:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        users.append(doc)
    return users

# fake_user: User = {
#     "name": "Almat",
#     "email": "almat@gmail.com",
#     "avatar":"https://i0.wp.com/picjumbo.com/wp-content/uploads/woman-enjoying-the-sunset-by-the-sea-free-photo.jpg?w=600&quality=80"
# }

@router.post(
    "/", response_description="Create New User", status_code=status.HTTP_201_CREATED
)
async def create_user(request: Request, user: User = Body(...)):
    """
    Insert new user document to User Collection
    """
    user_encoded = jsonable_encoder(user)
    new_user = await request.app.mongodb["users"].insert_one(user_encoded)
    print(new_user.inserted_id, "print")
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=new_user.inserted_id)


@router.get("/{user_id}", response_description="Get One User")
async def get_user(user_id: str, request: Request):
    """
    Get the record for a specific user with the id
    """
    if user := await request.app.mongodb["users"].find_one({"_id": ObjectId(user_id)}):
        del user["_id"]
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"User with{user_id} not found"
    )

@router.delete("/{user_id}")
async def delete_one_user(user_id: str, request: Request):
    res = await request.app.mongodb['users'].delete_one({'_id': user_id})
    if res.deleted_count == 1:
        JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    else:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with {user_id} not found")


@router.get("/{user_id}/chats", response_description="Get chats for a user")
async def get_user_chats(user_id: str, request: Request):
    chats = []
    query = (
        await request.app.mongodb["chats"]
        .find({"user._id": ObjectId(user_id)})
        .to_list(100)
    )
    print(query, "query")
    for doc in query:
        del doc["_id"]
        del doc["user"]["_id"]
        chats.append(doc)
    return chats


@router.post("/{user_id}/chats", response_description="Create new chat")
async def create_new_chat():

    return "new chat"


@router.get("/{user_id}/chats/{chat_id}", response_description="get one chat")
async def get_one_chat(request: Request, chat_id):
    """
    Return a record of chats
    """
    if chat := await request.app.mongodb["chats"].find_one({"_id": ObjectId(chat_id)}):
        del chat["_id"]
        del chat["user"]["_id"]
        return chat
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"chat with{chat_id} not found"
    )


@router.put("/{user_id}/chats/{chat_id}", response_description="Update one chat")
async def update_one_chat():
    return "update chat"


@router.delete("/{user_id}/chats/{chat_id}", response_description="Delete one chat")
async def delete_one_chat(chat_id:str, request:Request):
    res = await request.app.mongodb['chats'].delete_one({'_id': chat_id})
    if res.deleted_count == 1:
        JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    else:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chat with {chat_id} not found")

