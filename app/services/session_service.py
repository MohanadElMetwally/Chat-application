import time
from app.utils.database import get_collection

class SessionService:
    def __init__(self):
        self.collection = get_collection()

    def get_or_create_session(self, new_session: bool) -> int:
        last_session = self.collection.find_one({}, sort=[("session_id", -1)])
        
        if new_session or not last_session:
            new_session_id = (last_session['session_id'] + 1) if last_session else 1
            session_doc = {
                'session_id': new_session_id,
                'started_at': time.strftime('%H:%M:%S %d-%m-%Y', time.localtime()),
                'messages': []
            }
            self.collection.insert_one(session_doc)
            return new_session_id
        return last_session['session_id']

    # returns a session specified by id
    def get_session(self, session_id):
        return self.collection.find_one({'session_id': session_id})['session_id']

    def update_session(self, session_id: int, question: str, response: str) -> None:
        update_data = {
            '$push': {
                'messages': {
                    '$each': [
                        {
                            'role': 'user',
                            'sent_at': time.strftime('%H:%M:%S %d-%m-%Y', time.localtime()),
                            'question': question
                        },
                        {
                            'role': 'assistant',
                            'responded_at': time.strftime('%H:%M:%S %d-%m-%Y', time.localtime()),
                            'answer': response[response.find('</think>') + len('</think>'):].strip()
                        }
                    ]
                }
            }
        }
        self.collection.update_one(
            {'session_id': session_id},
            update_data
        )