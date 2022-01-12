##############################################################
#Ruta del archivo
##############################################################

file = './datasets/Mercado libre/data.csv'

##############################################################
#Lectura básica
##############################################################

# f = open(file, "r")          #abre el archivo en modo lectura
# print(f.read())              #lee n caracteres del archivo. Si no hay parámetro, lee todo el archivo
# print(f)
# print(f.readline())          #lee la siguiente línea del archivo
# print(f.readlines())         #contruye una lista con las líneas del archivo
# f.close()                    #cierra el archivo

##############################################################
#procesamiento de cadenas
##############################################################

# print("-","     hola     ".strip(),"-")          #quita espacios al inicio y al final de la cadena. Versiones lstrip y rstrip
# print("hola,hola, cosa".split(","))              #crea una lista separando la cadena por medio de la coma


##############################################################
#Todo junto
##############################################################

# f = open(file,"r")
# aux = f.readlines()
# for linea in aux:
#     print(linea)
#     columnas = linea.split(",")
#     print(columnas)
# f.close()



##############################################################
#Leer archivos CSV (comma separated values) con python
##############################################################

# import csv
# 
# with open(file, 'r') as f:
#     my_reader = csv.reader(f, delimiter=',')
#     for row in my_reader:
#         print(row)


##############################################################
#Leer archivos CSV (comma separated values) con pandas
##############################################################

import pandas as pd

df = pd.read_csv(file)
# print(type(df))     #es un DataFrame https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(df.head())    #head(n=5) muestra los primeros 5 renglones del dataframe
# print(df.tail())    #tail(n=5) muestra los primeros 5 renglones del dataframe
# print(df.columns)   #lista con nombres de las columnas. Se puede cambiar el nombre de las columnas al asignar otro valor a este atributo
# print(df.shape)     #tupla con número de renglones y número de columnas
# print(df.dtypes)    #tipos de datos de cada columna

# quita los renglones (axis=0) que contienen cualquier (how='any', 'all') columna vacía, inplace significa que modifica el dataframe df
# df.dropna(axis = 0, how = 'any', inplace = True)



#Acceder a valores
# print(df["price"])         #columna completa, tipo Series, también se le puede aplicar operaciones como head o tail
# print(df["price"][0])     #columna e índice
# print(df["price"].unique()) #valores únicos de una columna


##############################################################
#Estadísticos básicos
##############################################################

# columna = df["price"]        #también se puede columna = df.price
# 
# #mean
# print(columna.mean())        #promedio
# 
# #median
# print(columna.median())      #mediana (valor que se encuentra al centro de la lista ordenada de valores)
# 
# #max
# print(columna.max())         #valor máximo
# 
# #min
# print(columna.min())         #valor mínimo
# 
# #std
# print(columna.std())         #desviación estándar, qué tan dispersos están los datos alrededor de la media
#
# #estadísticos básicos en formato de tabla
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(df.describe())



##############################################################
#Histograma
##############################################################

import matplotlib.pyplot as plt       #pandas se apoya en matplotlib para las gráficas

#histograma
# grid boolean, muestra una cuadrícula, default = True
# range tuple, el valor mínimo y máximo para el histograma, lo demás es ignorado, default = None
# cumulative bool o -1, acumula los valores en cada barra, default = None
# orientation string, orientación de las barras, default = "vertical"
# color string, color de las barras, default = None, https://matplotlib.org/stable/gallery/color/named_colors.html

df = df[df["doors"]<=5]

# print(df["doors"].min())
# print(df["doors"].max())

#truco para poner eje de números enteros
# import numpy as np
# bins = np.arange(0, df.doors.max() + 1.5) - 0.5
# bins = np.arange(0, 5 + 1.5) - 0.5
# 
# df.hist(column="doors", bins=bins, grid=False, orientation="horizontal", color = "coral")
# plt.show()



##############################################################
# Cajas y bigotes
##############################################################

# grid boolean, muestra una cuadrícula, default = True
# orientation boolean, orientación de las barras, default = True
# showcaps boolean, muestra líneas al final de los bigotes, default = False
# color string, color de las cajas, default = None, https://matplotlib.org/stable/gallery/color/named_colors.html
# patch_artist boolean, relleno de las cajas, default = False
# showmeans boolean, muestra la media, default = False

# df = df[df.power<275]
# df.boxplot(column=["power"], color = "green", showmeans=True )
# plt.show()


##############################################################
# Correlación
##############################################################

# print(df.corr())      # es un dataframe



##############################################################
# Mapa de calor
##############################################################

import seaborn as sns

# vmin int, valor mínimo de la escala
# vmax int, valor mínimo de la escala
# annot boolean, muestra el valor de la correlación, default = False
# cmap mapa de color, colores usados para el mapa, https://matplotlib.org/stable/gallery/color/colormap_reference.html

# plt.figure(figsize=(15, 5))
# sns.heatmap(df.corr(), annot=True, vmin=0, vmax=1, cmap="cividis");
# plt.show()


# Triángulo
# import numpy as np
# plt.figure(figsize=(15, 5))
# mask = np.triu(np.ones_like(df.corr(), dtype=bool))     # tril para triángulo inferior
# sns.heatmap(df.corr(), mask=mask, vmin=-1, vmax=1, annot=True, cmap='Greens')
# plt.show()


# Observar una sola variable
# plt.figure(figsize=(15, 5))
# column = df.corr()[['price']].sort_values(by='price', ascending=False)
# sns.heatmap(column, vmin=-1, vmax=1, annot=True, cmap='GnBu')
# 
# plt.show()