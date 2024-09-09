# 🤖 Customer Review Processing Bot

This project is a **Customer Review Processing Bot** built using LangChain, designed to automate the analysis and response to customer reviews. The bot processes reviews written in various languages and outputs essential insights such as sentiment analysis, a summary of the review, the original language of the review, and generates an email response based on the sentiment.

## Project Diagram

![diagram](https://github.com/aadhil96/Customer-Review-Processing-Bot-/blob/9107e690f1a01f251ed30854472f4a2733407d63/diagram.png)

## ✨ Features

1. 🌍 **Multilingual Review Translation**: The bot detects and translates non-English reviews into English.
2. 📝 **Review Summary Generation**: A concise summary of each review is created.
3. 🗣️ **Language Detection**: The original language of the review is identified.
4. 🎯 **Sentiment Analysis**: The sentiment of the review (positive, neutral, or negative) is determined.
5. 💌 **Automated Email Response**: Based on the sentiment, a professional email response is generated for the customer.

## 🗂️ Project Structure

- **LangChain Chains**:
  - Sequential chains for processing the review through various stages.
  
- **Prompts**:
  - Different prompts are used to handle translation, summarization, sentiment analysis, language detection, and email response generation.

## How It Works 🛠️
The bot processes reviews in several steps using Langchain components:

1. **Translate Review** 🌐:  
   If the review is not in English, it is translated. If it’s already in English, it is passed as is.

2. **Create Summary** 📝:  
   Summarizes the main points of the customer’s feedback in a few sentences.

3. **Identify Original Language** 🌍:  
   Detects the language in which the review was originally written.

4. **Determine Sentiment** 😃:  
   Analyzes the sentiment of the review based on all inputs (positive, neutral, or negative).

5. **Generate Email Response** 💬:  
   Using the sentiment and feedback, the bot creates a professional, specific email response. The email will thank the customer for positive/neutral feedback, or apologize and offer assistance if the sentiment is negative.

## Prerequisites 📋
- Python 3.x
- Environment variables for API keys if using an external LLM.

## Installation 🔧
Install the required Python packages with the following commands:

```bash
!pip install langchain
!pip install langchain_community
!pip install langchain_openai
