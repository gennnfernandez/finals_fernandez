from dbms.database import initialize_database, create_course, read_courses, update_course, delete_course

def display_courses():
    courses = read_courses()
    print(f"{'ID':<5}{'Title':<30}{'Description':<50}{'Duration':<15}{'Trainer':<30}")
    print("-" * 120)
    for course in courses:
        print(f"{course[0]:<5}{course[1]:<30}{course[2]:<50}{course[3]:<15}{course[4]:<30}")

def main_menu():
    initialize_database()
    while True:
        print("\nICT Training Course Management")
        print("1. Add a new training course")
        print("2. View all training courses")
        print("3. Update a training course")
        print("4. Delete a training course")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the course title: ")
            description = input("Enter the course description: ")
            duration = input("Enter the course duration (e.g., '2 hours', '1 day'): ")
            trainer = input("Enter the trainer's name: ")
            create_course(title, description, duration, trainer)
            print("Training course added successfully!")
        elif choice == "2":
            display_courses()
        elif choice == "3":
            course_id = int(input("Enter the course ID to update: "))
            title = input("Enter the new course title: ")
            description = input("Enter the new course description: ")
            duration = input("Enter the new course duration: ")
            trainer = input("Enter the new trainer's name: ")
            update_course(course_id, title, description, duration, trainer)
            print("Training course updated successfully!")
        elif choice == "4":
            course_id = int(input("Enter the course ID to delete: "))
            delete_course(course_id)
            print("Training course deleted successfully!")
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()  # Ensure this line is at the end to call the main menu
