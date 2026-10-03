## Encapsulation in Python OOPS

class ChatModel:
    def __init__(self, model_name, api_key):
        self.__model_name = model_name  # Private attribute
        self.__api_key = api_key        # Private attribute

    def generate_response(self, prompt):
        return f"Generating response for prompt: '{prompt}' using model: {self.__model_name}"

    def get_model_name(self):
        return self.__model_name

    def get_api_key(self):
        return self.__api_key

model = ChatModel("GPT-4", "your_api_key_here")
print(model.generate_response("What is the weather like today?"))
print("Model Name:", model.get_model_name())
print("API Key:", model.get_api_key())

## Now no one can access the private attributes directly
# print(model.__model_name)  # This will raise an AttributeError

## Now using the getter methods, we can access the private attributes

class ChatModel:
    def __init__(self, model_name, api_key):
        self.__model_name = model_name  # Private attribute
        self.__api_key = api_key        # Private attribute

    def generate_response(self, prompt):
        return f"Generating response for prompt: '{prompt}' using model: {self.__model_name}"

    # Getter for model_name
    @property
    def model_name(self):
        return self.__model_name

    # Getter for api_key
    @property
    def api_key(self):
        return self.__api_key


model2 = ChatModel("GPT-6", "your_api_key_here")
print(model2.generate_response("What is the weather like today?"))
print("Model Name:", model2.model_name)
print("API Key:", model2.api_key)
## But we can not set the private attributes directly
model2.model_name = "GPT-7"  # This will raise an AttributeError
"""

Traceback (most recent call last):
  File "E:\1_Python\mastering-python\advance\encapsulation.py", line 51, in <module>
    model2.model_name = "GPT-7"  # This will raise an AttributeError
    ^^^^^^^^^^^^^^^^^
AttributeError: property 'model_name' of 'ChatModel' object has no setter

"""
