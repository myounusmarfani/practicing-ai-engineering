## Inheritance in Python OOPS

## Using the Real World Example of Inheritance

class ChatModel:
    def __init__(self, model_name, api_key):
        self.model_name = model_name
        self.api_key = api_key

    def generate_response(self, prompt):
        return f"Generating response for prompt: '{prompt}' using model: {self.model_name}"

class Agent(ChatModel):
    def __init__(self, model_name, api_key, agent_name, tools):
        super().__init__(model_name, api_key)
        self.agent_name = agent_name
        self.tools = tools

    def introduce(self):
        return f"Hello, I am {self.agent_name}, an AI agent using the {self.model_name} model."

    def get_tools(self):
        return self.tools

agent1 = Agent("GPT-4", "your_api_key_here", "Assistant", ["Tool A", "Tool B", "Tool C"])
print(agent1.introduce())
print(agent1.generate_response("What is the weather like today?"))
print("Available tools:", agent1.get_tools())
print("Agent's model name:", agent1.model_name)
print("Agent's API key:", agent1.api_key)
print("Agent's name:", agent1.agent_name)
print("Agent's tools:", agent1.tools)
print("Agent's class:", agent1.__class__.__name__)
print("Is agent1 an instance of Agent?", isinstance(agent1, Agent))
print("Is agent1 an instance of ChatModel?", isinstance(agent1, ChatModel))