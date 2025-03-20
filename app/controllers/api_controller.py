from fastapi import APIRouter, HTTPException
from app.models.schemas import PromptSchema
from app.services.chat_service import ChatService
from app.services.session_service import SessionService

router = APIRouter()
llm_service = ChatService()
session_service = SessionService()

@router.post("/generate")
def generate_response(prompt: PromptSchema):
    try:
        session_id = session_service.get_or_create_session(prompt.new_session)
        response = llm_service.generate_response(prompt.prompt)
        session_service.update_session(session_id, prompt.prompt, response)
        return {"response": response}
    except HTTPException as e:
        raise Exception(status_code=500, detail='Internal Server Error.') from e