from src import register_user, login_user
from InquirerPy import inquirer, get_style

custom_style = get_style({
    "pointer": "#00ff00 bold",
    "questionmark": "#00ff00 bold",
    "selected": "#00ff00 bold",
})

def main_menu():
    while True:
        choice = inquirer.select(
            message="Select an option:",
            choices=["Register", "Login", "Exit"],
            style=custom_style
        ).execute()
        
        if choice == "Register":
            register_user()
        elif choice == "Login":
            if login_user():
                print("Welcome to EduBase Dashboard(under construction)")
        elif choice == "Exit":
            print("Exiting EduBase.")
            break


if __name__ == "__main__":
    main_menu()