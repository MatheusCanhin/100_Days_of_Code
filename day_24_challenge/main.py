# Constante que será substituida
PLACEHOLDER = "[name]"

# Abrindo o arquivo que contem os nomes e criando uma lista com o método readlines
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Abrindo o arquivo que contém a estrutura da carta, percorrendo cada nome na nossa lista de nome, substituindo o
# counteúdo na carta e criando o arquivo com a carta completa.
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        name_stripped = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, name_stripped)
        with open(f"./Output/ReadyToSend/letter_for_{name_stripped}.txt", mode="w") as completed_file:
            completed_file.write(new_letter)
