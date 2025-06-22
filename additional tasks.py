# таск 1 — генерація тексту на основі ланцюгів Маркова

import random
import re


def read_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def clean_text(text):
    return text.lower()


def tokenize_text(text):
    return re.findall(r"\w+|[^\w\s]", text)


def create_markov_chain(tokens):
    markov_chain = {}

    for i in range(len(tokens) - 1):
        current_token = tokens[i]
        next_token = tokens[i + 1]

        if current_token not in markov_chain:
            markov_chain[current_token] = []

        markov_chain[current_token].append(next_token)

    return markov_chain


def generate_text(markov_chain, length=200):
    current_word = random.choice(list(markov_chain.keys()))
    result = [current_word]

    for _ in range(length - 1):
        next_word = random.choice(markov_chain[current_word])
        result.append(next_word)
        current_word = next_word

    return " ".join(result)


def main():
    file_path = "Friday-5th-August-Afternoon-Session-Oversharing-Sylvia-Plath.txt"
    text = read_text(file_path)
    cleaned_text = clean_text(text)
    tokens = tokenize_text(cleaned_text)
    markov_chain = create_markov_chain(tokens)

    generated_text = generate_text(markov_chain, length=200)

    print(generated_text)


if __name__ == "__main__":
    main()

# таск 2 — аналіз макроекономічних даних

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("macro.csv")

df_long = df.set_index("Series Name").transpose()
df_long.index.name = "Year"
df_long.reset_index(inplace=True)
df_long.columns = ["Year", "GDP", "Inflation", "ExchangeRate", "Unemployment"]
df_long["Year"] = df_long["Year"].astype(int)

df_long["GDP_Growth_%"] = df_long["GDP"].pct_change() * 100

# graph 1
plt.figure(figsize=(10, 5))
plt.plot(df_long["Year"], df_long["GDP"] / 1e9, label="GDP (млрд $)", marker="o")
plt.plot(df_long["Year"], df_long["Inflation"], label="Інфляція (%)", marker="s")
plt.title("ВВП і рівень інфляції в Україні (2000–2023)")
plt.xlabel("Рік")
plt.ylabel("Значення")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# graph 2
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(df_long["Year"], df_long["ExchangeRate"], label="Курс долара", color="green", marker="o")
plt.ylabel("Курс")
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(df_long["Year"], df_long["Unemployment"], label="Безробіття (%)", color="red", marker="s")
plt.xlabel("Рік")
plt.ylabel("Безробіття (%)")
plt.legend()
plt.grid(True)

plt.suptitle("Курс долара та рівень безробіття в Україні (2000–2023)")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

max_growth_year = df_long.loc[df_long["GDP_Growth_%"].idxmax(), "Year"]
min_growth_year = df_long.loc[df_long["GDP_Growth_%"].idxmin(), "Year"]

print(f"\nРік з найбільшим приростом ВВП: {max_growth_year}")
print(f"Рік з найменшим приростом ВВП: {min_growth_year}")
