from pydantic import BaseModel

class PromptSchema(BaseModel):
    prompt: str
    new_session: bool = False