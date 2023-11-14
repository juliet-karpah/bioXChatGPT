from fastapi import APIRoute

router = APIRoute(prefix="/users")

@router.get("/")
async def get_users():
    return ["juliet", "John"]

@router.get("/{user_id}")
async def get_user(user_id):
    return {"user_id": user_id}

@router.get("/{user_id}/chats")
async def get_user_chats():
    return "The chats for a particular user"

@router.post("/{user_id}/chats")
async def create_new_chat():
    return "new chat"

@router.get("/{user_id}/chats/{chat_id}")
async def get_one_chat():
    return "new chat"

@router.put("/{user_id}/chats/{chat_id}")
async def update_one_chat():
    return "new chat"

@router.delete("/{user_id}/chats/{chat_id}")
async def delete_one_chat():
    return "new chat"