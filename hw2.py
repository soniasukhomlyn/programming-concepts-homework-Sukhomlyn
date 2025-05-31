# 1
variable = "Hello, Python World!"
print(variable)

# 2
while True:
    a = input("Введіть перше число: ")
    if a.lstrip("-").isdigit():
        a = int(a)
        break
    else:
        print("Це не число. Спробуйте ще раз.")

while True:
    b = input("Введіть друге число: ")
    if b.lstrip("-").isdigit():
        b = int(b)
        break
    else:
        print("Це не число. Спробуйте ще раз.")

print("Додавання:", a + b)
print("Віднімання:", a - b)
print("Множення:", a * b)
print("Ділення:", a / b if b != 0 else "На нуль ділити не можна!")

# 3
s1 = "Слава"
s2 = "Україні!"
combined = s1 + " " + s2
print("Об'єднаний рядок:", combined)
print("Довжина рядка:", len(combined))

# 4
while True:
    num = input("Введіть ціле число для перевірки на парність: ")
    if num.lstrip("-").isdigit():
        num = int(num)
        break
    else:
        print("Це не число. Спробуйте ще раз.")

if num % 2 == 0:
    print("Парне")
else:
    print("Непарне")

# 5
for i in range(1, 11):
    print(i)

# 6
while True:
    num = input("Введіть будь-яке ціле число: ")
    if num.lstrip("-").isdigit():
        num = int(num)
        break
    else:
        print("Це не число. Спробуйте ще раз.")

if num > 0:
    print("Позитивний")
elif num < 0:
    print("Негативний")
else:
    print("Нуль")

# 7
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
    break

# 8
while True:
    n = input("Введіть ціле число n для підрахунку суми: ")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Це не число. Спробуйте ще раз.")

total = 0
for i in range(1, n + 1):
    total += i

print("Сума від 1 до", n, ":", total)

# 9
for i in range(10, 0, -1):
    print(i)

# 10
for i in range(1, 11):
    if i == 5:
        continue
    if i == 7:
        break
    print(i)
