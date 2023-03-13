#4. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input("Input size n: "))
m = int(input("Input size m: "))
k = int(input("Input number of broken pieces: "))
if n * m % k != 0:
    print('Possible')
else:
    print('Impossible')
