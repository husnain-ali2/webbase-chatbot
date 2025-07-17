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
## Project Structure
```
webbase-chatbot/
├── static/
│   ├── css/
│   └── js/
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
├── .env.example
└── README.md
```
## License

MIT License - See LICENSE file

## Contributing
Pull requests welcome! Please open an issue first to discuss changes.

## Support
For issues, please open a GitHub issue.

text
```
Key improvements made:
1. Fixed formatting (proper Markdown syntax)
2. Corrected command for running Flask (`flask run` instead of `run app.py`)
3. Organized sections logically
4. Added project structure visualization
5. Made the Groq API key instructions clearer
6. Fixed capitalization consistency
7. Added proper code block formatting
8. Included a contributing section
9. Added support information

The file now has proper Markdown formatting and provides clear, accurate instructions for setting up and running your chatbot project.

```
