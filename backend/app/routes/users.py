from fastapi import APIRouter, Body, Request, HTTPException, status
# from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
# from app.models.users import UserCollection, User

router = APIRouter(prefix="/users")


@router.get("/", response_description="List All Users")
async def get_users(request: Request):
    """
    Get a List of all the Users
    """
    users = []
    query = await request.app.mongodb["users"].find().to_list(length=100)
    print(query, "query")
    for doc in jsonable_encoder(query):
        users.append(doc)
    return users


# @router.post("/", response_description="Create New User", status_code=status.HTTP_201_CREATED)
# async def create_user(request:Request, user: User = Body(...)):
#     """
#     Insert new user document to User Collection
#     """
#     user_encoded = jsonable_encoder(user)
#     new_user = request.app.mongodb['users'].insert_one(user_encoded)
#     return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_task)


# @router.get("/{user_id}", response_description="Get One User", response_model=User)
# async def get_user(user_id, request: Request):
#     if (user:= await request.app.mongodb['users'].find_one({'_id': user_id})):
#         return user
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with{user_id} not found")

# @router.get("/{user_id}/chats", response_description="Get chats for a user")
# async def get_user_chats():
#     return "The chats for a particular user"

# @router.post("/{user_id}/chats", response_description="Create new chat")
# async def create_new_chat():
#     return "new chat"

# @router.get("/{user_id}/chats/{chat_id}", response_description="get one chat")
# async def get_one_chat():
#     return "new chat"

# @router.put("/{user_id}/chats/{chat_id}", response_description="Update one chat")
# async def update_one_chat():
#     return "update chat"

# @router.delete("/{user_id}/chats/{chat_id}", response_description="Delete one chat")
# async def delete_one_chat():
#     return "delete chat"
