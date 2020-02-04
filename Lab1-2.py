# 2 В таблице приведены формулы и три варианта исходных данных, по которым надо разработать
# три циклические программы с одними и теми же расчетными формулами.
import math

a = 8
m = 6
b = 5 * 10 ** (-3)
k = (1.6, 9.1, 8)

for i in range(len(k)):
    d = math.sin(k[i] / a) / math.cos(m * b)
    c = d / (d ** 2 + 1) / (1 - math.e ** k[i])
    print(c)
print("\n")

k = a
while k >= 3:
    d = math.sin(k / a) / math.cos(m * b)
    c = d / (d ** 2 + 1) / (1 - math.e ** k)
    print(c)
    k -= 0.5
print("\n")

x = (1.7, 5, -2)
for z in range(len(x)):
    a = 2
    while a <= 2.8:
        d = math.sin(x[z] / a) / math.cos(m * b)
        c = d / (d ** 2 + 1) / (1 - math.e ** x[z])
        print(c)
        a += 0.2
