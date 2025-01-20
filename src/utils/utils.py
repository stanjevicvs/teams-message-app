from pydantic import BaseModel

class Message(BaseModel):
    type: str
    attachments: list

def construct_message(message_text: str) -> Message:
    return Message(
        type="message",
        attachments=[
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.2",
                    "body": [
                        {
                            "type": "TextBlock",
                            "text": message_text
                        }
                    ]
                }
            }
        ]
    )