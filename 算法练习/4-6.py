# a,b,c = map(int,input().split())
# print(a, b, c)

# n = int(input())
# lst = [int(input()) for _ in range(n)]
# print(lst)

# n,m = map(int, input().split())

# matrix = [list(map(int,input().split())) for _ in range(n)]
# print(matrix)

# square = [i**2 for i in range(1,11)]
# print(square)

# evens = [i for i in range(1,20) if i % 2 == 0]
# print(evens)

# input_data = list(map(int, input().split()))
# print(input_data)

# input_data = [int(x) for x in input().split()]
# print(input_data)

# n = 3 
# zero_matrix = [[0 for _ in range(n)] for _ in range(n)]
# print(zero_matrix)

# n = 10
# fib = [0, 1]
# [fib.append(fib[-1] + fib[-2]) for _ in range(n - 2)]
# print(fib)

# martix = [[1,2,3], [4,5,6], [7,8,9]]
# flatten = [x for row in martix for x in row]
# print(flatten)

# s = "algorithm"
# char_count = {char:s.count(char) for char in set(s)}
# print(char_count)

# n = 5
# for i in range(n * 2):
#     idx = i % n
#     print(idx,end = " ")


rows,cols = 2,3
grid = [(i,j) for i in range(rows) for j in range(cols)]
print(grid)