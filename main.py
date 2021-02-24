from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd 
import time


def get_dict(param,pos_param):
    global y_line
    # manu : pos_param = 22
    # marine : pos_param = 29
    devut = time.time()
    file = r'/Users/martinc/Downloads/Presidentielle_2017_Resultats_Communes_Tour_2_c.xls'
    df = pd.read_excel(file)
    liste_dep = []
    for z in df["Libellé du département"]:
        if z not in liste_dep:
            liste_dep.append(z)

    voix = list()
    longe = len(df[param])
    last = 1
    values = list()

    for x in range(longe):
        dep = df.iloc[x,0]
        if dep == last:
            values.append(df.iloc[x,pos_param])
        else:
            y_line.append(last)
            voix.append(values)
            last = dep
            values = [df.iloc[x,pos_param]]
    voix.append(values)
    dico = {}

    for x in range(len(liste_dep)):
        dico[liste_dep[x]] = voix[x]
    print(len(liste_dep))
    first = list(dico.keys())
    if len(voix) == len(liste_dep):
        print("Good")
    else:
        print(f"Trouble: {len(voix)} != {len(liste_dep)}")
    print(f"Fait en {time.time() - devut} secondes")
    return dico

y_line = []
manu = get_dict("Voix",22)
marine = get_dict("Voix2",29)
if manu == marine:
    print("same")

first_x = []
for x in manu:
    somme = 0
    for y in manu[x]:
        somme = somme + y

    first_x.append(somme)

print(len(y_line) == len(first_x), ':',len(y_line),'vs',len(first_x))
plt.plot(first_x,range(len(y_line)),label = "MACRON")
plt.show()