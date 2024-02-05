from functions import *
from functions import basic_chat

history = [{"role": "system", "content": "You are a helpful assistant."}]

while True: 
    message = input('Input: ')
    chat = basic_chat(message, history, "gpt-3.5-turbo")
    history = chat[0]
    completion = chat[1]

    print(f"ChatGPT: {completion}")
    print("---------------------------------------------------")
    print(f"Prompt tokens: {chat[2]}")
    print(f"Completion Tokens: {chat[3]}")
    print(f"Total tokens: {chat[4]}")
    print("----------------------------------------------------")



    continue
