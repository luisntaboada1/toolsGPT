
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
    
    return_completion = completion.choices[0].message.content
    return_history = chat_history
    prompt_tokens = completion.usage.prompt_tokens
    completion_tokens = completion.usage.completion_tokens
    total_tokens = completion.usage.total_tokens
    return_list = [return_history, return_completion, prompt_tokens, completion_tokens, total_tokens]

    return return_list