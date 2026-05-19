from pydantic import BaseModel

# -----------------------------------
# Chat Request Model
# -----------------------------------

class ChatRequest(BaseModel):

    message: str