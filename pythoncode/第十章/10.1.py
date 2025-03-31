# from pathlib import Path

# path = Path('第十章\learning_python.txt')
# contens = path.read_text()

#10.1
# print(contens)
# lines = contens.splitlines()
# python_line = []
# for line in lines:
#     python_line.append(line)
#     print(line)
# print(python_line)

#10.2
# lines = contens.splitlines()
# for i in range(3):
#     lines[i].replace('Python','C')
#     print(lines[i])
# contens = path.read_text().replace('Python','C')
# print(contens)

#10.3
# path = Path('例子实操\pi_million_digits.txt')
# contents = path.read_text().rstrip()

# for line in contents.splitlines():
#     print(line)

#10.4
# from pathlib import Path

# path = Path('第十章\guest.txt')
# name = input("请输入你的名字：")

# path.write_text(name)
# contents = path.read_text()
# print(f"你输入的名字为：{contents}")
# 
# 10.5

# from pathlib import Path
# names = ""

# path = Path('第十章\guest_book.txt')
# while 1:
#     name = input("请输入名字：")
#     if 'quit' in name:
#         break
#     names += name +'\n'

# path.write_text(names)


#10.6
# try:
#     first_number = int(input("Enter first number: "))
#     second_number = int(input("Enter second number: "))
# except ValueError:
#     print("请输入正确的数字!")
# else:
#     print(first_number+second_number)

#10.7
# while True:
#     try:
#         first_number = int(input("Enter first number: "))
#         second_number = int(input("Enter second number: "))
#     except ValueError:
#         first_number = int(input("Enter first number: "))
#         second_number = int(input("Enter second number: "))
        
#     else:
#         print(first_number+second_number)

#10.8
# from pathlib import Path
# path1 = Path('第十章/cat.txt')
# path2 = Path('第十章/dog.txt')
# try:
#     contents1 = path1.read_text('utf-8')
#     contents2 = path2.read_text('utf-8')

# except FileNotFoundError:
#     print("请确定文件的正确位置")
# else:
#     print(contents1)
#     print(contents2)

#10.9
# from pathlib import Path
# txt_list = ['第十章/cat.txt','第十章/dog.txt']
# for txt in txt_list:
#     path = Path(txt)
#     try:
#         contents = path.read_text('utf-8')
#     except FileNotFoundError:
#         pass
#     else:
#         print(contents)

#10.10
# from pathlib import Path
# book_list = ['第十章/book1.txt','第十章/book2.txt']

# for book in book_list:
#     path = Path(book)
#     contents = path.read_text('utf-8')
#     sum = 0
#     sum1 = contents.lower().count('the ')
#     sum += sum1
# print(sum)

# from pathlib import Path
# import json

# path = Path('第十章/number.json')
# if path.exists():
#    contents = path.read_text()
#    favorite_number = json.loads(contents)
#    print(f"I konw your favorite number! It's {favorite_number}")
# else:
#     favorite_number = int(input("请输入你喜欢的数字： "))
#     contents = json.dumps(favorite_number)
#     path.write_text(contents)
#     print(f"您喜欢的数字已经被记住") 

# from pathlib import Path
# import json

# def konw_favorie_number(path):
#     contents = path.read_text()
#     favorite_number = json.loads(contents)
#     return favorite_number

# def get_favorite_number(path):
#     favorite_number = int(input('请输入你喜欢的数字: '))
#     contents = json.dumps(favorite_number)
#     path.write_text(contents)

# def greet_number():
#     path = Path('第十章/number.json')
#     if path.exists():
#         favorite_number = konw_favorie_number(path)
#         print(f"我记得你最喜欢数字，是{favorite_number}")
#     else:
#         get_favorite_number(path)
#         print("你最喜欢的数字已经被记住")

# greet_number()


# from pathlib import Path
# import json

# def get_new_message(path):
#     messages = {}
#     messages['name'] = input("请输入你的名字: ")
#     messages['age'] = input("请输入你的年龄: ")
#     messages['work_place'] = input("请输入你的工作地点: ")
#     contents = json.dumps(messages)
#     path.write_text(contents)

# def know_message(path):
#     contents = path.read_text()
#     messages = json.loads(contents)
#     return messages

# def greet_user():
#     path = Path('第十章/usermessage.json')
#     if path.exists():
#         usermessage = know_message(path)
#         username = input("请输入你的用户名进行核对：")
#         if username == usermessage['name']:
#             print(f"欢迎回来，你的信息为：{usermessage}")
#         else:
#             print("用户名错误！")
#             get_new_message(path)
#             print("你的信息已经被记住")
#     else:
#         get_new_message(path)
#         print("你的信息已经被记住")
# greet_user()