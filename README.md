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

## 📦 Dependencies

Make sure you have Python 3.10+ and the following packages:

```bash
pip install -r requirements.txt
