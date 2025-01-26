

import os
import requests
from groq import Groq
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize Groq client for response generation
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

# Function to get sentiment from Groq API
def get_sentiment(issue_body):
    """
    Analyze the sentiment of the given issue body using the Groq API.
    """
    try:
        messages = [
            {
                "role": "system",
                "content": """
                You are the customer support team assistant responsible for sentiment analysis.
                Analyze the sentiment of the given text and categorize it as one of the following:
                - Positive
                - Negative
                - Neutral
                - Frustrated
                """
            },
            {
                "role": "user",
                "content": issue_body
            }
        ]

        # API call to Groq for sentiment analysis
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages,
            temperature=0,
            max_completion_tokens=10,
            top_p=1,
            stream=False
        )

        sentiment_raw = completion.choices[0].message.content.strip()

        valid_sentiments = ['positive', 'negative', 'neutral', 'frustrated']
        sentiment = sentiment_raw.lower()

        return sentiment if sentiment in valid_sentiments else "neutral"

    except Exception as e:
        print(f"Error during sentiment analysis: {e}")
        return "error"

# Function to determine priority
def determine_priority(subject, body):
    """
    Determine the priority of the incoming issue based on keywords.
    """
    combined_text = subject + " " + body

    very_high_keywords = [
        "Disruption", "Failure", "Outage", "Critical", "Emergency"
    ]
    for key in very_high_keywords:
        if key.lower() in combined_text.lower():
            return "VERY_HIGH"

    high_keywords = ["Delay", "Lag", "Issue", "Bug"]
    for key in high_keywords:
        if key.lower() in combined_text.lower():
            return "HIGH"

    return "LOW"

# Function to generate a response using the Groq API
def get_groq_response(issue_body):
    """
    Generate a customer support response using the Groq API.
    """
    try:
        messages = [
            {
                "role": "system",
                "content": "Generate a polite and empathetic response for the user."
            },
            {
                "role": "user",
                "content": issue_body
            }
        ]

        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages,
            temperature=0.7,
            max_completion_tokens=100,
            top_p=1,
            stream=False
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        print(f"Error during Groq response generation: {e}")
        return "Unable to generate a response currently."

# Function to process incoming issues
def process_incoming_issue(incoming_issue):
    priority = determine_priority(incoming_issue["subject"], incoming_issue["body"])
    sentiment = get_sentiment(incoming_issue["body"])
    response = get_groq_response(incoming_issue["body"])

    return {
        "subject": incoming_issue["subject"],
        "priority": priority,
        "sentiment": sentiment,
        "response": response
    }

# FastAPI part to expose /save-issue endpoint
app = FastAPI()

class IncomingIssue(BaseModel):
    subject: str
    body: str

@app.post("/save-issue")
async def save_issue(incoming_issue: IncomingIssue):
    try:
        result = process_incoming_issue(incoming_issue.model_dump())

        # Replace with your Zapier Webhook URL
        webhook_url = "https://hooks.zapier.com/hooks/catch/21371791/2f3clcp/"
        zapier_response = requests.post(webhook_url, json=result)

        if zapier_response.status_code == 200:
            return {"message": "Issue processed and sent to Zapier successfully.", "result": result}
        else:
            raise HTTPException(status_code=zapier_response.status_code, detail="Failed to send data to Zapier")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the incoming issue: {e}")
