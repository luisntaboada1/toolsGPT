import functions

chat_history = history = [{"role": "system", "content": "You are a helpful assistant."}]

while True: 
    message = input('Input: ')
    functions.basic_chat(message, history, "gpt-3.5-turbo")
    chat_history = functions.basic_chat
    continue
