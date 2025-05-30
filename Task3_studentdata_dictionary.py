# Empty dictionary to store student records
students = {}

# Function to add a student
def add_student():
    roll = input("\tEnter Your Roll Number: ")
    if roll in students:
        print("Student with this roll number already exists.")
    else:
        name = input("\tEnter Name: ")
        marks = int(input("\tEnter Marks: "))
        contact = input("\tEnter Contact Number: ")
        students[roll] = {
            "Name": name,
            "Marks": marks,
            "Contact": contact
        }
        print("Student added successfully.")

# Function to search a student by roll number
def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        std = students[roll]
        print("\n--- Student Found ---")
        print("{:15}{:<15}{:<15}{:<15}".format("Roll", "Name", "Mark", "Contact"))
        print("-" * 60)
        for roll, std in students.items():
            print("{:15}{:<15}{:<15}{:<15}".format(roll, std['Name'], std['Marks'], std['Contact']))

    else:
        print("Student not found.")

# Function to display all students
def display_students():
    if not students:
        print("\tNo student records to display.")
        return
    print("\n--- Student Records ---")
    print("{:15}{:<15}{:<15}{:<15}".format("Roll", "Name", "Mark", "Contact"))
    print("-" * 60)
    for roll, std in students.items():
        print("{:15}{:<15}{:<15}{:<15}".format(roll, std['Name'], std['Marks'], std['Contact']))

# Main menu loop
while True:
    print("\n===== Student Record Menu =====")
    print("1. Add Student")
    print("2. Search Student by Roll Number")
    print("3. Display All Students")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_student()
        input("\nPress Enter to return to the menu...")
    elif choice == '2':
        search_student()
        input("\nPress Enter to return to the menu...")
    elif choice == '3':
        display_students()
        input("\nPress Enter to return to the menu...")
    elif choice == '4':
        print("Exit program")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")