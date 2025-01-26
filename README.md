# AI_Enhanced_customer_support_system

# Customer Support Issue Processing System

This project uses the Groq API for sentiment analysis and response generation, combined with FastAPI to expose an endpoint for processing incoming issues. The system determines the sentiment and priority of the incoming issues and generates a response. It then sends the processed issue data to a Zapier webhook for further automation.

## Features
- **Sentiment Analysis**: Analyzes the sentiment of the issue body (Positive, Negative, Neutral, Frustrated).
- **Priority Determination**: Assigns priority to the issue based on specific keywords.
- **Response Generation**: Uses the Groq API to generate a polite and empathetic customer support response.
- **Integration**: Sends processed data to a Zapier webhook for automation.

## Requirements
- Python 3.7+
- Install the required dependencies via `pip`:

    ```bash
    pip install fastapi requests groq pydantic uvicorn
    ```

## Setup

1. **Groq API Key**: Replace `GROQ_API_KEY` with your Groq API key. You can obtain it by signing up for Groq’s API service.

2. **Zapier Webhook URL**: Replace the placeholder webhook URL in the `save_issue` endpoint with your own Zapier webhook URL.

3. **Running the Application**:
   - Start the FastAPI server with Uvicorn:
   
   ```bash
   uvicorn main:app --reload
