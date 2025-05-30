#create a program that take a list of student names and store them in a file . Then read the file and display the content

# Take number of students
num = int(input("Enter number of students: "))

# Take student names and store in a list
students = []
for i in range(num):
    name = input(f"Enter name of student {i+1}: ")
    students.append(name)

# Write the names to a file
with open("students.txt", "w") as file:
    for name in students:
        file.write(name + "\n")

print("\nStudent names have been saved to 'students.txt'.")

# Read and display the names from the file
print("\nReading from 'students.txt':")
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())
        #here strip() function just make format of name like std_name1 and std_name2 appear in continuous break line
