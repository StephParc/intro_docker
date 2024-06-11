import pandas as pd

elem_list = []

while len(elem_list) < 4:
    element = input("Que voulez-vous ajouter à votre liste de courses? ")
    elem_list.append(element)

df = pd.DataFrame(elem_list, columns=["number"])

print("Votre liste de courses: ")
print(df)
