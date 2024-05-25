from langchain_openai import ChatOpenAI
import langchain
from langchain_community.chat_message_histories import ChatMessageHistory
# from langchain_core.runnables.history import RunnableWithMessageHistory

def chat(message: str, history: ChatMessageHistory) -> str:
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    
    history.add_user_message(message)

    print(history.messages)
    return llm.invoke(history.messages).content
