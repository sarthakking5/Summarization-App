# 🧠 LangChain Summarization App

A simple and powerful Streamlit app that summarizes YouTube videos or any web article using **LangChain**, **Groq's Gemma model**, and **YouTube Transcript API**. Just paste a link, and get a 300-word summary instantly.

---

## 🚀 Features

- 🔗 Accepts both **YouTube URLs** and **webpage links**
- 🤖 Uses **LangChain + Groq's Gemma2-9b-It** model for summarization
- 📹 Fetches transcripts from YouTube using the latest `youtube-transcript-api`
- 📰 Loads content from websites using `UnstructuredURLLoader`
- ⚡ Clean and simple **Streamlit UI**

---

## 📷 Demo

![App Screenshot](https://github.com/sarthakking5/Summarization-App/blob/main/images/Screenshot%202025-07-22%20104619.png)

---
## 📦 Typical Dependencies

Make sure the following Python packages are installed:

- `streamlit`
- `langchain`
- `langchain-community`
- `langchain-groq`
- `youtube-transcript-api`
- `validators`
- `python-dotenv`
- `unstructured`

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```
## 🧠 How It Works

You input a **YouTube video URL** or **article URL**.

The app then:

- Fetches the transcript using `youtube-transcript-api` (for YouTube)
- Scrapes and parses the page using `UnstructuredURLLoader` (for websites)
- Combines content into a single document
- Sends it to LangChain using **Groq's Gemma2-9b-It** for summarization
- Displays a concise summary of about 300 words

---

## 🛠️ Usage

```bash
# Activate your virtual environment (if not already)
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Run the app
streamlit run app.py

## 📁 Project Structure
```text
📦summarization-app/
 ┣ 📄app.py              # Main Streamlit application
 ┣ 📄test.py             # Transcript fetch testing script
 ┣ 📄.env                # Your Groq API key (excluded from Git)
 ┣ 📄.gitignore          # Git ignored files (e.g., venv, __pycache__)
 ┗ 📄requirements.txt    # Python dependencies
```
## 🧪 Test a YouTube Video

python test.py

Use any valid video ID with captions.

## 🙋 FAQ

Q: What if a YouTube video has no transcript?
A: The app will show a warning. Try a different video that has captions (auto or manual).

Q: Can I use models other than Gemma?
A: Yes! Modify the ChatGroq model name to one supported by Groq, like llama3-8b.

