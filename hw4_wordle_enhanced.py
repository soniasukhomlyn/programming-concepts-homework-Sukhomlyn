import random


def secret_word_generator(words):
    random_value = random.random()
    scaled_value = random_value * len(words)
    random_index = int(scaled_value)
    return words[random_index]


def checking_the_guess(guess, secret_word):
    result = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            result.append('correct')
        elif guess[i] in secret_word:
            result.append('present')
        else:
            result.append('absent')
    return result


def display_result(guess, result):
    display = []
    for i in range(len(guess)):
        res = result[i]
        if res == 'correct':
            display.append("[" + guess[i].upper() + "]")
        elif res == 'present':
            display.append("(" + guess[i] + ")")
        else:
            display.append(" " + guess[i] + " ")
    print("Result:", ' '.join(display))


def play_round(secret_word, tries):
    guess = input(f"Attempt {7 - tries}/6 – Enter your guess: ").lower()

    if not guess:
        print("You must enter a word!")
        return False

    if len(guess) != len(secret_word):
        print(f"Wrong length. Expected {len(secret_word)} letters.")
        return False

    if not guess.isalpha():
        print("No such symbol can be in a word, try again!")
        return False

    if any(char.isdigit() for char in guess):
        print("No such symbol can be in a word, try again!")
        return False

    if guess == secret_word:
        print("Good job, You win!!! :) <З")
        return True

    result = checking_the_guess(guess, secret_word)
    display_result(guess, result)

    return False


def game_loop(words):
    secret_word = secret_word_generator(words)
    tries = 6
    print("Welcome to Wordle!")
    print(f"Guess the {len(secret_word)}-letter word. You have {tries} tries.")

    while tries > 0:
        if play_round(secret_word, tries):
            break
        tries -= 1
    else:
        print(f"Sorry, but you lost! The word was: {secret_word}")


words = ['apple', 'bread', 'candy', 'dream', 'eagle', 'flame', 'grape', 'house', 'input', 'joker']

game_loop(words)

# Під час рефакторингу гри Wordle я зрозуміла, наскільки важливо організувати код у чіткі функції,
# кожна з яких виконує лише одну задачу. Це робить програму легшою для розуміння і тестування.
# Ключовим аспектом рефакторингу стало покращення обробки помилок.
# Раніше код не міг коректно реагувати на неправильний ввід, що ускладнювало взаємодію з користувачем.
# Тепер програма чітко повідомляє про помилки, наприклад, коли введено цифри або спеціальні символи.
# Ще одне важливе покращення — оптимізація коду.
# Я замінила деякі зайві цикли на простіші перевірки, що зробило код компактнішим й ефективнішим.
# Програма стала зручнішою як і для користувача, так і для мого розуміння, бо тепер все красиво і зрозуміло організовано :)
# Однак, я зрозуміла, що можна було б покращити ще кілька моментів:
# 1. Додати рівні складності для гри, щоб користувач міг обирати, наприклад, слова різної довжини.
# 2. Можна було б вдосконалити фідбек для користувача, додаючи більше підказок або зробивши повідомлення інтерактивнішими.
# 3. Тестування коду може бути також ще детальнішим.
