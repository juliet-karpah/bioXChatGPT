from fastapi import APIRoute

router = APIRoute(prefix="/users")

@router.get("/", response_description="List All Users")
async def get_users():
    return ["juliet", "John"]

@router.get("/{user_id}", response_description="Get One User")
async def get_user(user_id):
    return {"user_id": user_id}

@router.get("/{user_id}/chats", response_description="Get chats for a user")
async def get_user_chats():
    return "The chats for a particular user"

@router.post("/{user_id}/chats", response_description="Create new chat")
async def create_new_chat():
    return "new chat"

@router.get("/{user_id}/chats/{chat_id}", response_description="get one chat")
async def get_one_chat():
    return "new chat"

@router.put("/{user_id}/chats/{chat_id}", response_description="Update one chat")
async def update_one_chat():
    return "update chat"

@router.delete("/{user_id}/chats/{chat_id}", response_description="Delete one chat")
async def delete_one_chat():
    return "delete chat"