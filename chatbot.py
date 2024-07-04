import random
#CREATED BY KAVYA TRIVEDI
def greet():
    responses = ["Hi there!", "Hello!", "Hey! How can I help you today?"]
    return random.choice(responses)

def farewell():
    responses = ["Goodbye!", "See you later!", "Have a great day!"]
    return random.choice(responses)

def provide_info(topic):
    info = {
        "weather": "The weather is currently good if you want to know more just open the window of your room.",
        "time": "Your system has watch check it.",
        "news": "Here are the latest headlines... ",
        "age": "I'm just a bot, so I don't have an age, but if you're asking for my version, it's 2.",
        "name": "I'm ChatBot K-1.1.",
        "owner": "My owner is KAVYA TRIVEDI.",
        "contact": "You can contact Kavya Trivedi on Instagram: @kavyatrivedi.og or on github=trivedikavya"
    }
    return info.get(topic, "I'm sorry, I don't have information on that topic.")
#CREATED BY KAVYA TRIVEDI
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
            print("Bot: " + provide_info("news"))
        elif "age" in user_input:
            print("Bot: " + provide_info("age"))
        elif "name" in user_input:
            print("Bot: " + provide_info("name"))
        elif "owner" in user_input:
            print("Bot: " + provide_info("owner"))
        elif "contact" in user_input:
            print("Bot: " + provide_info("contact"))
        else:
            print("Bot: I'm just a simple chatbot. which is created by KAVYA TRIVEDI. You can ask me about me, my owner and some basic questions like weather, time, news. I don't understand too much. so you can Type 'exit' to end the conversation.")
            #CREATED BY KAVYA TRIVEDI

if __name__ == "__main__":
    chat()
