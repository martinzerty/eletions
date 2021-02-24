from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd 
file = r'/Users/martinc/Downloads/Presidentielle_2017_Resultats_Communes_Tour_2_c.xls'
df = pd.read_excel(file)
print(len(df["Voix"]))
print(df["Voix"][0])
print(df["Voix"][len(df["Voix"])])