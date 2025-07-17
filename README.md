# Webbase-Chatbot

A web-based AI chatbot using Flask, HTML, CSS, JavaScript, and the Groq API with open-source Meta AI models.

## Features
- **Flask Backend**: Lightweight Python web framework
- **Groq API Integration**: High-performance AI inference
- **Modern UI**: Clean HTML/CSS interface with interactive JavaScript
- **OpenAI-Compatible**: Works with Meta's open-source models
- **Customizable**: Easily modify responses and behavior

## Requirements
- Python 3.8+
- pip package manager
- Groq API key (free at [console.groq.com](https://console.groq.com/))

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/husnain-ali2/webbase-chatbot.git
cd webbase-chatbot
```
#### 2. Set Up Virtual Environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```
## 3. Install Dependencies
```bash
pip install -r requirements.txt
```
## 4. Configure API Key
Create .env file:
```bash
env
GROQ_API_KEY=your_api_key_here
```
##Running the Application
```bash
flask run
Then open http://localhost:5000 in your browser.
```
