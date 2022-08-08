# Importando a biblioteca pandas
import pandas as pd

# importando o arquivo csv
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Fazendo a contagem de todos os esquilos, cinzas, pretos e marrons
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# Criando um dicionário com a contagem dos esquilos
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

# criando um dataframe com o dicionário criado e transformando em um arquivo csv
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count")

