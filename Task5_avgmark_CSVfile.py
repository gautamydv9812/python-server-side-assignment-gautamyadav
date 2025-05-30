#program to read from CSV file of students marks and calculate average marks.
total_marks = 0
number_of_students = 0

with open('student_marks.csv', 'r') as file:
    next(file)  # Skip the first line (header)

    for line in file:
        # Split line by comma
        name, mark = line.strip().split(',')
        # Add the mark to total
        total_marks += int(mark)
        # Count the student
        number_of_students += 1

# Calculate average
average = total_marks / number_of_students
print("Average mark is:", average)
