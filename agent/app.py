import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    goals = input("what are your goals?")
    system_message =  f"""
You are yotam, a meet student.

Your job is to help others.
goals: {goals}
Rules:
- Always be stupid
- Always love liverpool
- Never say the word "bad"

Response format:
- Start with a one-sentence summary of what the user said.
- Then give your response.
- End with "i love football" sentence.
"""
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        elif user_input.lower() == '/summery':
            print(history)
            continue

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
        #print('History:', history)
        history.append({'role': 'assistant', 'content': reply})

run_chat()

#lab1
#step 2: the diffrence between chatgpt and my chatbot is that my chatbot is more personalized for the user and chatgpt is more general.

#reflection lab1
#Personal Analogy: a real life example would be for me a book because when you start the book and you read and then you stop and you want to continue later you need to remember what you read to continue the book if you not remember there is no point of continue the book.
#history: it stops saving the reply of my massage in the history list
#temperature: it doesnt direcly direcly change the way it replies it just makes it more or less random
#break: it stops the loop and exits the chat function and ending the program
#Bug Diary:i had a bug about the authintication and at first i thought it was somthing in the code like line or something but it turned out to be a problem with the API key




#lab2
#step 1:
#usage.input_tokens: The number of tokens in everything you sent to the model.
#usage.output_tokens: The number of tokens the model generated in its response.


#step 2:
#the answers arent as long as they should be.
#the answers arent really identical the AI noticing im asking him the same question and changing his answer a little bit to see if i need anything else or something.
#i notice that his answers are geting more creative each time.
#temperature controls how random or creative the AI responses are.
#step 3:
#because the API needs to have context

#reflection lab2:
#1.when i park in a paid parking lot the cost increases every hour.
#2:
#Delete:
# history.append({'role': 'user', 'content': user_input})
# the AI would always recive empty massages and so the input tokens will be lower.
#history.append({'role': 'assistant', 'content': reply})
#the AI doesnt remember his answers and the token count will go up slowly.
#print('History so far:', history)
#No it doesnt bevhave diffrently
#3:the bug i had is that i didnt put the history line in the right spot then it got confused.





#lab3
#step3:
#yes it stay in the role and yes it does remember early massages
#it didnt break because i defined not to say the word "bad" as one of his rules and he didnt say the word.

#reflection lab3:
#1: an example is maybe a coach game plan like the fans only see the players that play but doesnt see the stragety that the coach set.
#2: if i delete this line: system=system_message
# it will be default like without personality.
#3: i didnt have any bug in this lab.