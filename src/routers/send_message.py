from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import httpx
from dotenv import load_dotenv
from src.utils.utils import Message

# Load environment variables from .env file
load_dotenv()

router = APIRouter()

# Load the webhook URL once at the module level
WEBHOOK_URL = os.getenv("TEAMS_WEBHOOK_URL")
print(f"Loaded Webhook URL: {WEBHOOK_URL}") 

@router.post("/sendMessage")
async def send_message(message: Message):
    if not WEBHOOK_URL:
        raise HTTPException(status_code=500, detail="Webhook URL not configured.")
    
    headers = {
        "Content-Type": "application/json"
    }
    
    # Check if the message is empty and prompt for user input if necessary
    if not message.attachments or not message.attachments[0].get('content', {}).get('body', []):
        raise HTTPException(status_code=400, detail="Message content is empty.")
    
    async with httpx.AsyncClient() as client:
        response = await client.post(WEBHOOK_URL, json=message.model_dump(), headers=headers)
    
    if response.status_code != 200 and response.status_code != 202:
        raise HTTPException(status_code=response.status_code, detail=f"Failed to send message: {response.text}")
    
    return {"status": "Message sent successfully."}