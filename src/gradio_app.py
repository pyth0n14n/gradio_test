import gradio as gr
from dotenv import load_dotenv
from chatbot_engine import chat
from langchain_community.chat_message_histories import ChatMessageHistory
import os

def respond(message, chat_history):
    history = ChatMessageHistory()
    for [user_msg, ai_msg] in chat_history:
        history.add_user_message(user_msg)
        history.add_ai_message(ai_msg)

    bot_message = chat(message, history)
    chat_history.append((message, bot_message))
    return "", chat_history


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == '__main__':
    from langchain.globals import set_verbose
    set_verbose(True)

    load_dotenv()

    app_env = os.environ.get('APP_ENV', 'production')
    print(app_env)

    if app_env == 'production':
        username = os.environ['GRADIO_USERNAME']
        password = os.environ['GRADIO_PASSWORD']
        auth = (username, password)
    else:
        auth = None

    demo.launch(auth=auth)