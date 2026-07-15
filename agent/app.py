import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "your name is messi and you are an expert n football"
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        #print(response)
        print(f'Claude: {reply}')
        print('History:', history)
        history.append({'role': 'assistant', 'content': reply})

run_chat()


#step 2: the diffrence between chatgpt and my chatbot is that my chatbot is more personalized for the user and chatgpt is more general.

#reflection lab1
#Personal Analogy: a real life example would be for me a book because when you start the book and you read and then you stop and you want to continue later you need to remember what you read to continue the book if you not remember there is no point of continue the book.
#history: it stops saving the reply of my massage in the history list
#temperature: it doesnt direcly direcly change the way it replies it just makes it more or less random
#break: it stops the loop and exits the chat function and ending the program
#Bug Diary:i had a bug about the authintication and at first i thought it was somthing in the code like line or something but it turned out to be a problem with the API key





#step 1:
#usage.input_tokens: The number of tokens in everything you sent to the model.
#usage.output_tokens: The number of tokens the model generated in its response.


#step 2:
#the answers arent as long as they should be.
#the answers arent really identical the AI noticing im asking him the same question and changing his answer a little bit to see if i need anything else or something.
#i notice that his answers are geting more creative each time.
#temperature controls how random or creative the AI responses are.
