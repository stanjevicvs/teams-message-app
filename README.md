# Teams Message App

This project is a Python application that sends messages to a Microsoft Teams channel using a webhook URL. The application is built using FastAPI and provides a REST API for sending messages.

## Project Structure

```
teams-message-app 
├── src 
│   ├── main.py                           # Entry point of the application 
│   ├── routers 
│   │   └── send_message.py               # Defines the /sendMessage POST endpoint 
│   ├── services 
│   │   └── message_sender_cli.py         # CLI for sending messages 
│   └── utils 
│   |   └── utils.py                      # Utility functions for sending messages 
├── static
|   ├── index.html                        # Static HTML file
├── tests                                 # Tests
|   ├── test_api.py                       # Tests for API endpoints
|   ├── test_cli.py                       # Tests for CLI argument parsing
|   ├── test_teams_posting.py             # Tests for Teams posting (mocked)
├── docker-compose.yml                    # Docker Compose configuration
├── dockerfile                            # Docker configuration
├── .dockerignore                         # Docker ignore file
├── requirements.txt                      # Project dependencies 
├── .env                                  # Environment variables (webhook URL) 
├── README.md                             # Project documentation
└── pytest.ini                            # pytest configuration

```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd teams-message-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Set up the environment variables:**
   Create a `.env` file in the root directory and add your Microsoft Teams webhook URL:
   ```
   TEAMS_WEBHOOK_URL=<your_webhook_url>
   ```

## Running instructions

### Running the FastAPI Application

1. **Start the FastAPI application:**
   ```
   uvicorn src.main:app --reload
   ```

2. **Access the application**
Open your web browser and navigate to `http://127.0.0.1:8000`.

### Run the CLI script

1. **Run the CLI script**
   ```
   python -m src.services.message_sender_cli
   ```

2. **Follow the prompts**
Enter the message text and press Enter to send the message.

### Running with Docker

1. **Build the Docker image**
   ```
   docker-compose build
   ```

2. **Run the Docker container**
   ```
   docker-compose up
   ```
  
3. **Access the application**

Open your web browser and navigate to http://127.0.0.1:8000.

## Message Input Methods

### POST /sendMessage

This endpoint accepts a JSON payload to send a message to the Microsoft Teams channel.

#### Request Body

```json
{
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
            "text": "Your message here"
          }
        ]
      }
    }
  ]
}
```

#### Example

```bash
curl -X POST "http://127.0.0.1:8000/sendMessage" -H "Content-Type: application/json" -d '{
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
            "text": "Hello, Teams!"
          }
        ]
      }
    }
  ]
}'
```

### Using the CLI

You can send a message interactively by running the message_sender_cli.py script and following the prompts.

   ```
   python -m src.services.message_sender_cli
   ```

## Environment Variable Configuration
The application requires a Microsoft Teams webhook URL to send messages. This URL should be stored in an .env file in the root directory of the project.

   ```
  TEAMS_WEBHOOK_URL=<your-teams-webhook-url>
   ```

By following these instructions, you can set up, run, and use the Teams Message App to send messages to a Microsoft Teams channel using both the FastAPI endpoint and the CLI.
