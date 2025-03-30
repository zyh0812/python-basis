# 9.13 设置骰子
# from random import randint
# class Die:
#     def __init__(self):
#         self.sides = 20

#     def roll_die(self):
#         a = randint(1,self.sides)
#         return a

# die = Die()
# for i in range(1,11):
#     print(die.roll_die())

# from random import choice
# class Lottery:
#     def __init__(self):
#         self.list = ['1','2','3','4','5','6','7','8','9','10','a','b','c','d','e']
    
#     def roll(self):
#         results = []
#         temp_list = self.list.copy()
#         for i in range(0,4):
#             choice_result = choice(temp_list)
#             results.append(choice_result)
#             temp_list.remove(choice_result)
        
#         return results
# lottery_result = []
# lottery = Lottery()
# times = 0
# my_ticket = ['1','3','a','c']
# while True:
#     times += 1
#     lottery_result = lottery.roll()
#     if (lottery_result == my_ticket):
#         break
# print(f"抽奖次数: {times}")

    