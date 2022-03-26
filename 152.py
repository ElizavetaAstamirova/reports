n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
s = int(input())
for i in range(n):
    print(i)
    matrix[s - 1][i] += 3
print(matrix)