# 🌟 AI-Enhanced Customer Support System 🌟

Welcome to the Customer Support Issue Processing System! 🚀 This project uses the Groq API for cutting-edge sentiment analysis and response generation, combined with FastAPI to efficiently process incoming customer issues. It determines the sentiment and priority of the issues, generates a thoughtful response, and sends the processed data to a Zapier webhook for seamless automation. ✨

---

## 🔥 Features
- 🧠 Sentiment Analysis: Understands the issue's sentiment — Positive, Negative, Neutral, or Frustrated.  
- 🏷️ Priority Determination: Automatically assigns priorities (LOW, MEDIUM, HIGH, VERY_HIGH) based on keywords.  
- 💬 Response Generation: Crafts polite and empathetic responses using the **Groq API**.  
- 🔗 Integration: Effortlessly sends processed data to a Zapier webhook for further actions.  

---

## 🛠️ Requirements
- 🐍 Python 3.7+
- 📦 Install the required dependencies with `pip`:  
  ```bash
  pip install fastapi requests groq pydantic uvicorn
---
##⚙️ Setup
-1️⃣ Configure API Key 🔑
Replace GROQ_API_KEY in your code with your Groq API key. Obtain it by signing up at Groq’s website.

##2️⃣ Zapier Webhook URL 🌐
-Replace the placeholder Zapier webhook URL in the save_issue endpoint with your own.

##3️⃣ Run the Application 🚀
-Start the FastAPI server with Uvicorn:
---
##🔗 API Endpoints
-📌 POST /save-issue
Description: Processes incoming issues, analyzes sentiment, assigns priority, and generates a response. Sends the processed data to a Zapier webhook.


