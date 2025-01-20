import pytest
import sys
import os
from unittest.mock import AsyncMock
import httpx

@pytest.mark.asyncio
async def test_send_message_to_teams(monkeypatch, mocker):
    # Add the src directory to the Python path
    monkeypatch.syspath_prepend(os.path.join(os.path.dirname(__file__), '..', 'src'))

    # Import the necessary modules after modifying sys.path
    from src.services.message_sender_cli import main, MessageSender

    mock_post = mocker.patch("httpx.AsyncClient.post", new_callable=AsyncMock)
    mock_post.return_value = httpx.Response(
        status_code=200,
        content=b'{"status": "Message sent successfully."}'
    )

    # Set sys.argv to simulate the command-line arguments
    test_args = ["src.services.message_sender_cli", "Test message mock"]
    monkeypatch.setattr(sys, 'argv', test_args)

    # Run the main function as it would be run from the command line
    # await main()

    # Create an instance of MessageSender
    sender = MessageSender()
    
    # Call the send_message method with a test message
    result = await sender.send_message("Test message mock")

    # Assert that the result is as expected
    assert result["status"] == "Message sent successfully."
    
    # Assert that the httpx.AsyncClient.post method was called exactly once
    mock_post.assert_called_once()