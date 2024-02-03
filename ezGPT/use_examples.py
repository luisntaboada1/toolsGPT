from functions import *
from functions import basic_chat

history = [{"role": "system", "content": "You are a helpful assistant."}]

while True: 
    message = input('Input: ')
    chat = basic_chat(message, history, "gpt-3.5-turbo")
    history = chat[0]
    completion = chat[1]

    print(completion)
    print("---------------------------------------------------")
    print(history)
    print("---------------------------------------------------")
    print(chat)


    continue
