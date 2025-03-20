from fastapi import APIRouter, HTTPException
from app.models.schemas import PromptSchema
from app.services.chat_service import ChatService
from app.services.session_service import SessionService
from app.utils.database import get_collection

router = APIRouter()
llm_service = ChatService()
session_service = SessionService()

@router.post("/generate")
def generate_response(prompt: PromptSchema):
    try:
        if prompt.session_id != -1:
            session_id = session_service.get_session(prompt.session_id)
        else:
            session_id = session_service.get_or_create_session(prompt.new_session)

        response = llm_service.generate_response(prompt.prompt, session_id)
        session_service.update_session(session_id, prompt.prompt, response)
        print(session_id)
        return {"response": response}
    except HTTPException as e:
        raise Exception(status_code=500, detail='Internal Server Error.') from e

@router.get("/get_session_ids")
def get_session_ids():
    try:
        return {'ids': get_collection().distinct('session_id')}
    except HTTPException as e:
        raise Exception(status_code=500, detail='Internal Server Error.') from e