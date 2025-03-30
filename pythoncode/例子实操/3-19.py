# def greet_users(names):
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)

# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

# unprinted_designs = ['print case', 'robot pendent', 'dodecahedron']
# completed_models = []
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model:{current_design}")
#     completed_models.append(current_design)

# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# def print_moudels(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
#     for i in unprint_designs:
#         print(i)

# def show_completed_models(completed_models):
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model) 

# unprint_designs = ['phone case', 'robot pendant', 'dodecachedron']
# completed_models = []

# print_moudels(unprint_designs[:], completed_models)
# # show_completed_models(completed_models)


# def make_pizza(*toppings):
#     print(toppings)

# make_pizza('zyh')
# make_pizza('hyd','ljw','zyx')

# def make_pizza(*toppings):
#     print("\nMking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"-{topping}")

# make_pizza('zyh')
# make_pizza('hyd','ljw','zyx')


# def make_pizza(size,*toppings):
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"-{topping}")

# make_pizza(16,'zyh')
# make_pizza(12,'hyd','ljw','zyx')


# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert','einstein',
#                              location = 'princeton',
#                              filed = 'physics')
# print(user_profile)

# def sanwichs(*food):
#     print(f"Sanwich's food -{food}")

# sanwichs('zyh')
# sanwichs('ljw','hyd')
# sanwichs('ljw','hyd','zyx')

# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert','einstein',
#                              location = 'princeton',
#                              filed = 'physics')


# a = build_profile('zhou','yuhong',
#                 location = 'wuhan',
#                 filed = 'physics')
# print(a)


# def cars(build_id,size,**any):
#     any['build_id'] = build_id
#     any['size'] = size
#     return any

# car = cars('sanbaru','s',
#            'color' = blue,) 


