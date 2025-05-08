# Student Marksheet Program

# Input student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Input marks for 5 subjects
print("Enter marks for 5 subjects:")
marks = []
total_marks = 0
for i in range(1, 6):
    mark = float(input(f"Subject {i} marks: "))
    marks.append(mark)
    total_marks += mark

# Calculate average
average = total_marks / 5

# Determine grade
if average >= 90:
    grade = 'A+'
elif average >= 80:
    grade = 'A'
elif average >= 70:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 50:
    grade = 'D'
else:
    grade = 'F'

# Display mark sheet
print("\n----- Student Marksheet -----")
print("Name: " + name)
print(f"Roll No   : {roll_no}")
print("Marks     : ", marks)
print(f"Total     : {total_marks}")
print(f"Average   : {average:.2f}")
print(f"Grade     : {grade}")
print("-----------------------------")

