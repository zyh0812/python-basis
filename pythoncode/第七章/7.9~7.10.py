# sandwich_orders = ['a', 'b', 'c', 'd']
# finished_sandwiches =[]

# while sandwich_orders:
#     sandwichs = sandwich_orders.pop()
#     print(f"I made your tuna sanwich:{sandwichs}.")
#     finished_sandwiches.append(sandwichs)
# print("\nThere are all sandwichs:")
# for i in finished_sandwiches:
#     print(i)

# sandwich_orders = ['a','pastrami', 'b', 'pastrami','c', 'pastrami']
# finished_sandwiches =[]
# print('Pastrami were selled ')

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# print(sandwich_orders)

# travel_list = {}
# print("If you could visit one place in the world , where would you go")
# travel_active = True
# while travel_active:
#     name = input("Please enter your name: ")
#     place = input("Please tell where you want to travel: ")
#     travel_list[name] = place

#     b = input("If go on?(yes/no)")
#     if b == 'no':
#         travel_active = False

# for name,place in travel_list.items():
#     print(f"{name} want to travel to {place}.")