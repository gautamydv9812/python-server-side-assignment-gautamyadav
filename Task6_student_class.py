class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = ""
        self.marks = 0

    def input_details(self):
        self.name = input("Enter student's name: ")
        self.roll_no = input("Enter roll number: ")
        self.marks = float(input("Enter marks: "))

    def display_details(self):
        print("\n--- Student Details ---")
        print("Name      :", self.name)
        print("Roll No   :", self.roll_no)
        print("Marks     :", self.marks)


# Creating an object of Student
student1 = Student()

# Taking input from user
student1.input_details()

# Displaying the student data
student1.display_details()
