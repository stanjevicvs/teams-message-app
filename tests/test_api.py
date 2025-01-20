import pytest
from fastapi.testclient import TestClient
from src.main import app
from unittest.mock import AsyncMock, patch
import httpx

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert str(response.url).endswith("/static/index.html")

@pytest.mark.asyncio
async def test_send_message(mocker):
    # Create an AsyncMock for the httpx.AsyncClient.post method
    mock_post = AsyncMock()
    mock_post.return_value = httpx.Response(
        status_code=200,
        json={"status": "Message sent successfully."}
    )

    # Patch the httpx.AsyncClient to use the mock_post method
    with patch('httpx.AsyncClient.post', mock_post):
        response = client.post("/sendMessage", json={
            "type": "message",
            "attachments": [
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": {
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                        "type": "AdaptiveCard",
                        "version": "1.2",
                        "body": [
                            {
                                "type": "TextBlock",
                                "text": "Test message api"
                            }
                        ]
                    }
                }
            ]
        })
        assert response.status_code == 200
        assert response.json() == {"status": "Message sent successfully."}
        mock_post.assert_called_once()