# Задача 2: Найдите сумму цифр трехзначного числа.

while True:
    n = input('Введите трехзначное число: ')
    if (len(n) != 3):
        print('Необходимо ввести трехзначное число')
    else:
        n = int(n)
        break

summa = 0
while n != 0:
    summa += n % 10
    n //= 10

print(f'Сумма цифр введенного числа: {summa}')
#----------------------------------------------------------------------------------------------------------------------
# Задача 4: Петя, Катя, Сережа и журавлики

n = int(input('Сколько всего сделали журавликов: '))
print(f'Петя сделал {n/6}\nСережа сделал {n/6}\nКатя сделала {n*2/3}')

#----------------------------------------------------------------------------------------------------------------------
# Задача 6: Проверить счастливость билета (сумма первых трех цифр равна
# сумме последних трех цифр)

while True:
    n = input('Введите шестизначный номер билета: ')
    if len(n) != 6:
        print('Необходимо ввести шестизначный номер!')
    else:
        n = int(n)
        break

sum1 = 0
sum2 = 0

for i in range(0, 3):
    sum1 += n % 10
    n //= 10

for i in range(0, 3):
    sum2 += n % 10
    n //= 10

if sum1 == sum2:
    print('Билет счастливый!')
else:
    print('Билет обычный')

#----------------------------------------------------------------------------------------------------------------------
# Задача 8: Определить, можно ли от шоколадки n x m отломить k долек

n = int(input('Введите длину шоколадки(n): '))
m = int(input('Введите ширину шоколадки(m): '))
k = int(input('Сколько долек нужно отломить: '))

if (k % n == 0 or k % m == 0) and (k < m * n):
    print('Можно отломить')
else:
    print('Нельзя отломить')
