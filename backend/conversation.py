    

from urllib import request
from uuid import uuid4

def get_conversation_history(request):  
    try:
        conversation_id = (
            request.conversation_id
            or str(uuid4())
        )
    except Exception as e:
        print("Error generating conversation ID:", e)
