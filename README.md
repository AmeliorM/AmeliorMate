# AmeliorMate Python Library
This is a python library made to help with GPT3 chatbots.

### Watch a video tutorial [here](https://youtu.be/ZcE7PGsumkY)

It has one class object, ```ChatBot()```, which has three methods:

## Methods
- ```set_key()``` Takes your OpenAI credentials in the form of a string and sets them so you can access the API with this library.

- ```proto_chat()``` Takes nothing and creates a chatbot for you to interact with in your terminal or in your colab cell output space.

- ```prod_chat()``` Takes user input in the form of a string and returns your chatbot's GPT3 generated response in the form of a string. If you don't want it to include the bot label, set the optional label parameter to false ```label=False```.



## To Install:
```pip install -i https://test.pypi.org/simple/ AmeliorMate-AmeliorM==0.0.4```

You also need to have the OpenAI library installed. Your pipfile should include these at a minimum:

```
[packages]
ameliormate-ameliorm = {index = "https://test.pypi.org/simple/", version = "==0.0.4"}
openai = "*"
```

Your import statements should look like this:
```
import openai
from AmeliorMate.GPT3 import ChatBot
```

## Get started in three lines of code!
```
# Create an instance of the ChatBot class
bot = ChatBot()

# Set your OpenAI credentials
bot.set_key(YOUR_OPENAI_KEY_HERE)

#Start a test chat
bot.proto_chat()
```

The ```proto_chat()``` method will allow you to chat with your chatbot either in your colab cell output space or in your terminal. This allows you to easily and quickly test your prompt designs.

## Prompt Engineering
Engineer your prompts by changing parameters in ```ChatBot()```

For Example:
```
# Create an instance of the ChatBot class
Jane = ChatBot(bot="Jane",
               user="You",
               instructions="This is a conversation with Jane, a friendly and futuristic thinker.",
               examples=[("How different will the future be?", 
                          "Very different due to exponential growth in key areas.")],
               temperature=.95)

# Set your OpenAI credentials
Jane.set_key(YOUR_OPENAI_KEY_HERE)

#Start a test chat
Jane.proto_chat()

#When you're ready to move to production
Jane.prod_chat("Are you excited about the future?")
```

## Paramters:
- ```bot``` Takes a string and is the name of the bot you're creating. The default is ```"AI"```

- ```user``` Takes a string and is the name of the person chatting with the bot. The default is ```"Human"```

- ```instructions``` Takes a string and is the instructions for the conversation. The default is ```"The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."```

- ```examples``` Takes a list of question/answer tuples with the example question coming first and the example answer coming second. You can add as many tuples as you'd like. The default is ```[("Hello, who are you?", "I am an AI created by OpenAI. How can I help you today?")]```

- ```engine``` Takes a string and is the name of the engine you'd like to use. The default is ```"davinci"```. For a list of all possible engines, see the [OpenAI documentation](https://onboard.openai.com/docs/api-reference/create-completion?lang=python).

- ```max_tokens``` Takes an integer and is the maximum number of tokens you'd like returned. The default is ```150```

- ```temperature``` Takes a float between 0 and 1. The default is ```.9```

- ```top_p``` Takes a float between 0 and 1. The default is ```1```

- ```stop``` Takes either a string or a list of strings as stop words. The default is ```True``` which means you'd like ChatBot() to create stop words for you based on ```bot``` and ```user```.

- ```presence_penalty``` Takes a float between 0 and 1. The default is ```0```.

- ```frequency_penalty``` Takes a float between 0 and 1. The default is ```0```.

## Methods
- ```set_key()``` Takes your OpenAI credentials in the form of a string and sets them so you can access the API with this library.

- ```proto_chat()``` Takes nothing and creates a chatbot for you to interact with in your terminal or in your colab cell output space.

- ```prod_chat()``` Takes user input in the form of a string and returns your chatbot's GPT3 generated response in the form of a string. If you don't want it to include the bot label, set the optional label parameter to false ```label=False```.

## Questions, Comments, or Feedback?
Email Katie at katie@ameliormate.com