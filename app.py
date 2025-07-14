from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

app = Flask(__name__)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.0,
    max_retries=2,
)

@app.route('/')
def home():
    return render_template('chat.html')  # Make sure your template is named chat.html

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_message = request.form['msg']
    response = llm.invoke(user_message)
    bot_response = response.content
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)