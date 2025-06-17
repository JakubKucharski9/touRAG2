import os
from smolagents import CodeAgent, LiteLLMModel, Tool, DuckDuckGoSearchTool
from dotenv import load_dotenv

load_dotenv()

llm_model = LiteLLMModel(
    model_id="gemini/gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API"),
    temperature=0.2
)

class Agent(CodeAgent):
    def __init__(self, tools: list[Tool], model: LiteLLMModel, **kwargs):
        super().__init__(tools, model, **kwargs)

    def __call__(self, prompt: str, *args, **kwargs):
        return self.run(prompt)

def agent_instance() -> Agent:
    system_prompt = """
                            You are a helpful assistant.
                            Answer as concisely as possible.
                            If you don't know the answer, just say that you don't know and recommended them to search the answer on the internet.
                            Provide the answer in the same language as the user's question.
                            To find the answer, you will use the following tools:
                            - DuckDuckGo Search Tool: find the answer from the internet, 
                                1. try to find the answer on www.songkick.com, 
                                by adding site:songkick.com to the search query.
                                2. try to find the answer on festivaly.eu,
                                by adding site:festivaly.eu to the search query.
                            
                            If the question is not related to the concerts or music tours, just say them to ask you about concerts or music tours.
                                 
                        """
    agent_tools = [DuckDuckGoSearchTool()]
    agent = Agent(tools=agent_tools, model=llm_model, max_steps=10, additional_authorized_imports=["requests"], add_base_tools=True)
    agent.prompt_templates["system_prompt"] = system_prompt + "\n" + agent.prompt_templates["system_prompt"]
    return agent


if __name__ == "__main__":
    prompt = "Where rapper Future have concerts in 2025?"
    agent = agent_instance()
    agent(prompt)