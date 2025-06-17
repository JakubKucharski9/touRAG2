import gradio as gr
from agent import agent_instance

def random_response(message, history):
    reply = agent(message)
    return reply

def chat_fn():
    chat = gr.ChatInterface(fn=random_response,type="messages")
    return chat

if __name__ == "__main__":
    agent = agent_instance()
    chat_fn().launch(share=False)
