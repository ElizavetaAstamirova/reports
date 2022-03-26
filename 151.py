n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
nums = 0
summ = 0
for i in range(n):
    for j in range(len(matrix[0])):
        if matrix[i][j] % 3 == 0 and matrix[i][j] > 0:
            nums += 1
            summ += matrix[i][j]
print(summ / nums)