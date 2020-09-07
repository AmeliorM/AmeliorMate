import openai

class ChatBot():
    """A class to help engineer simple chatbots with GPT3"""

    def __init__(self, 
    bot="AI", 
    user="Human",
    instructions="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.",
    examples=[("Hello, who are you?", "I am an AI created by OpenAI. How can I help you today?")],
    engine="davinci",
    max_tokens=150,
    temperature=.9,
    top_p=1,
    stop=True,
    presence_penalty=0,
    frequency_penalty=0):

        self.bot = bot + ": "
        self.user = user + ": "
        self.examples = examples
        self.instructions = instructions
        self.engine = engine
        self.presence_penalty = presence_penalty,
        self.frequency_penalty = frequency_penalty
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.stop = stop

        if self.stop == True:
            self.stop = [self.user, self.bot]

        self.prompt = self.instructions + "\r\n\r\n"
        self.intro = self.instructions + "\r\n"
        
        if self.examples != None:
            self.intro = self.prompt + self.user + self.examples[0][0] + "\r\n" + self.bot + self.examples[0][1] + "\r\n\r\n"
            for i in self.examples:
                self.prompt += self.user + i[0] + "\r\n" + self.bot + i[1] + "\r\n\r\n"
        

    def set_key(self, key):
        """A method to set your OpenAI API key"""
        openai.api_key = key

    def proto_chat(self):
        """A method to create a simple chatbot in your terminal
        and interact with it so you can test your prompts."""

        print("***To QUIT, type 'QUIT' into the prompt field***\n\r")
        print(self.intro)

        while True:
            user_input = input(self.user)

            if user_input.lower() != "quit":

                combined = self.prompt + self.user + user_input + "\r\n" + self.bot

                response = openai.Completion.create(engine=self.engine, prompt=combined, 
                                                    max_tokens=self.max_tokens, temperature=self.temperature, 
                                                    top_p=self.top_p, n=1, 
                                                    stream=False, stop=self.stop)
                
                print(self.bot + response['choices'][0]["text"] + "\r\n\r\n")

            else:
                break

    def prod_chat(self, user_input, label=True):
        """A method that takes a string and outputs a GPT3 chat response"""
        if label == True:
            combined = self.prompt + self.user + user_input + "\r\n" + self.bot

            response = openai.Completion.create(engine=self.engine, prompt=combined, 
                                                max_tokens=self.max_tokens, temperature=self.temperature, 
                                                top_p=self.top_p, n=1, 
                                                stream=False, stop=self.stop)
            
            return self.bot + response['choices'][0]["text"]

        else:
            combined = self.prompt + self.user + user_input + "\r\n" + self.bot

            response = openai.Completion.create(engine=self.engine, prompt=combined, 
                                                max_tokens=self.max_tokens, temperature=self.temperature, 
                                                top_p=self.top_p, n=1, 
                                                stream=False, stop=self.stop)
            
            return response['choices'][0]["text"]