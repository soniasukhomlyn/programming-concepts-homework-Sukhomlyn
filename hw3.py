# Початковий рівень

# 1
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)

# 2
minimum = min(numbers)

# 3
reversed_list = numbers[::-1]

print("Перевернутий список:", reversed_list)

# 4
odd_numbers = []
for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

print("Непарні числа:", odd_numbers)

# 5
factor = int(input("Введіть число, на яке потрібно помножити елементи списку: "))
multiplied = []
for number in numbers:
    multiplied.append(number * factor)

print("Помножений список:", multiplied)

# Легкий рівень

# 1
X = int(input("\nВведіть X для фільтрації (більше за X): "))
filtered = []
for number in numbers:
    if number > X:
        filtered.append(number)
print("Числа більші за X:", filtered)

# 2
positive = []
for number in numbers:
    if number > 0:
        positive.append(number)
average = sum(positive) / len(positive) if positive else 0
print("Середнє додатних чисел:", average)

# 3.
X = int(input("Введіть X для фільтрації чисел у списку (менше за X): "))
less_than_X = []
for number in numbers:
    if number < X:
        less_than_X.append(number)
max_val = max(less_than_X) if less_than_X else None
print("Максимум чисел < X:", max_val)

# 4
Y = int(input("Введіть Y: "))
div_sum = 0
for number in numbers:
    if number % Y == 0:
        div_sum += number
print("Сума чисел, що діляться на Y:", div_sum)

# 5
squares = []
for number in numbers:
    squares.append(number ** 2)
print("Квадрати чисел:", squares)

# 6
positives = []
for number in numbers:
    if number > 0:
        positives.append(number)
print("Додатні числа:", positives)

# 7
strings = input("Введіть слова (через кому): ").split(",")
prefix = input("Введіть префікс: ")
prefixed = []
for s in strings:
    if s.strip().startswith(prefix):
        prefixed.append(s.strip())
print("Слова, що починаються з вказаного префікса:", prefixed)

# 8.
N = int(input("Введіть число N: "))
sum_N = 0
for i in range(min(N, len(numbers))):
    sum_N += numbers[i]
print("Сума перших N чисел:", sum_N)

# 9
palindromes = []
for s in strings:
    word = s.strip()
    if word == word[::-1]:
        palindromes.append(word)
print("Паліндроми:", palindromes)

# 10
divisor = int(input("Введіть дільник: "))
div_check = []
for number in numbers:
    div_check.append(number % divisor == 0)
print("Подільність:", div_check)

# Середній рівень

# 1
X = int(input("\nВведіть X: "))
Y = int(input("Введіть Y: "))
filtered = []
for number in numbers:
    if number % X == 0 and number % Y != 0:
        filtered.append(number)
print("Діляться на X, але не на Y:", filtered)

# 2.
nested_input = input("Введіть декілька списків чисел через крапку з комою (;), а самі числа через кому (,)\nНаприклад: 1,2;3,4;5\n> ")
raw_sublists = nested_input.split(";")
nested_lists = []
for sub in raw_sublists:
    number_strings = sub.split(",")
    sublist = []

    for num_str in number_strings:
        sublist.append(int(num_str))

    nested_lists.append(sublist)

flattened = []

for sublist in nested_lists:
    for number in sublist:
        flattened.append(number)

print("Єдиний список з усіх вкладених:", flattened)

# 3
text = input("Введіть текст: ")
uppercase_chars = []
for char in text:
    if char.isupper():
        uppercase_chars.append(char)
print("Великі літери у слові:", uppercase_chars)

# 4
from collections import Counter

items_input = input("Введіть список чисел для сортування (через пробіл): ")
string_numbers = items_input.split()

items = []
for string in string_numbers:
    number = int(string)
    items.append(number)

counts = Counter(items)

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        a, b = items[i], items[j]
        if b > a:
            items[i], items[j] = items[j], items[i]
        elif b == a and counts[b] > counts[a]:
            items[i], items[j] = items[j], items[i]

print("Відсортований список:", items)

# 5
a_input = input("Введіть список A (через пробіл): ")
a_strings = a_input.split()

a = []
for s in a_strings:
    number = int(s)
    a.append(number)

b_input = input("Введіть список B (через пробіл): ")
b_strings = b_input.split()

b = []
for s in b_strings:
    number = int(s)
    b.append(number)

combined = []

min_length = min(len(a), len(b))

for i in range(min_length):
    if a[i] % 2 == 0:
        combined.append(a[i])
    else:
        combined.append(b[i])

print("Комбінований список:", combined)


# 6
data_input = input("Введіть пари ключ=значення через кому (наприклад: a=10,b=20,a=30): ")
data = [pair.strip().split("=") for pair in data_input.split(",")]
agg = {}
for key, val in data:
    val = int(val)
    if key in agg:
        agg[key] += val
    else:
        agg[key] = val
print("Агрегований словник:", agg)

# 7

input_string = input("Введіть список чисел для заміни (через пробіл): ")
string_list = input_string.split()

lst = []
for s in string_list:
    number = int(s)
    lst.append(number)

replaced = []
for num in lst:
    if num < 0:
        replaced.append(0)
    else:
        replaced.append(num)

print("Після заміни:", replaced)


# 8
string_list = input("Введіть список слів через кому: ").split(",")
X = int(input("Введіть мінімальну довжину слова: "))
count = 0
for s in string_list:
    if len(s.strip()) > X:
        count += 1
print("Кількість довгих слів:", count)

# 9
list1 = input("Введіть перший список рядків (через кому): ").split(",")
list2 = input("Введіть другий список рядків (через кому): ").split(",")
combined = []
for i in range(min(len(list1), len(list2))):
    combined.append(list1[i].strip() + list2[i].strip())
print("Чергування:", combined)

# 10
X = int(input("Введіть X для порівняння: "))
Y = int(input("Введіть Y для множення: "))
result = []
for number in numbers:
    if number > X:
        result.append(number * Y)
    else:
        result.append(number)
print("Помножено за умовою:", result)
