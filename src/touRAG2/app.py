import gradio as gr
from agent import agent_instance

def agent_response(message, history):
    prompt = message
    if history:
        prompt = history[-2].get("content") + "\n" + prompt

    reply = agent(prompt)
    return reply

def chat_fn():
    chat = gr.ChatInterface(fn=agent_response,type="messages")
    return chat

if __name__ == "__main__":
    agent = agent_instance()
    chat_fn().launch(share=False)
