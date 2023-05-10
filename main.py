import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = data["Primary Fur Color"]

black_fur = len(data[fur_color == "Black"])
gray_fur = len(data[fur_color == "Gray"])
cinnamon_fur = len(data[fur_color == "Cinnamon"])


dict_data = {
    "black fur total": [f"{black_fur}"],
    "gray fur total" : [f"{gray_fur}"],
    "cinnamon fur total" : [f"{cinnamon_fur}"]
}

fur_data = pandas.DataFrame(dict_data)
fur_data.to_csv("fur_data.csv")