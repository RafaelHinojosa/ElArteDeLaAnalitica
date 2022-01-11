"""
    Autor: Rafael Hinojosa López
    Fecha: 11 - Ene - 2022
"""

import numpy as np
import pandas as pd
from pandas.core.algorithms import unique 

# 1. Cargar los datos
songs = pd.read_csv("songs.csv")

# 2. Número de variables y registros
noRegistros = songs.shape[0]
noVariables = songs.shape[1]
print('Número de Registros: ' + str(noRegistros))
print('Número de Variables: ' + str(noVariables))

# 3. Mostrar nombre de las columnas
print('\nColumnas:')
print(songs.columns)

# 4. Mostrar tipos de datos
print('\nTipos de datos:')
print(songs.dtypes)

# 5. Seleccionar dos columnas (key, tempo)
keys = songs['key']
tempos = songs['tempo']

print('\n---- Keys ----')
# Key - Unique
uniqueKeys = keys.unique()
uniqueKeys.sort()
print('\nUnique Keys:')
print(uniqueKeys)

# Key - Max and Min
print('\nMinKey: ' + str(uniqueKeys.min()))
print('MaxKey: ' + str(uniqueKeys.max()))

# Key - Mean, Median, Standard Deviation
print('\nMean Key: ' + str(keys.mean()))
print('Median Key: ' + str(keys.median()))
print('Std Deviation of Keys: ' + str(keys.std()))

print('\n---- Tempos ----')
# Tempo - Unique
uniqueTempos = tempos.unique()
uniqueTempos.sort()
print('\nUnique Tempos:')
print(uniqueTempos)

# Tempo - Max and Min
print('\nMinTempo: ' + str(uniqueTempos.min()))
print('MaxTempo: ' + str(uniqueTempos.max()))

# Tempo - Mean, Median, Standard Deviation
print('\nMean Tempo: ' + str(tempos.mean()))
print('Median Tempo: ' + str(tempos.median()))
print('Std Deviation Tempo: ' + str(tempos.std()))