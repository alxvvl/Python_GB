# 3. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

num = int(input("Input number with 6 digits: "))
num1 = num % 10
num2 = num // 10 % 10
num3 = num // 100 % 10
num4 = num // 1000 % 10
num5 = num // 10000 % 10
num6 = num // 100000 % 10
result = bool(num1 + num2 + num3 == num4 + num5 + num6)
print(f"Lucky number: {result}")