from src import register_user, login_user, add_subject, view_subjects
from InquirerPy import inquirer, get_style

custom_style = get_style({
    "pointer": "#00ff00 bold",
    "questionmark": "#00ff00 bold",
    "selected": "#00ff00 bold",
})

def main_menu():
    actions = {
        "Register": register_user,
        "Login": handle_login,
        "Exit": exit_app,
    }
    while True:
        choice = inquirer.select(
            message="Select an option:",
            choices=list(actions.keys()),
            style=custom_style
        ).execute()
        actions[choice]()
        
        
def handle_login():
    success, user_id = login_user()
    if success:
        user_dashboard(user_id)

def user_dashboard(user_id):
    actions = {
        "Add Subject": lambda: add_subject(user_id),
        "View Subjects": lambda: view_subjects(user_id),
        "Logout": logout_user,
    }
    while True:
        choice = inquirer.select(
            message="Select an option:",
            choices=list(actions.keys()),
            style=custom_style
        ).execute()
        actions[choice]()
    
def exit_app():
    print("Exiting EduBase. Goodbye!")
    exit()
    
def logout_user():
    print("Logging out...")
    main_menu()


if __name__ == "__main__":
    main_menu()