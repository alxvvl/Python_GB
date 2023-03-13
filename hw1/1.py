# 1. Найдите сумму цифр трехзначного числа.
n = int(input("Input number with 3 digits: "))

n1 = n % 10
n2 = n // 10 % 10
n3 = n // 100 % 10
sum = n1 + n2 + n3
print(n1)
print(n2)
print(n3)
print(sum)



