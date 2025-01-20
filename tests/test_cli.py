import sys
import asyncio
import pytest
import os

def test_cli_argument_parsing(monkeypatch, mocker):
    # Add the src directory to the Python path
    monkeypatch.syspath_prepend(os.path.join(os.path.dirname(__file__), '..', 'src'))

    # Import the necessary modules after modifying sys.path
    from src.services.message_sender_cli import main, MessageSender

    test_args = ["src.services.message_sender_cli", "Test message cli"]
    monkeypatch.setattr(sys, 'argv', test_args)
    
    mock_send_message = mocker.patch.object(MessageSender, 'send_message', return_value={"status": "Message sent successfully."})
    
    asyncio.run(main())
    
    mock_send_message.assert_called_once_with("Test message cli")