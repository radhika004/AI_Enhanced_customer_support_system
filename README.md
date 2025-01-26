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
   Here's everything in markdown syntax for the README:

```markdown
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
   ```
   This will start the FastAPI application on `http://127.0.0.1:8000`.

## Endpoints

### POST /save-issue

**Description**: Processes incoming issues, determines sentiment and priority, and generates a response using the Groq API. Sends the result to a Zapier webhook.

**Request Body**:
```json
{
  "subject": "Issue Subject",
  "body": "The issue description or body"
}
```

**Response**:
- **Success**: Returns the processed issue with sentiment, priority, and generated response.
- **Error**: Returns an error message if the issue could not be processed.

**Example**:
```json
{
  "message": "Issue processed and sent to Zapier successfully.",
  "result": {
    "subject": "System outage",
    "priority": "VERY_HIGH",
    "sentiment": "negative",
    "response": "We apologize for the inconvenience. Our team is working on resolving the issue."
  }
}
```

## Functions

- **get_sentiment(issue_body)**: Uses the Groq API to determine the sentiment of the issue body (Positive, Negative, Neutral, Frustrated).
- **determine_priority(subject, body)**: Determines the priority based on specific keywords.
- **get_groq_response(issue_body)**: Generates a customer support response using the Groq API.
- **process_incoming_issue(incoming_issue)**: Processes the incoming issue by determining its priority, sentiment, and generating a response.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This is the full README in GitHub-flavored markdown. You can copy and paste it into your `README.md` file for your repository.
