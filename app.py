# print("Hello World")

# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")

# character_name = "Tom"
# character_age = 50.44
# is_male = True


# print("Learning Python")
# print("Learning\nPython")
# print("Learning\"Python")
# print("Learning\Python")
# phrase = "Learning Python"
# print(phrase)
# # concatenation: string appending another string
# print(phrase + "is important")
# # function
# print(phrase.lower())
# print(phrase.upper())
# print(phrase.isupper())
# print(phrase.upper().isupper())
# print(len(phrase))
# print(phrase[0])
# print(phrase[0:3])
# print(int(phrase.index("L")))
# print(int(phrase.index("n"))) # the first index
# print(int(phrase.index("Py")))
# # print(int(phrase.index("z"))) # throw error
# print(phrase.replace("Learning", "Studying"))

# print(2)
# print(2.123)
# print(-2)
# print(2 + 4)
# print(2 * 3.5)
# print(2 * 3 + 4)
# print(2 * (3 + 4))
# print(10 % 3)
# my_num = 4
# print(my_num)
# # Convert a number into a string
# print(str(my_num) + " is 4")
# # print(my_num + " is 4") # error
# # function
# neg_num = -3
# print(abs(neg_num))
# print(pow(3, 2)) # 3 ^ 2
# print(max(3, 2, 5))
# print(min(3, 2, 5))
# print(round(3.2))
# print(round(3.7))
# # import external code
# from math import *
# print(floor(3.7))
# print(ceil(3.7))
# print(sqrt(4))

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)

'''
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2
print(result)
# By default, python convert the input number into a string
# Convert string into number
# result = int(num1) + int(num2)
result = float(num1) + float(num2)
print(result)
'''


'''
# print("Roses are red")
# print("Violets are blue")
# print("I love you")
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
'''

'''
my_list = ["String", 2, 'v', True]
print(my_list)

friends = ["Elle", "Emily", "Eileen"]
print(friends)
print(friends[2])
print(friends[-1])
print(friends[-2])
print(friends[0:2])
print(friends[0:3])
print(friends[1:])
friends[1] = "Ami"
print(friends[1])
'''

'''
numbers = [10, 3, 5, 5]
friends = ["Ami", "Bella", "Clair", "Divina", "Eileen"]
print(friends)
friends.extend(numbers)
print(friends)
friends.append("Fenty")
print(friends)
friends.insert(1, "Gina")
print(friends)
friends.remove(3)
print(friends)
friends.pop()
print(friends)
print(friends.index("Ami"))
print(friends.count(5))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
# friends.sort() # error, int vs. string
# print(friends)
friends2 = friends.copy()
print(friends2)
friends.clear()
print(friends)
'''

'''
coordinates = (1, 2)
print(coordinates)
print(coordinates[0])
# coordinates[0] = 10 # error, tuple cannot be change
'''

'''
def say_hi():
    # intend sensitive
    print("Hi, there!")
print("Top")
say_hi()
print("Bottom")

def say_bye(name):
    print("Bye, " + name)
say_bye("Tom")
say_bye("Jerry")

def profile(name, age):
    print("Name is " + name + ", age is " + str(age))
profile("Tom", 12)
'''

'''
def cube1(num):
    num * num * num
print(cube1(3))


def cube2(num):
    return num * num * num
# print(cube2(3))
result = cube2(4)
print(result)
'''

'''
is_male = True
is_tall = True

if is_male:
    print("You are a male")
else:
    print("You are NOT a male")

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You either not male or not tall or both")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are NOT a male but are tall")
else:
    print("You are NOT a male and NOT tall ")
'''

'''
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(4, 2, 9))
'''

'''
num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
'''

'''
dateConversions = {
    "Mon": "Monday",
    "Tue": "Tuesday",
    "Wed": "Wednesday",
    "Thu": "Thursday",
    "Fri": "Friday",
    "Sat": "Saturday",
    "Sun": "Sunday"
}
print(dateConversions["Sat"])
print(dateConversions["Mon"])
print(dateConversions.get("Fri"))
# default value
print(dateConversions.get("Abd", "Not a valid key"))
'''

'''
i = 1
while i <= 5:
    print(i)
    i += 1
    # i++ # error
print("Loop End!")
'''

'''
secret_word = "morning"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True;

if out_of_guesses:
    print("Out of guesses! You lose!")
else:
    print("You win!")
'''

'''
for letter in "Hi, there":
    print(letter)

friends = ["Ami", "Bella", "Eileen"]
for friend in friends:
    print(friend)

for index in range(10):
    print(index)

for index in range(3, 10):
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First element")
    else:
        print("NOT First element")
'''

'''
print(2 ** 3) # 2 ^ 3

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result *= base_num
    return result
print(raise_to_power(2, 4))
'''

'''
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[1][1])

for row in number_grid:
    for col in row:
        print(col)
'''

'''
# vowels -> g
# dog -> dgg
# cat -> cgt

def translate(phrase):
    translation = ""
    for letter in phrase:

        # if letter in "AEIOUaeiou":

        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
'''

# Comments
'''
multiple
line
comments
'''
# print("Comments are fun")


'''
try:
    value = 10 / 0 # ZeroDivisionError
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
'''


'''
# open("employees.txt", "r")
# open("employees.txt", "w")
# open("employees.txt", "a")
# open("employees.txt", "r+")

# r -> read only
# w -> write -> add / change info in the file
# a -> append info at the end of the file, but not change the existing info
# r+ -> read and write
# open file, must close file

employee_file = open("employees.txt", "r")

# print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readline())
# print(employee_file.readlines())
# print(employee_file.readlines()[2])
for employee in employee_file.readlines():
    print(employee)

employee_file.close()
'''

'''
employee_file = open("employees.txt", "a")
employee_file.write("Frank - HR")
employee_file.write("\nGina - Customer Service")
employee_file.close()

employee_file = open("employees1.txt", "w")
employee_file.write("Helen - HR")
employee_file.write("\nIvy - Customer Service")
employee_file.close()

employee_file = open("index.html", "w")
employee_file.write("<p>This is HTML</p>")
employee_file.close()
'''

'''
import useful_tools

print(useful_tools.roll_dice(10))

import docx
'''

'''
from Student import Student # from Student file import Student class

student1 = Student("Ami", "Business", 3.2, False)
student2 = Student("Bill", "Computer", 3.9, True)

print(student1)
print(student1.major)
print(student2.name)
'''


'''
from Question import Question
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
'''


'''
from Student import Student

student1 = Student("Ami", "Business", 3.2, False)
student2 = Student("Bill", "Computer", 3.9, True)

print(student1.on_honor_roll())
print(student2.on_honor_roll())
'''

from Farm import Farm
from TropicalFarm import TropicalFarm

myFarm = Farm()
myFarm.plant_apple()
myFarm.plant_grape()

myTropicalFarm = TropicalFarm()
myTropicalFarm.plant_grape()
myTropicalFarm.plant_mango()





