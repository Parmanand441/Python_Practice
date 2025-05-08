# # Check whether a condition is true or not.
'''value = input("Write something.")
if "Evidence found" in  value:
    print('War')
else:
    print('Peace')'''

# # 2nd code in python

'''canals = input("Say something")
if "construct six new canals" in canals:
    print('Padar Khaenden')
else:
    print('Padar Na khaenden')'''

# # 3rd code in python

'''num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

check wether number is even or odd'''

'''num = int(input("Enter number"))
if num % 2==0:
   print("Even")
else:
   print("Odd")

first = int(input("Enter first number"))
second = int(input("Enter second number"))

if first>second:
    print("first is greater than second")
else:
      print("second is greater than first")'''

#student marksheet

'''name = input("Enter student name")
rollnumber = int(input("Enter student rollnumber"))
marks = int(input("Enter student marks"))
totalmarks = 100
average = marks * totalmarks / 100

if marks >= 80:
    print(f"Name: {name}\nGrade A-1 \nAverage: {average:.2f} \nCongratulations! {name}")
elif marks>=70:
    print(f"Name: {name}\nGrade A \nAverage: {average:.2f} \nCongratulations! {name}")
elif marks>=60:
    print(f"Name: {name}\nGrade B \nAverage: {average:.2f} \nCongratulations! {name}")
elif marks>=50:
    print(f"Name: {name}\nGrade C \nAverage: {average:.2f} \nCongratulations! {name}")
else:
    print(f"Name: {name}\nGrade D \nAverage: {average:.2f} \nSorry you're failed, hard luck for next time! {name}")
'''
#grade 
'''def grade_message(grade):
    return {
        "A": "Excellent!",
        "B": "Very Good",
        "C": "Good",
        "D": "Needs Improvement"
    }.get(grade.upper(), "Invalid grade")

grade = input("Enter grade: ")
print(grade_message(grade))'''

#calculator

'''num1 = int(input("Enter value 1:"))
num2 = int(input("Enter valu3 2:"))
print(f"The sum of num1 and num2 is: {num1 + num2}")
print(f"The sub of num1 and num2 is: {num1 - num2}")
print(f"The multiple of num1 and num2 is: {num1 * num2}")
print(f"The division of num1 and num2 is: {num1 / num2}")'''

# leap year check 
'''year = int(input("Enter a year: "))
if (year % 4 == 0):
    print("Leap year")
else:
    print("Not a leap year")'''


# multiple students marks

# Function to calculate grade based on average
'''def calculate_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

# List to store all student data
students = []

n = int(input("Enter number of students: "))

for _ in range(n):
    name = input("\nEnter student name: ")
    roll = input("Enter roll number: ")
    
    marks = []
    total = 0

    print("Enter marks for 5 subjects:")
    for i in range(1, 6):
        m = float(input(f"Subject {i}: "))
        marks.append(m)
        total += m

    average = total / 5
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)

# Display all student data
print("\n----- Student Marksheet Summary -----")
for s in students:
    print(f"\nName: {s['name']}")
    print(f"Roll No: {s['roll']}")
    print(f"Marks: {s['marks']}")
    print(f"Total: {s['total']}")
    print(f"Average: {s['average']:.2f}")
    print(f"Grade: {s['grade']}")

# Calculate class average
class_avg = sum(s['average'] for s in students) / n
print(f"\nClass Average: {class_avg:.2f}")

# Find topper
topper = max(students, key=lambda s: s['total'])
print(f"\nTopper: {topper['name']} (Roll: {topper['roll']}) - Total: {topper['total']}")

'''

# chatbot

'''import random

responses = {
    "hi": ["Oh great, you're here again.", "Hi... I guess.", "Hello, mortal."],
    "how are you": ["I'm a bot. I have no feelings, unlike your ex.", "Thriving on electricity!"],
    "what is your name": ["I’m SarcastoBot, your emotional support toaster.", "Name’s Bot. Sarcastic Bot."],
    "bye": ["Finally. I thought you’d never leave.", "Bye. Try not to trip over your own ego."]
}

default_responses = [
    "Interesting. Tell me more so I can pretend to care.",
    "Oh wow. Let me alert the media.",
    "Fascinating... not really.",
    "I'm just a bot, not your therapist!"
]

print("🤖 Welcome to SarcastoBot!")
print("Type 'bye' to end the convo.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("SarcastoBot: Bye. Try not to break anything.")
        break
    elif user_input in responses:
        print("SarcastoBot:", random.choice(responses[user_input]))
    else:
        print("SarcastoBot:", random.choice(default_responses))'''

