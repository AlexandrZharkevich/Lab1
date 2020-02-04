# Найти для каждого элемента списка А сумму предыдущих элементов и записать эти суммы в новый список B.
import random

A = []
for i in range(10):
    A.append(random.randint(0, 100))
print(A)

B = []
for i in range(len(A)):
    sum = 0
    for j in range(i - 1, -1, -1):
        sum += A[j]
    B.append(sum)
print(B)
