
from keys import *
from openai import OpenAI

client = OpenAI(api_key = openai_api_key)

#history = [{"role": "system", "content": "You are a helpful assistant."}]

def basic_chat(user_input, chat_history, gpt_model):

    chat_history.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model=gpt_model,
        messages=chat_history
    )

    chat_history.append({"role": "assistant", "content": completion.choices[0].message.content})
    print(completion.choices[0].message.content)
    print('----------------------------------------')
    return_history = chat_history
    #print(chat_history)
    #print('----------------------------------------')
    return return_history



