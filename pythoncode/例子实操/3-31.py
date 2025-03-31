# from pathlib import Path

# path = Path('例子实操\pi_digits.txt')
# # contents = path.read_text()

# # contents = contents.rstrip()
# contents = path.read_text().rstrip()
# print(contents)

# path = Path('例子实操/pi_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# for line in lines:
#     print(line)

# path = Path('例子实操/pi_digits.txt')
# contents = path.read_text()
# lines = contents.splitlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()

# print(pi_string)
# print(len(pi_string))

# path = Path('例子实操\pi_million_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()

# print(f"{pi_string[:52]}...")
# print(len(pi_string)) 

# from pathlib import Path

# path = Path('例子实操\programming.txt')
# path.write_text("I love programming.")
# contents = "I love programming.\n"
# contents += "I love creating new games.\n"
# contents += "I also love working with data.\n"

# path = Path('例子实操\programming.txt')
# path.write_text(contents)

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nfirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nsecond number: ")
#     if second_number == 'q':
#         break

#     try:
#         print(int(first_number) / int(second_number))
#     except ZeroDivisionError:
#         print("You can't divide by 0!")

# while True:
#     first_number = input("\nfirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nsecond number: ")
#     if second_number == 'q':
#         break

#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)

# from pathlib import Path

# def count_words(path):

#     try:
#         contents = path.read_text(encoding='utf-8')
#     except FileNotFoundError:
#         # print(f"Sorry, the file {path} does no exit.")
#         pass
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {path} has about {num_words} words.")

# # path = Path('例子实操/alice.txt')
# # count_words(path)

# filenames = ['例子实操/alice.txt','t.txt','xiyouji.txt']
# for file in filenames:
#     path = Path(file)
#     count_words(path)

# from pathlib import Path
# import json

# numbers = [2,3,5,7,11,13]
# path = Path('例子实操/number.json')
# contents = json.dumps(numbers)
# path.write_text(contents)

# from pathlib import Path
# import json

# username = input("What's your name?")

# path = Path('例子实操/username.json')
# contents = json.dumps(username)
# path.write_text(contents)

# print(f"We will remember you when you com back, {username}")

# from pathlib import Path
# import json

# path = Path('例子实操/username.json')
# if path.exists():
#     contents = path.read_text()
#     username = json.loads(contents)
#     print(f"Welcome back, {username}")
# else:
#     username = input("What is your name?")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"We will remember you when you come back, {username}")

from pathlib import Path
import json

# def greet_user():
#     path = Path('例子实操/username.json')
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What's your name?")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")

# greet_user()

def get_store_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    username = input("What's your name?")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('例子实操/username.json')
    username = get_store_username(path)
    if username:
        username1 = input("请核对你的用户名：")
        if username1 == username:
            print(f"Welcome back,{username}!")
        else:
            print("用户名错误")
            get_new_username(path)
            print(f"Welcome back,{username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}")

greet_user()
        
    