'''num = int(input("Enter number:"))
divided = 5
if num % 2==0 and num % divided== 0:
    print("Your number is even, and divisible by 5")
elif num % 2==0:
    print("Your number is even but not divisble by 5")
elif num % 2!=0 and num % divided== 0:
    print("your number is odd, and not divisible by 5")
else:
    print("something went wrong....")'''

#table

# Multiplication tables from 2 to 10
'''for num in range(1, 11):
    print(f"\n1 To 11 {num}")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")'''

# Print letters from A to Z
'''for letter in range(ord('A'), ord('Z') + 1):
    print(chr(letter), end=' ')'''
'''def char_range(start, end):
    for c in range(ord(start), ord(end) + 1):
        yield chr(c)

for letter in char_range('A', 'Z'):
    print(letter, end=' ')'''
'''letter = input("Enter a letter: ")
if letter.isdigit():
    print("Integers are not allowed!")
if "hardwork" in letter:
    print("Right")
elif "hard" in letter:
    print("Almost right, but not exact!")
elif "work" in letter:
    print("Somehow right, but not exact")
elif "ard" in letter:
    print("Null")
else:
    print("Invalid Value!")'''



# Get the input from the user remove any word and add any word..
'''letter = input("Enter a letter: ")
remove_value = input("Enter the value to remove: ")
add_value = input("Enter the value to Add: ")
modified_input = letter.replace(remove_value, "")
modified_input += add_value
print(f"Modified input: {modified_input}")'''

# Word suggestion
'''word_list = ["hard", "hardwork", "work", "worker", "working", "smart", "effort", "success"]
word = input("Enter any word: ").lower()
suggestions = [w for w in word_list if w.startswith(word)]
if suggestions:
    print("Suggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("No suggestions found.")
print(word_list)'''

'''if 5 > 2:
  print("Five is greater than two")'''

# taking two inputs at a time
'''x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)'''
 
# taking three inputs at a time
'''x, y, z = map(int, input("Enter three values (separated by space): ").split())

print("Total number of students: ", x + y + z)
print("Number of boys is: ", x+y)
print("Number of girls is: ", z)'''

'''letters = input("Enter names:")
print(letters)
remove_value = input("Enter the value that you want to remove:")
modified_value = letters.replace(remove_value, "")
add_value = input("Add new letter:")
modified_value += add_value
print(modified_value)'''

'''for num in range(2, 11):
    print(f"\nTable of: {num}")
    for i in range(1, 11):
        print(f"{i} x {num} = {num * i}")'''
'''for num in range(1, 11):
    print(f"\nTable of : {num}")
    for i in range(1, 11):
        print(f"{i} x {num} = {num * i}")'''
'''number = int(input("Enter any number")) 
for i in range(1, 11):
        print(f"{i} x {number} = {number * i}")'''


'''score = 0 
for number in range(5):
    number = int(input("Enter any number: "))
    answer = input("Is the number Even or Odd? ")

    if number % 2 == 0 and answer == "even":
        print("Correct! It's even.")
        score += 1
    elif number % 2 != 0 and answer == "odd":
        print("Correct! It's odd.")
        score += 1
    else:
        print("Wrong answer.")
if score == 5:
    print("Congratulations! Your total score is:", score)
else:
    print("Game Over! Your total score is:", score)'''

# password suggestions
'''password = input("Enter Password:")
if password == "":
    print("Null")
elif password == "Parmanand":
    print("Password is weak")
    print("Use symbols and numbers")
    password = input("Enter Password:")
elif password =="Parmanand1":
    print("Password is still weak!")
    print("Use symbols and numbers")
    password = input("Enter Password:")
elif password == "Parmanand12@#":
    print("Password is perfect")
    print("Thank you for choosing strong password")
else:
    print("Invalid!")'''

#random password generator
'''import random
import string

# Length of the password
length = int(input("Enter the desired password length: "))

# Define the character set
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ''.join(random.choice(characters) for _ in range(length))

# Show the result
print("Your generated password is:", password)'''

    




