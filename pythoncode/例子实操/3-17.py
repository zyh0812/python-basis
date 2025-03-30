
# def greet_user():
#     print("Hello!")

# greet_user()
# def greet_user(username):
#     print(f"Hello, {username.title()}!")

# greet_user('jesse')

# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster','harry')

# def describe_pet(animal_type,pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# # describe_pet("dog","mike")
# # describe_pet("cat","sweety")

# describe_pet(animal_type='dog',pet_name='maie')
# describe_pet(pet_name="sweetty",animal_type="cat")

# def describe_pet(pet_name, animal_type='dog'):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(pet_name="mike",animal_type="cat")

# def get_formatted_name(first_n,last_n):
#     full_name = f"{first_n} {last_n}"
#     return full_name.title()

# name = get_formatted_name("zhou","yuhong")
# print(name)

# def get_formatted_name(first_n,middle_n,last_n):
#     full_name = f"{first_n} {middle_n} {last_n}"
#     return full_name.title()

# musician = get_formatted_name("john", 'lee', 'hooker')
# print(musician)

# def get_formatted_name(first_n,last_n,middle_n=''):
#     if middle_n:
#         full_name = f"{first_n} {middle_n} {last_n}"
#     else:
#         full_name = f"{first_n} {last_n}"
#     return full_name.title()

# musician = get_formatted_name('jimi','hendrix')
# musician2 = get_formatted_name('john', 'hooker', 'lee')
# print(musician,"\n",musician2)


# def build_person(first_n,last_n):
#     person = {"first": first_n,'last':last_n}
#     return person

# musician = build_person('jimi', 'hendrix')
# print(musician)

# def build_person(first_name, last_name, age=None):
#     person = {"first": first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)


# def get_formatted_name(first_n,last_n):
#     full_name = f"{first_n} {last_n}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name: ")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     formatted_name = get_formatted_name(f_name,l_name)
#     print(f"\nHello, {formatted_name.title()}")

# def get_formatted_name(first_n,last_n):
#     full_name = f"{first_n} {last_n}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
    
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     for_name = get_formatted_name(f_name,l_name)
#     print(f"\nHello, {for_name}")