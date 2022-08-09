import pandas as pd

# Lendo o csv
df = pd.read_csv("nato.csv")

# Criando dicionário NATO
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}


# Recebendo a entrada no usuário e criando uma lista com os valores do dicionário NATO
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)