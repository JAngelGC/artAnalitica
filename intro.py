
import numpy as np
import pandas as pd

# %% 
print("Hello world")

# %%

lista = [1,2,4,6]
nplista = np.array(lista)
pdlista = pd.Series(lista)

# print(lista * 10)
# print(nplista * 2)
# print(pdlista * 2)


df = pd.read_csv("insurance.csv")


# print(df)
# print("\n-----------\n")
# print(df.head()) # puedes poner cuantos elementos en el head
# print("\n-----------\n")
# print(df.tail())
# print("\n-----------\n")
# print(df.sample(10))
print("\n-----------\n")



# print(df.describe())
# print("\n-----------\n")
# print(df.info())


# print(df['age'])
# print("\n-----------\n")
# print(df[['age']])
# print("\n-----------\n")
# print(df[['age', 'bmi']].head())
# print("\n-----------\n")
# print(df[:3])



# print(df.tail(3))
# print("\n-----------\n")
# print(df[['age', 'bmi']].head(2))
# print("\n-----------\n")
# print(df[10:11])
# print("\n-----------\n")
# print(df['age'][10])



print("\n-----------\n")
print(df[['bmi', 'age']].mean())
print("\n-----------\n")
print(df['age'].mean())
print("\n-----------\n")
print(df['age'].quantile([0.25, 0.50, 0.75]))
print("\n-----------\n")
print(df[['age', 'bmi']].mode())


