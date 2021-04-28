x = int(input("Insira um número: "))
n = 1

while x < 0:
    x = int(input("Insira um número válido: "))
print(x, end="! = ")

for x in range(x, 0, -1):
    n *= x
    if x != 1:
        print(f'{x}', end=" x ")
    else:
        print(x, end='')
