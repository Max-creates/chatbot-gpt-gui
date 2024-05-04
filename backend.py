import openai

class Chatbot:
    def __init__(self):
        openai.api_key = "paste your api key here"
        
    def get_response(self, user_input):
        # response = openai.Completion.create(
        #     engine="text-davinci-003",
        #     prompt=user_input,
        #     max_tokens=3000,
        #     temperature=0.5,
        # ).choices[0].text
        response = "Unable to find a free engine... maximum I can do is repeat your prompt: " \
                   + user_input + ("\nIf you get an engine just replace it in "
                                   "file backend.py in get_response function engine='your engine name'")
        return response
    
if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)
        
