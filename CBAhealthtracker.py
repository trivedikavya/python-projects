import os
import json
import random
from colorama import Fore, Style, init
from tabulate import tabulate

# Initialize colorama for colorful console output
init()

DATA_FILE = "health_data.json"

# Utility Functions
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# Notifications
def send_notifications(user_name, data):
    user_data = data.get(user_name, {})
    metrics = user_data.get("metrics", [])
    goals = user_data.get("goals", {})

    if metrics and goals:
        latest = metrics[-1]
        notifications = []
        if latest["steps"] < goals["steps"]:
            notifications.append("Steps below target!")
        if latest["calories"] < goals["calories"]:
            notifications.append("Calories burned below target!")
        if latest["sleep"] < goals["sleep"]:
            notifications.append("Sleep duration below target!")

        if notifications:
            print(Fore.RED + "Notifications:" + Style.RESET_ALL)
            for note in notifications:
                print("- " + note)
        else:
            print(Fore.GREEN + "Great job! You're meeting your goals!" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "Set your goals and add metrics to receive notifications." + Style.RESET_ALL)


# Health Tips
def health_tips():
    tips = [
        "Drink at least 8 glasses of water daily.",
        "Aim for 30 minutes of physical activity each day.",
        "Get 7-9 hours of sleep every night.",
        "Include more fruits and vegetables in your diet.",
        "Take regular breaks when working for long hours."
    ]
    return random.choice(tips)


# Main Menu with Authentication
def main_menu():
    data = load_data()
    clear_console()
    print(Fore.CYAN + "Welcome to the Health Tracker!" + Style.RESET_ALL)
    print("1. Login")
    print("2. Create Account")
    choice = input("Choose an option: ")

    if choice == "1":
        user_name = input("Enter your username: ")
        if user_name in data:
            print(Fore.GREEN + f"Welcome back, {user_name}!" + Style.RESET_ALL)
            user_dashboard(user_name, data)
        else:
            print(Fore.RED + "User not found. Please create an account." + Style.RESET_ALL)
    elif choice == "2":
        user_name = input("Choose a username: ")
        if user_name in data:
            print(Fore.RED + "Username already exists. Try logging in." + Style.RESET_ALL)
        else:
            print(Fore.GREEN + f"Account created for {user_name}!" + Style.RESET_ALL)
            data[user_name] = {"metrics": [], "goals": {}, "challenges": {}}
            save_data(data)
            user_dashboard(user_name, data)
    else:
        print(Fore.RED + "Invalid option. Restarting..." + Style.RESET_ALL)


# User Dashboard
def user_dashboard(user_name, data):
    while True:
        clear_console()
        print(Fore.CYAN + f"Welcome, {user_name}!" + Style.RESET_ALL)
        send_notifications(user_name, data)
        print(Fore.YELLOW + "Health Tip: " + health_tips() + Style.RESET_ALL)
        print("\nMenu:")
        print("1. Add Health Metrics")
        print("2. View Health Metrics")
        print("3. Set Goals")
        print("4. View Progress")
        print("5. Set Weekly/Monthly Challenges")
        print("6. View Leaderboard/Achievements")
        print("7. Social Sharing")
        print("8. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_health_metrics(user_name, data)
        elif choice == "2":
            view_health_metrics(user_name, data)
        elif choice == "3":
            set_goals(user_name, data)
        elif choice == "4":
            view_progress(user_name, data)
        elif choice == "5":
            set_challenges(user_name, data)
        elif choice == "6":
            view_leaderboard(data)
        elif choice == "7":
            social_sharing(user_name)
        elif choice == "8":
            print(Fore.GREEN + "Logged out successfully!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
            input("Press Enter to continue...")


# Core Features
def add_health_metrics(user_name, data):
    clear_console()
    print(Fore.CYAN + "Add Health Metrics" + Style.RESET_ALL)
    steps = int(input("Enter steps walked: "))
    calories = int(input("Enter calories burned: "))
    sleep = float(input("Enter sleep duration (hours): "))
    user_data = data[user_name]
    user_data["metrics"].append({"steps": steps, "calories": calories, "sleep": sleep})
    save_data(data)
    print(Fore.GREEN + "Metrics added successfully!" + Style.RESET_ALL)
    input("Press Enter to continue...")


def view_health_metrics(user_name, data):
    clear_console()
    print(Fore.CYAN + "View Health Metrics" + Style.RESET_ALL)
    user_data = data[user_name]
    if not user_data["metrics"]:
        print(Fore.RED + "No metrics to display." + Style.RESET_ALL)
    else:
        metrics = user_data["metrics"]
        headers = ["Entry", "Steps", "Calories Burned", "Sleep (hrs)"]
        rows = [[i + 1, m["steps"], m["calories"], m["sleep"]] for i, m in enumerate(metrics)]
        print(tabulate(rows, headers, tablefmt="grid"))
    input("Press Enter to continue...")


def set_goals(user_name, data):
    clear_console()
    print(Fore.CYAN + "Set Goals" + Style.RESET_ALL)
    steps_goal = int(input("Enter daily steps goal: "))
    calories_goal = int(input("Enter daily calories goal: "))
    sleep_goal = float(input("Enter daily sleep goal (hours): "))
    user_data = data[user_name]
    user_data["goals"] = {"steps": steps_goal, "calories": calories_goal, "sleep": sleep_goal}
    save_data(data)
    print(Fore.GREEN + "Goals set successfully!" + Style.RESET_ALL)
    input("Press Enter to continue...")



def set_challenges(user_name, data):
    clear_console()
    print(Fore.CYAN + "Set Weekly/Monthly Challenges" + Style.RESET_ALL)
    duration = input("Set challenge duration (weekly/monthly): ").lower()
    challenge = input("Enter your challenge (e.g., 'Walk 50,000 steps'): ")
    user_data = data[user_name]
    user_data["challenges"][duration] = challenge
    save_data(data)
    print(Fore.GREEN + "Challenge set successfully!" + Style.RESET_ALL)
    input("Press Enter to continue...")


def view_leaderboard(data):
    clear_console()
    print(Fore.CYAN + "Leaderboard/Achievements" + Style.RESET_ALL)
    leaderboard = sorted(data.items(), key=lambda x: len(x[1]["metrics"]), reverse=True)
    headers = ["Rank", "User", "Entries"]
    rows = [[i + 1, user, len(info["metrics"])] for i, (user, info) in enumerate(leaderboard)]
    print(tabulate(rows, headers, tablefmt="grid"))
    input("Press Enter to continue...")


def social_sharing(user_name):
    clear_console()
    print(Fore.CYAN + "Social Sharing" + Style.RESET_ALL)
    print(f"{user_name} shared their achievements on social media! 🎉")
    input("Press Enter to continue...")


# Entry Point
if __name__ == "__main__":
    main_menu()
