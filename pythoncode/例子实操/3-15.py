# message = input("Tell me something, and I will repeat it back to you:")
# print(message)

# name = input("Please enter your name: ")
# print(f"\nHello, {name.title()}")

# prompt = "If you share your name, we can personalize the message you see."
# prompt += "\nWhat is your first name"

# name = input(prompt)
# print(f"Hello,{name.title()}")

# height = int(input("How tell are you, in inches? "))
# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you are a little older.")

# number = int(input("Enter a number,and I'll tell you if it's even or odd: "))

# if number % 2 == 0:
#     print(f"\nThe number {number} is even")
# else:
#     print(f"\nThe number {number} is odd.")

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt = '\nEnter "quit" to end the program. '
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt = '\nEnter "quit" to end the program. '
# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt = '\nEnter "quit" to end the program. '

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}")

# curren_number = 0
# while curren_number < 10:
#     curren_number += 1
#     if curren_number % 2 == 0:
#         continue
#     print(curren_number)

# x = 1
# while x <= 5:
#     print(x)

# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user}")
#     confirmed_users.append(current_user)

# print("\nThe follow users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets = ['dogs', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# responses = {}
# polling_active = True

# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
#     responses[name] = response

#     repeat = input("Would you like to let another person respond?(yes/no) ")
#     if repeat == 'no':
#         polling_active = False
# print("\n--- Poll Results ---")
# for name,response in responses.items():
#     print(f"{name.title()} would like to climb {response}.")

