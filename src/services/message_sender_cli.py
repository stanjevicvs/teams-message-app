import asyncio
import sys
from src.routers.send_message import send_message as send_message_endpoint
from src.utils.utils import construct_message

class MessageSender:
    def __init__(self):
        pass
    
    async def send_message(self, message_text):
        message = construct_message(message_text)
        
        try:
            result = await send_message_endpoint(message)
            return result
        except Exception as e:
            print(f"Failed to send message: {e}")
            return {"status": "message sender Failed to send message"}

async def main(message_text=None):
    if message_text is None:
        if len(sys.argv) > 1:
            message_text = sys.argv[1]
        else:
            print("Welcome to the Teams Message Sender CLI!")
            message_text = input("Please enter the message text: ")
    
    sender = MessageSender()
    result = await sender.send_message(message_text)
    print(result["status"])

if __name__ == "__main__":
    asyncio.run(main())