# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi'
# }

# for key,value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")

# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust'
# }

# # for name in sorted(favorite_language.keys()):
# #     print(name.title())

# for language in favorite_language.values():
#     print(language.title())

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'red', 'points': 4}
# alien_2 = {'color': 'yellow', 'points': 1}

# aliens = [alien_0,alien_1,alien_2]

# for alien in aliens:
#     print(alien)

# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms','extra cheese']
# }

# for topping in pizza['toppings']:
#     print(topping)

users = {
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton'
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }

}

for username,user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")