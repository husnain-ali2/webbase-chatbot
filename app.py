from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

app = Flask(__name__)

# Developer information
DEVELOPER_NAME = "Husnain Ali"
DEVELOPER_COMPANY = "tecknik Nest"
CHATBOT_PERSONA = "Raja babo"

llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.0,
    max_retries=2,
)

def handle_special_questions(message):
    message = message.lower().strip()
    if any(q in message for q in ["who made you", "who created you", "who developed you", "who is your owner"]):
        return f"I was developed by {DEVELOPER_NAME} at {DEVELOPER_COMPANY} as an AI assistant."
    return None

@app.route('/')
def home():
    return render_template('chat.html',
                         bot_persona=CHATBOT_PERSONA,
                         developer_name=DEVELOPER_NAME,
                         developer_company=DEVELOPER_COMPANY)

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_message = request.form['msg']
    try:
        # Check for special questions first
        special_response = handle_special_questions(user_message)
        if special_response:
            return jsonify({
                'response': special_response,
                'persona': CHATBOT_PERSONA,
                'developer': DEVELOPER_NAME,
                'company': DEVELOPER_COMPANY
            })
            
        # Normal LLM response
        response = llm.invoke(user_message)
        return jsonify({
            'response': response.content,
            'persona': CHATBOT_PERSONA,
            'developer': DEVELOPER_NAME,
            'company': DEVELOPER_COMPANY
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
