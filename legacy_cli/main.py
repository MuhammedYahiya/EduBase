from src import User, Subject, Topic, ProgressManager
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
        
        
def register_user():
    user = User()
    user.register()

def handle_login():
    user = User()
    success = user.login()
    if success:
        user_dashboard(user.user_id)
    else:
        print("Login failed. Please try again.")

def user_dashboard(user_id):
    actions = {
        "Add Subject": lambda: add_subject(user_id),
        "View Subjects & Add topics": lambda: view_subjects(user_id),
        "Search subjects": lambda: search_subjects(user_id),
        "Sort subjects": lambda: sort_subjects(user_id),
        "Export Progress": lambda:export_progress(user_id),
        "Logout": logout_user,
    }
    while True:
        choice = inquirer.select(
            message="Select an option:",
            choices=list(actions.keys()),
            style=custom_style
        ).execute()
        actions[choice]()
        
def add_subject(user_id):
    subject = Subject(user_id=user_id)
    subject.add_subject()
        
def view_subjects(user_id):
    subject = Subject(user_id=user_id)
    subjects = subject.view_subjects()
    if not subjects:
        print("No subjects found. Please add a subject first.")
        return

        
    subject_map ={name: sub_id for sub_id, name in subjects}
    while True:
        choice = inquirer.select(
            message="Select a subject to add a topic or view topics or mark topic as completed:",
            choices=list(subject_map.keys()) + ["Dashboard"] ,
            style=custom_style,
        ).execute()


        if choice == "Dashboard":
            user_dashboard(user_id)
        
        selected_subject_id = subject_map[choice]
        subject_action_menu(selected_subject_id, user_id)

def search_subjects(user_id):
    subject = Subject(user_id=user_id)
    subjects = subject.search_subject()
    if len(subjects) > 0:
        print(f"{len(subjects)} subjects matched your search")
        for sub in subjects:
            print(sub)
            
    else:
        print("No search result found")
        return
    return

def sort_subjects(user_id):
    subject = Subject(user_id=user_id)
    choice = inquirer.select(
        message="Selected how you needed to sorted",
        choices=['A-Z','Z-A'],
        style=custom_style
    ).execute()
    
    if choice == 'A-Z':
        subjects = subject.sort_subject(choice)
        
        for sub in subjects:
            print(sub)
            
        return
    elif choice == 'Z-A':
        subjects = subject.sort_subject(choice)
        for sub in subjects:
            print(sub)
        return
            
    
def subject_action_menu(subject_id,user_id):
    action={
        "Add Topic": lambda:add_topic(subject_id),
        "Mark Topic as Completed": lambda:marked_as_completed(subject_id),
        "View Topics": lambda:view_topics(subject_id),
        "Search Topics": lambda:search_topic(subject_id),
        "Sort Topics": lambda:sort_topic(subject_id),
        "Back to Subjects": lambda:view_subjects(user_id)
    }
    while True:
        choice = inquirer.select(
            message="Choose an action for this subject:",
            choices=list(action.keys()),
            style=custom_style
        ).execute()
        
        action[choice]()
        
def add_topic(subject_id):
    topic = Topic(subject_id=subject_id)
    topic.add_topic()
        
def view_topics(subject_id):
    topic = Topic(subject_id=subject_id)
    topics = topic.view_topics()
    if topics:
        print("\nTopics:")
        for _, name, completed in topics:
            status = "✅" if completed else "❌"
            print(f" - {name} [{status}]")
    else:
        print("No topics found.")
        
    input("\nPress Enter to return to the menu...")
    
    return topics

def search_topic(subject_id):
    topic = Topic(subject_id=subject_id)
    topics = topic.search_topics()
    if len(topics) > 0:
        print(f"{len(topics)} topic matches your search:")
        for top in topics:
            status = "✅ Completed" if top["completed"] else "❌ Incomplete"
            print(f'{top["name"]}: {status}')
    else:
        print("No topic found")
        return
    return
        
def sort_topic(subject_id):
    topic = Topic(subject_id=subject_id)    
    choice = inquirer.select(
        message="select how u needed to sort",
        choices=['A-Z','Z-A','Completed','Not Completed'],
        style=custom_style
    ).execute()
    
    topics = topic.sort_topic(choice)
    for top in topics:
        status = "✅ Completed" if top["completed"] else "❌ Incomplete"
        print(f'{top["name"]}: {status}')
    
    return
        
def marked_as_completed(subject_id):
    topic = Topic(subject_id=subject_id)
    topics = topic.view_topics()
    if not topics:
        print("No topics available.")
        return
    topic_map = {name: topic_id for topic_id, name, _ in topics}
    topic_names = list(topic_map.keys()) + ["Cancel"]
    
    selected = inquirer.select(
        message="Select a topic to mark as completed:",
        choices=topic_names,
        style=custom_style
    ).execute()
    
    if selected != "Cancel":
        topic = Topic(topic_id=topic_map[selected])
        topic.marked_as_completed()
        
def export_progress(user_id):
    export = ProgressManager(user_id)
    export.export_progress()
    
    
def exit_app():
    print("Exiting EduBase. Goodbye!")
    exit()
    
def logout_user():
    print("Logging out...")
    main_menu()


if __name__ == "__main__":
    main_menu()