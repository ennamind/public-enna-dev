import os
from app import run
from flask import Flask, render_template, request
from app.assets import prompt_functions

app = Flask(__name__)

# initialize an empty list to store the conversation history
conversation_history = []

@app.route('/', methods=['GET', 'POST'])
def conversation():
    global conversation_history
    
    # initiate the openAI api and make the first prompt, and display the response
    if len(conversation_history) == 0:
        welcome_message = prompt_functions.get_openai_response("start with a welcome message", conversation_history)
        conversation_history.append({
            'chatbotOutput': welcome_message,
            'userInput': '-this is first welcome message-',
            'datetime': ''
        })
    
    if request.method == 'POST':
        # get the user input from the form
        text_input_from_user = request.form['user_input']
        
        # add the user input to the conversation history
        conversation_history.append({
            'chatbotOutput': '-this is user input-',
            'userInput': text_input_from_user,
            'datetime': ''
        })
        
        # get the chatbot response using the user input
        chatbot_response = prompt_functions.get_openai_response(text_input_from_user, conversation_history)
        
        # add the chatbot response to the conversation history
        conversation_history.append({
            'chatbotOutput': chatbot_response,
            'userInput': '-this is response from user input-',
            'datetime': ''
        })
 
    return render_template('input_form.html', conversation_history=conversation_history)

if __name__ == '__main__':
    # clear the conversation history when the Flask app is compiled
    conversation_history = []
    
    app.run(debug=True)
