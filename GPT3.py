
import openai


class ChatBot():
    """A class to help engineer simple chatbots with GPT3"""

  def __init__(self, engine="davinci", 
               presence_penalty=0,
               frequency_penalty=0,
               instructions="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.",
               max_tokens=50, 
               temperature=.9, 
               top_p=1, 
               stream=False, 
               stop=True, 
               examples=[("Hello, who are you?", "I am an AI created by OpenAI. How can I help you today?")], 
               bot="AI", 
               user="Human", 
               prompt=None):

    self.bot = bot + ": "
    self.user = user + ": "
    self.engine = engine
    self.presence_penalty = presence_penalty,
    self.frequency_penalty = frequency_penalty
    self.prompt = prompt
    self.max_tokens = max_tokens
    self.temperature = temperature
    self.top_p = top_p
    self.n = 1
    self.stream = stream
    self.stop = stop
    if self.stop == True:
      self.stop = [self.user, self.bot]
    self.examples = examples
    self.instructions = instructions
    if self.prompt == None:
      self.prompt = self.instructions + "\r\n\r\n"
    self. intro = self.instructions + "\r\n"
    
    if self.examples != None:
      self.intro = self.prompt + self.user + self.examples[0][0] + "\r\n" + self.bot + self.examples[0][1] + "\r\n\r\n"
      for i in self.examples:
        self.prompt += self.user + i[0] + "\r\n" + self.bot + i[1] + "\r\n\r\n"
 

  def proto_chat(self):
      """A method to create a simple chatbot in your terminal
      and interact with it so you can test your prompts."""

    print("***To QUIT, type 'QUIT' into the prompt field***\n\r")
    print(self.intro)

    while True:
      user_input = input(self.user)

      if user_input != "QUIT".lower():

        combined = self.prompt + self.user + user_input + "\r\n" + self.bot

        response = openai.Completion.create(engine=self.engine, prompt=combined, 
                                            max_tokens=self.max_tokens, temperature=self.temperature, 
                                            top_p=self.top_p, n=self.n, 
                                            stream=self.stream, stop=self.stop)
          
        print(self.bot + response['choices'][0]["text"] + "\r\n\r\n")

      else:
        break

