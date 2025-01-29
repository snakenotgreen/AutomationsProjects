from math import *
#13
x = 34
a = 2
vid = 1
while a < 64:
    if x-a-1 <= 0:
        print('Відповіді нема')
        break
    else:
        vid *= (x-a)/(x-a-1)
        a *= 2
print(vid)

#38
a = 2
n = 14
vid = 0
while n != 0:
    vid += 2
    n -= 1
print(vid)

#76
result = 0
i = 1
while i <= 100:
    j = 1
    while j <= 60:
        result += sin(i**3 + j**4)
        j += 1
    i += 1
print(result)

#44
n = 5
a = 6
c = 1
vid = 0
while c < a:
    vid += a*c
    c+=1
print(vid)
#24
k = 1
n = 10
vid = 0
while k != n:
    vid += 1/(2*k+1)**2
    k+=1
print(vid)
#70
n = 16  # Задане число n
k = ''
i = 2
while i < n:
    a = n
    b = i
    while b:
        a, b = b, a % b #знаходимо НСД
    if a == 1:
        k += str(i) + ' '
    i += 1
print(k)
#6
n = 5
i = 1 #кількість доданків
while i <= n:
    cos_sum = 0
    sin_sum = 0
    j = 1
    while j <= i: #обчислення суми для кожного i
        cos_sum += cos(j)
        sin_sum += sin(j)
        j += 1
    result *= (cos_sum / sin_sum)
    i += 1
print(result)
#1
n = 5
result = 1

while n > 0:
    result *= 2
    n -= 1

print(result)
#71
p = 7
q = 21

divisors = ''

i = 1
while i <= q:
    if q % i == 0: # Якщо i є дільником q
        if gcd(p, i) == 1: # gcd(НСД) перевірка, чи є i взаємопростим з p
            divisors = f'{i }'
    i += 1
print("Дільники q, які взаємопрості з p:", divisors)
#43
a = 3
n = 10
c = 1
vid = 0
while c != n:
    vid += sqrt(10+a**2)
    c+=1
print(vid)
#18
m = 2
n = 42137
sum = 0

while m > 0 and n > 0:
    last_digit = n % 10  # Отримуємо останню цифру числа n
    sum += last_digit  # Додаємо цю цифру до суми
    n //= 10  # Видаляємо останню цифру числа n
    m -= 1

print(sum)
#6
# Границі інтегрування
a = 2
b = 3
n = 1000  # Кількість підінтервалів (збільшення для більшої точності)
# Ініціалізуємо суму та крок інтегрування
integral = 0
h = (b - a) / n #квадратурна формула
x = a + h / 2  #Початкова точка

# Обчислюємо інтеграл за допомогою квадратурної формули середніх прямокутників
i = 0
while i < n:
    integral += sin(1/(x*log(x, e)**2)) * h
    x += h
    i += 1

print("Значення інтеграла:", integral)