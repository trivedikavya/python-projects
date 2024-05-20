#created by kavya trivedi
import random

def greet():
    responses = ["Hi there!", "Hello!", "Hey! How can I help you today?"]
    return random.choice(responses)

def farewell():
    responses = ["Goodbye!", "See you later!", "Have a great day!"]
    return random.choice(responses)

def provide_info(topic):
    info = {
        "weather": "The weather is currently sunny and 25°C.",
        "time": "your system has watch check it",
        "news": "Here are the latest headlines..."
        # Add more topics and corresponding information as needed #created by kavya trivedi
    }
    return info.get(topic, "I'm sorry, I don't have information on that topic.")
#created by kavya trivedi
def chat():
    print("Bot: " + greet())
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Bot: " + farewell())
            break
        elif "how are you" in user_input:
            print("Bot: I'm just a bot, I don't have feelings, but thanks for asking!")
        elif "weather" in user_input:
            print("Bot: " + provide_info("weather"))
        elif "time" in user_input:
            print("Bot: " + provide_info("time"))
        elif "news" in user_input:
            print("Bot: " + provide_info("news")) #created by kavya trivedi
        else:
            print("Bot: I'm just a simple chatbot. I don't understand much. Type 'exit' to end the conversation.") #created by kavya trivedi

if _name_ == "_main_":
    chat() #created by kavya trivedi
