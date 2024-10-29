#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


defun_98 = pd.read_csv('./datos/DEFUN98.csv')
pd.set_option('display.max_colwidth', None)
defun_98.head()


# In[4]:


#Homologar con diccionario 2020


# In[5]:


#Ocupación
map_ocup = {
    2: 11,
    11: 2,
    12: 2,
    13: 2,
    14: 2,
    21: 1,
    41: 6,
    51: 8,
    52: 8,
    53: 8,
    54: 7,
    55: 8,
    61: 3,
    62: 3,
    71: 4,
    72: 4,
    81: 5,
    82: 5,
    83: 5,
    98: 98,
    99: 99
}
defun_98['OCUPACION'] = defun_98['OCUPACION'].astype(int)
defun_98['OCUPACION'] = defun_98['OCUPACION'].map(map_ocup)

#Sexo
defun_98['SEXO'] = defun_98['SEXO'].replace(3, 9)

#Escolaridad
map_esc = {
    1: 1,
    2: 3,
    3: 3,
    4: 4,
    5: 6,
    6: 8,
    7: 9,
    8: 88,
    9: 99
}

defun_98['ESCOLARIDA'] = defun_98['ESCOLARIDA'].astype(int)
defun_98['ESCOLARIDA'] = defun_98['ESCOLARIDA'].map(map_esc)

#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_98['CAPITULO'] = defun_98.apply(concatenar_capitulo_grupo, axis=1)

# Eliminar la columna 'GRUPO'
defun_98 = defun_98.drop(columns=['GRUPO'])

defun_98


# In[6]:


print(defun_98.columns.to_list())


# In[7]:


#Agregamos columna Area_ur con registro 9: "no especificado"
defun_98['AREA_UR'] = 9
defun_98.head()


# In[8]:


#Defunciones 1999
defun_99 = pd.read_csv('./datos/DEFUN99.csv')
defun_99.head()


# In[9]:


print(defun_99.columns.to_list())


# In[10]:


#Agregamos columna Area_ur con registro 9: "no especificado"
defun_99['AREA_UR'] = 9
defun_99.head()


# In[11]:


#HOMOLOGACIÓN
#OCUPACION
map_ocup = {
    2: 11,
    11: 2,
    12: 2,
    13: 2,
    14: 2,
    21: 1,
    41: 6,
    51: 8,
    52: 8,
    53: 8,
    54: 7,
    55: 8,
    61: 3,
    62: 3,
    71: 4,
    72: 4,
    81: 5,
    82: 5,
    83: 5,
    98: 98,
    99: 99
}
defun_99['OCUPACION'] = defun_99['OCUPACION'].astype(int)
defun_99['OCUPACION'] = defun_99['OCUPACION'].map(map_ocup)

#Sexo
defun_99['SEXO'] = defun_99['SEXO'].replace(3, 9)

#Escolaridad
map_esc = {
    1: 1,
    2: 3,
    3: 3,
    4: 4,
    5: 6,
    6: 8,
    7: 9,
    8: 88,
    9: 99
}

defun_99['ESCOLARIDA'] = defun_99['ESCOLARIDA'].astype(int)
defun_99['ESCOLARIDA'] = defun_99['ESCOLARIDA'].map(map_esc)

#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_99['CAPITULO'] = defun_99.apply(concatenar_capitulo_grupo, axis=1)

# Eliminar la columna 'GRUPO'
defun_99 = defun_99.drop(columns=['GRUPO'])

defun_99


# In[12]:


#Defunciones 2000
defun_00 = pd.read_csv('./datos/DEFUN00.csv')
defun_00.head()


# In[13]:


print(defun_00.columns.to_list())


# In[14]:


#Agregamos columna Area_ur con registro 9: "no especificado"
defun_00['AREA_UR'] = 9
defun_00.head()


# In[15]:


#HOMOLOGACIÓN
#OCUPACION
map_ocup = {
    2: 11,
    11: 2,
    12: 2,
    13: 2,
    14: 2,
    21: 1,
    41: 6,
    51: 8,
    52: 8,
    53: 8,
    54: 7,
    55: 8,
    61: 3,
    62: 3,
    71: 4,
    72: 4,
    81: 5,
    82: 5,
    83: 5,
    98: 98,
    99: 99
}
#defun_00['OCUPACION'] = defun_00['OCUPACION'].astype(int)
defun_00['OCUPACION'] = defun_00['OCUPACION'].map(map_ocup)

#Sexo
defun_00['SEXO'] = defun_00['SEXO'].replace(3, 9)

#Escolaridad
map_esc = {
    1: 1,
    2: 3,
    3: 3,
    4: 4,
    5: 6,
    6: 8,
    7: 9,
    8: 88,
    9: 99
}

defun_00['ESCOLARIDA'] = defun_00['ESCOLARIDA'].astype(int)
defun_00['ESCOLARIDA'] = defun_00['ESCOLARIDA'].map(map_esc)

#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_00['CAPITULO'] = defun_00.apply(concatenar_capitulo_grupo, axis=1)
# Eliminar la columna 'GRUPO'
defun_00 = defun_00.drop(columns=['GRUPO'])

defun_00


# In[17]:


#Defunciones 2001
defun_01 = pd.read_csv('./datos/DEFUN01.csv')
defun_01.head()


# In[18]:


print(defun_01.columns.to_list())


# In[19]:


#Agregamos columna Area_ur con registro 9: "no especificado"
defun_01['AREA_UR'] = 9
defun_01.head()


# In[20]:


#HOMOLOGACIÓN
#OCUPACION
map_ocup = {
    2: 11,
    11: 2,
    12: 2,
    13: 2,
    14: 2,
    21: 1,
    41: 6,
    51: 8,
    52: 8,
    53: 8,
    54: 7,
    55: 8,
    61: 3,
    62: 3,
    71: 4,
    72: 4,
    81: 5,
    82: 5,
    83: 5,
    98: 98,
    99: 99
}
defun_01['OCUPACION'] = defun_01['OCUPACION'].astype(int)
defun_01['OCUPACION'] = defun_01['OCUPACION'].map(map_ocup)

#Sexo
defun_01['SEXO'] = defun_01['SEXO'].replace(3, 9)

#Escolaridad
map_esc = {
    1: 1,
    2: 3,
    3: 3,
    4: 4,
    5: 6,
    6: 8,
    7: 9,
    8: 88,
    9: 99
}

defun_01['ESCOLARIDA'] = defun_01['ESCOLARIDA'].astype(int)
defun_01['ESCOLARIDA'] = defun_01['ESCOLARIDA'].map(map_esc)

#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_01['CAPITULO'] = defun_01.apply(concatenar_capitulo_grupo, axis=1)
# Eliminar la columna 'GRUPO'
defun_01 = defun_01.drop(columns=['GRUPO'])
defun_01


# In[21]:


#Defunciones 2002
defun_02 = pd.read_csv('./datos/DEFUN02.csv')
defun_02.head()


# In[22]:


print(defun_02.columns.to_list())


# In[23]:


#HOMOLOGACIÓN
#OCUPACION
map_ocup = {
    2: 11,
    11: 2,
    12: 2,
    13: 2,
    14: 2,
    21: 1,
    41: 6,
    51: 8,
    52: 8,
    53: 8,
    54: 7,
    55: 8,
    61: 3,
    62: 3,
    71: 4,
    72: 4,
    81: 5,
    82: 5,
    83: 5,
    97: 97,
    98: 98,
    99: 99
}
defun_02['OCUPACION'] = defun_02['OCUPACION'].astype(int)
defun_02['OCUPACION'] = defun_02['OCUPACION'].map(map_ocup)

#Sexo
defun_02['SEXO'] = defun_02['SEXO'].replace(3, 9)

#Escolaridad
map_esc = {
    1: 1,
    2: 3,
    3: 3,
    4: 4,
    5: 6,
    6: 8,
    7: 9,
    8: 88,
    9: 99
}

defun_02['ESCOLARIDA'] = defun_02['ESCOLARIDA'].astype(int)
defun_02['ESCOLARIDA'] = defun_02['ESCOLARIDA'].map(map_esc)

#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_02['CAPITULO'] = defun_02.apply(concatenar_capitulo_grupo, axis=1)
# Eliminar la columna 'GRUPO'
defun_02 = defun_02.drop(columns=['GRUPO'])
defun_02


# In[24]:


#Defunciones 2003
defun_03 = pd.read_csv('./datos/DEFUN03.csv')
defun_03.head()


# In[25]:


print(defun_03.columns.to_list())


# In[26]:


#HOMOLOGACIÓN
#OCUPACION
map_ocup = {
    2: 11,
    11: 2,
    12: 2,
    13: 2,
    14: 2,
    21: 1,
    41: 6,
    51: 8,
    52: 8,
    53: 8,
    54: 7,
    55: 8,
    61: 3,
    62: 3,
    71: 4,
    72: 4,
    81: 5,
    82: 5,
    83: 5,
    97: 97,
    98: 98,
    99: 99
}
defun_03['OCUPACION'] = defun_03['OCUPACION'].astype(int)
defun_03['OCUPACION'] = defun_03['OCUPACION'].map(map_ocup)

#Sexo
defun_03['SEXO'] = defun_03['SEXO'].replace(3, 9)


#Escolaridad
map_esc = {
    1: 1,
    2: 3,
    3: 3,
    4: 4,
    5: 6,
    6: 8,
    7: 9,
    8: 88,
    9: 99
}

defun_03['ESCOLARIDA'] = defun_03['ESCOLARIDA'].astype(int)
defun_03['ESCOLARIDA'] = defun_03['ESCOLARIDA'].map(map_esc)

#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_03['CAPITULO'] = defun_03.apply(concatenar_capitulo_grupo, axis=1)
# Eliminar la columna 'GRUPO'
defun_03 = defun_03.drop(columns=['GRUPO'])

defun_03


# In[27]:


#Defunciones 2004
defun_04 = pd.read_csv('./datos/DEFUN04.csv')
defun_04.head()


# In[28]:


print(defun_04.columns.to_list())


# In[29]:


#HOMOLOGACIÓN
#OCUPACION
map_ocup = {
    2: 11,
    11: 2,
    12: 2,
    13: 2,
    14: 2,
    21: 1,
    41: 6,
    51: 8,
    52: 8,
    53: 8,
    54: 7,
    55: 8,
    61: 3,
    62: 3,
    71: 4,
    72: 4,
    81: 5,
    82: 5,
    83: 5,
    97: 97,
    98: 98,
    99: 99
}
defun_04['OCUPACION'] = defun_04['OCUPACION'].astype(int)
defun_04['OCUPACION'] = defun_04['OCUPACION'].map(map_ocup)

#Sexo
defun_04['SEXO'] = defun_04['SEXO'].replace(3, 9)

#Escolaridad
map_esc = {
    1: 1,
    2: 3,
    3: 3,
    4: 4,
    5: 6,
    6: 8,
    7: 9,
    8: 88,
    9: 99
}

defun_04['ESCOLARIDA'] = defun_04['ESCOLARIDA'].astype(int)
defun_04['ESCOLARIDA'] = defun_04['ESCOLARIDA'].map(map_esc)

#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_04['CAPITULO'] = defun_04.apply(concatenar_capitulo_grupo, axis=1)
# Eliminar la columna 'GRUPO'
defun_04 = defun_04.drop(columns=['GRUPO'])
defun_04


# In[30]:


#Defunciones 2005
defun_05 = pd.read_csv('./datos/DEFUN05.csv', low_memory=False)
defun_05.head()


# In[31]:


print(defun_05.columns.to_list())


# In[32]:


#HOMOLOGACIÓN
#OCUPACION
map_ocup = {
    2: 11,
    11: 2,
    12: 2,
    13: 2,
    14: 2,
    21: 1,
    41: 6,
    51: 8,
    52: 8,
    53: 8,
    54: 7,
    55: 8,
    61: 3,
    62: 3,
    71: 4,
    72: 4,
    81: 5,
    82: 5,
    83: 5,
    97: 97,
    98: 98,
    99: 99
}
defun_05['OCUPACION'] = defun_05['OCUPACION'].astype(int)
defun_05['OCUPACION'] = defun_05['OCUPACION'].map(map_ocup)

#Sexo
defun_05['SEXO'] = defun_05['SEXO'].replace(3, 9)

#Escolaridad
map_esc = {
    1: 1,
    2: 3,
    3: 3,
    4: 4,
    5: 6,
    6: 8,
    7: 9,
    8: 88,
    9: 99
}

defun_05['ESCOLARIDA'] = defun_05['ESCOLARIDA'].astype(int)
defun_05['ESCOLARIDA'] = defun_05['ESCOLARIDA'].map(map_esc)

#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_05['CAPITULO'] = defun_05.apply(concatenar_capitulo_grupo, axis=1)
# Eliminar la columna 'GRUPO'
defun_05 = defun_05.drop(columns=['GRUPO'])

defun_05


# In[33]:


#Defunciones 2006
defun_06 = pd.read_csv('./datos/DEFUN06.csv', low_memory=False)
defun_06.head()


# In[34]:


print(defun_06.columns.to_list())


# In[35]:


#HOMOLOGACIÓN
#OCUPACION
map_ocup = {
    2: 11,
    11: 2,
    12: 2,
    13: 2,
    14: 2,
    21: 1,
    41: 6,
    51: 8,
    52: 8,
    53: 8,
    54: 7,
    55: 8,
    61: 3,
    62: 3,
    71: 4,
    72: 4,
    81: 5,
    82: 5,
    83: 5,
    97: 97,
    98: 98,
    99: 99
}
defun_06['OCUPACION'] = defun_06['OCUPACION'].astype(int)
defun_06['OCUPACION'] = defun_06['OCUPACION'].map(map_ocup)

#Sexo
defun_06['SEXO'] = defun_06['SEXO'].replace(3, 9)

#Escolaridad
map_esc = {
    1: 1,
    2: 3,
    3: 3,
    4: 4,
    5: 6,
    6: 8,
    7: 9,
    8: 88,
    9: 99
}

defun_06['ESCOLARIDA'] = defun_06['ESCOLARIDA'].astype(int)
defun_06['ESCOLARIDA'] = defun_06['ESCOLARIDA'].map(map_esc)

#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_06['CAPITULO'] = defun_06.apply(concatenar_capitulo_grupo, axis=1)
# Eliminar la columna 'GRUPO'
defun_06 = defun_06.drop(columns=['GRUPO'])

defun_06


# In[36]:


#Defunciones 2007
defun_07 = pd.read_csv('./datos/DEFUN07.csv', low_memory=False)
defun_07.head()


# In[37]:


print(defun_07.columns.to_list())


# In[38]:


#HOMOLOGACIÓN
#OCUPACION
map_ocup = {
    2: 11,
    11: 2,
    12: 2,
    13: 2,
    14: 2,
    21: 1,
    41: 6,
    51: 8,
    52: 8,
    53: 8,
    54: 7,
    55: 8,
    61: 3,
    62: 3,
    71: 4,
    72: 4,
    81: 5,
    82: 5,
    83: 5,
    97: 97,
    98: 98,
    99: 99
}
defun_07['OCUPACION'] = defun_07['OCUPACION'].astype(int)
defun_07['OCUPACION'] = defun_07['OCUPACION'].map(map_ocup)

#Sexo
defun_07['SEXO'] = defun_07['SEXO'].replace(3, 9)

#Escolaridad
map_esc = {
    1: 1,
    2: 3,
    3: 3,
    4: 4,
    5: 6,
    6: 8,
    7: 9,
    8: 88,
    9: 99
}

defun_07['ESCOLARIDA'] = defun_07['ESCOLARIDA'].astype(int)
defun_07['ESCOLARIDA'] = defun_07['ESCOLARIDA'].map(map_esc)

#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_07['CAPITULO'] = defun_07.apply(concatenar_capitulo_grupo, axis=1)
# Eliminar la columna 'GRUPO'
defun_07 = defun_07.drop(columns=['GRUPO'])

defun_07


# In[39]:


#Defunciones 2008
defun_08 = pd.read_csv('./datos/DEFUN08.csv', low_memory=False)
defun_08.head()


# In[40]:


print(defun_08.columns.to_list())


# In[41]:


#HOMOLOGACIÓN
#OCUPACION
map_ocup = {
    2: 11,
    11: 2,
    12: 2,
    13: 2,
    14: 2,
    21: 1,
    41: 6,
    51: 8,
    52: 8,
    53: 8,
    54: 7,
    55: 8,
    61: 3,
    62: 3,
    71: 4,
    72: 4,
    81: 5,
    82: 5,
    83: 5,
    97: 97,
    98: 98,
    99: 99
}
defun_08['OCUPACION'] = defun_08['OCUPACION'].astype(int)
defun_08['OCUPACION'] = defun_08['OCUPACION'].map(map_ocup)

#Sexo
defun_08['SEXO'] = defun_08['SEXO'].replace(3, 9)

#Escolaridad
map_esc = {
    1: 1,
    2: 3,
    3: 3,
    4: 4,
    5: 6,
    6: 8,
    7: 9,
    8: 88,
    9: 99
}

defun_08['ESCOLARIDA'] = defun_08['ESCOLARIDA'].astype(int)
defun_08['ESCOLARIDA'] = defun_08['ESCOLARIDA'].map(map_esc)

#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_08['CAPITULO'] = defun_08.apply(concatenar_capitulo_grupo, axis=1)
# Eliminar la columna 'GRUPO'
defun_08 = defun_08.drop(columns=['GRUPO'])

defun_08


# In[42]:


#Defunciones 2009
defun_09 = pd.read_csv('./datos/DEFUN09.csv', low_memory=False)
defun_09.head()


# In[43]:


print(defun_09.columns.to_list())


# In[44]:


#HOMOLOGACIÓN
#OCUPACION
map_ocup = {
    2: 11,
    11: 2,
    12: 2,
    13: 2,
    14: 2,
    21: 1,
    41: 6,
    51: 8,
    52: 8,
    53: 8,
    54: 7,
    55: 8,
    61: 3,
    62: 3,
    71: 4,
    72: 4,
    81: 5,
    82: 5,
    83: 5,
    97: 97,
    98: 98,
    99: 99
}
defun_09['OCUPACION'] = defun_09['OCUPACION'].astype(int)
defun_09['OCUPACION'] = defun_09['OCUPACION'].map(map_ocup)

#Sexo
defun_09['SEXO'] = defun_09['SEXO'].replace(3, 9)

#Escolaridad
map_esc = {
    1: 1,
    2: 3,
    3: 3,
    4: 4,
    5: 6,
    6: 8,
    7: 9,
    8: 88,
    9: 99
}

defun_09['ESCOLARIDA'] = defun_09['ESCOLARIDA'].astype(int)
defun_09['ESCOLARIDA'] = defun_09['ESCOLARIDA'].map(map_esc)

#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_09['CAPITULO'] = defun_09.apply(concatenar_capitulo_grupo, axis=1)
# Eliminar la columna 'GRUPO'
defun_09 = defun_09.drop(columns=['GRUPO'])

defun_09


# In[45]:


#Defunciones 2010
defun_10 = pd.read_csv('./datos/DEFUN10.csv', low_memory=False)
defun_10.head()


# In[46]:


print(defun_10.columns.to_list())


# In[47]:


#HOMOLOGACIÓN
#OCUPACION
map_ocup = {
    2: 11,
    11: 2,
    12: 2,
    13: 2,
    14: 2,
    21: 1,
    41: 6,
    51: 8,
    52: 8,
    53: 8,
    54: 7,
    55: 8,
    61: 3,
    62: 3,
    71: 4,
    72: 4,
    81: 5,
    82: 5,
    83: 5,
    97: 97,
    98: 98,
    99: 99
}
defun_10['OCUPACION'] = defun_10['OCUPACION'].astype(int)
defun_10['OCUPACION'] = defun_10['OCUPACION'].map(map_ocup)

#Sexo
defun_10['SEXO'] = defun_10['SEXO'].replace(3, 9)

#Escolaridad
map_esc = {
    1: 1,
    2: 3,
    3: 3,
    4: 4,
    5: 6,
    6: 8,
    7: 9,
    8: 88,
    9: 99
}

defun_10['ESCOLARIDA'] = defun_10['ESCOLARIDA'].astype(int)
defun_10['ESCOLARIDA'] = defun_10['ESCOLARIDA'].map(map_esc)

#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_10['CAPITULO'] = defun_10.apply(concatenar_capitulo_grupo, axis=1)
# Eliminar la columna 'GRUPO'
defun_10 = defun_10.drop(columns=['GRUPO'])

defun_10


# In[48]:


#Defunciones 2011
defun_11 = pd.read_csv('./datos/DEFUN11.csv', low_memory=False)
defun_11.head()


# In[49]:


print(defun_11.columns.to_list())


# In[50]:


#HOMOLOGACIÓN
#OCUPACION
map_ocup = {
    2: 11,
    11: 2,
    12: 2,
    13: 2,
    14: 2,
    21: 1,
    41: 6,
    51: 8,
    52: 8,
    53: 8,
    54: 7,
    55: 8,
    61: 3,
    62: 3,
    71: 4,
    72: 4,
    81: 5,
    82: 5,
    83: 5,
    97: 97,
    98: 98,
    99: 99
}
defun_11['OCUPACION'] = defun_11['OCUPACION'].astype(int)
defun_11['OCUPACION'] = defun_11['OCUPACION'].map(map_ocup)

#Sexo
defun_11['SEXO'] = defun_11['SEXO'].replace(3, 9)

#Escolaridad
map_esc = {
    1: 1,
    2: 3,
    3: 3,
    4: 4,
    5: 6,
    6: 8,
    7: 9,
    8: 88,
    9: 99
}

defun_11['ESCOLARIDA'] = defun_11['ESCOLARIDA'].astype(int)
defun_11['ESCOLARIDA'] = defun_11['ESCOLARIDA'].map(map_esc)

#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_11['CAPITULO'] = defun_11.apply(concatenar_capitulo_grupo, axis=1)
# Eliminar la columna 'GRUPO'
defun_11 = defun_11.drop(columns=['GRUPO'])

defun_11


# In[51]:


#Defunciones 2012
defun_12 = pd.read_csv('./datos/DEFUN12.csv', low_memory=False)
defun_12.head()




# In[52]:


print(defun_12.columns.to_list())


# In[53]:


#HOMOLOGACIÓN
#OCUPACION
map_ocup = {
    2: 11,
    11: 2,
    12: 2,
    13: 2,
    14: 2,
    21: 1,
    41: 6,
    51: 8,
    52: 8,
    53: 8,
    54: 7,
    55: 8,
    61: 3,
    62: 3,
    71: 4,
    72: 4,
    81: 5,
    82: 5,
    83: 5,
    97: 97,
    98: 98,
    99: 99
}
defun_12['OCUPACION'] = defun_12['OCUPACION'].astype(int)
defun_12['OCUPACION'] = defun_12['OCUPACION'].map(map_ocup)

#Sexo
defun_12['SEXO'] = defun_12['SEXO'].replace(3, 9)

#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_12['CAPITULO'] = defun_12.apply(concatenar_capitulo_grupo, axis=1)
# Eliminar la columna 'GRUPO'
defun_12 = defun_12.drop(columns=['GRUPO'])

defun_12


# In[54]:


#Defunciones 2013
defun_13 = pd.read_csv('./datos/DEFUN13.csv', low_memory=False)
defun_13.columns = defun_13.columns.str.upper()
defun_13.head()


# In[55]:


print(defun_13.columns.to_list())


# In[56]:


#HOMOLOGACIÓN
#OCUPACION
#map_ocup = {
 #   2: 11,
 #  11: 2,
 #   12: 2,
 #   13: 2,
 #   14: 2,
 #   21: 1,
 #   41: 6,
 #   51: 8,
 #   52: 8,
 #   53: 8,
 #   54: 7,
 #   55: 8,
 #   61: 3,
 #   62: 3,
 #   71: 4,
 #   72: 4,
 #   81: 5,
 #   82: 5,
 #   83: 5,
 #   97: 97,
 #   98: 98,
 #   99: 99
#}
#defun_13['OCUPACION'] = defun_13['OCUPACION'].astype(int)
#defun_13['OCUPACION'] = defun_13['OCUPACION'].map(map_ocup)

#Diccionario 2020 para ocupación

#Sexo
defun_13['SEXO'] = defun_13['SEXO'].replace(3, 9)

#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_13['CAPITULO'] = defun_13.apply(concatenar_capitulo_grupo, axis=1)
# Eliminar la columna 'GRUPO'
defun_13 = defun_13.drop(columns=['GRUPO'])
defun_13


# In[58]:


#Defunciones 2014
defun_14 = pd.read_csv('./datos/DEFUN14.csv', low_memory=False)
defun_14.columns = defun_14.columns.str.upper()

#homologar
#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_14['CAPITULO'] = defun_14.apply(concatenar_capitulo_grupo, axis=1)

defun_14.head()


# In[59]:


print(defun_14.columns.to_list())


# In[60]:


#Defunciones 2015
defun_15 = pd.read_csv('./datos/DEFUN15.csv', low_memory=False)
defun_15.columns = defun_15.columns.str.upper()
#homologar
#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_15['CAPITULO'] = defun_15.apply(concatenar_capitulo_grupo, axis=1)
defun_15.head()


# In[61]:


print(defun_15.columns.to_list())


# In[62]:


#Defunciones 2016
defun_16 = pd.read_csv('./datos/DEFUN16.csv', low_memory=False)
defun_16.columns = defun_16.columns.str.upper()

#homologar
#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_16['CAPITULO'] = defun_16.apply(concatenar_capitulo_grupo, axis=1)

defun_16.head()


# In[63]:


print(defun_16.columns.to_list())


# In[64]:


#Defunciones 2017
defun_17 = pd.read_csv('./datos/DEFUN17.csv', low_memory=False)

#homologar
#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_17['CAPITULO'] = defun_17.apply(concatenar_capitulo_grupo, axis=1)

defun_17.head()


# In[65]:


print(defun_17.columns.to_list())


# In[66]:


#Defunciones 2018
defun_18 = pd.read_csv('./datos/DEFUN18.csv', low_memory=False)

#homologar
#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_18['CAPITULO'] = defun_18.apply(concatenar_capitulo_grupo, axis=1)

defun_18.head()


# In[67]:


print(defun_18.columns.to_list())


# In[68]:


#Defunciones 2019
defun_19 = pd.read_csv('./datos/DEFUN19.csv', low_memory=False)
defun_19.columns = defun_19.columns.str.upper()

defun_19.head()


# In[69]:


print(defun_19.columns.to_list())


# In[70]:


#HOMOLOGACIÓN


#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_19['CAPITULO'] = defun_19.apply(concatenar_capitulo_grupo, axis=1)
# Eliminar la columna 'GRUPO'
defun_19 = defun_19.drop(columns=['GRUPO'])

defun_19


# In[71]:


#Defunciones 2020
defun_20 = pd.read_csv('./datos/DEFUN20.csv', low_memory=False)
defun_20.columns = defun_20.columns.str.upper()
defun_20.head()


# In[72]:


print(defun_20.columns.to_list())


# In[73]:


#HOMOLOGACIÓN


#Capitulo
def concatenar_capitulo_grupo(row):
    capitulo = str(row['CAPITULO'])
    grupo = str(row['GRUPO'])
    if row['GRUPO'] < 10:
        return int(capitulo + '0' + grupo)
    else:
        return int(capitulo + grupo)

# Aplicar la función al DataFrame
defun_20['CAPITULO'] = defun_20.apply(concatenar_capitulo_grupo, axis=1)
# Eliminar la columna 'GRUPO'
defun_20 = defun_20.drop(columns=['GRUPO'])

defun_20


# In[76]:


#Defunciones 2021
defun_21 = pd.read_csv('./datos/DEFUN21.csv', low_memory=False, encoding='UTF-8')
defun_21.columns = defun_21.columns.str.upper()
defun_21.head()


# In[77]:


columnasdeseadas = [
    'ENTIDADRESIDENCIA', 'MUNICIPIORESIDENCIA', 'LOCALIDADRESIDENCIA', 
    'ENTIDADDEFUNCION', 'MUNICIPIODEFUNCION', 'SEXO', 'ANIO', 'CLAVEOCUPACIONHABITUAL', 'ESCOLARIDADD', 'CODIGOCIECAUSA_A_1', 'EDAD'
]
defun_21 = defun_21[columnasdeseadas]

defun_21.head()


# In[78]:


# Homologando Escolaridad
print(defun_21['ESCOLARIDADD'].unique())


# In[79]:


diccionario_escolaridad = {
    'NINGUNA': 1,
    'PREESCOLAR COMPLETA': 2,
    'PRIMARIA INCOMPLETA': 3,
    'PRIMARIA COMPLETA': 4,
    'SECUNDARIA INCOMPLETA': 5,
    'SECUNDARIA COMPLETA': 6,
    'BACHILLERATO O PREPARATORIA INCOMPLETA': 7,
    'BACHILLERATO O PREPARATORIA COMPLETA': 8,
    'LICENCIATURA O PROFESIONAL INCOMPLETO': 7,  
    'LICENCIATURA O PROFESIONAL COMPLETO': 9,
    'POSGRADO COMPLETO': 10,
    'NO APLICA': 88,
    'SE IGNORA': 99,
    'NO ESPECIFICADO': 99
}
defun_21['ESCOLARIDADD'] = defun_21['ESCOLARIDADD'].map(diccionario_escolaridad)


# In[80]:


print(defun_21['ESCOLARIDADD'].unique())


# In[81]:


# Homologando ocupación
def transformar_clave_ocupacion(valor):
    if valor == 0:
        return 99
    elif valor in [1, 2, 3, 4]:
        return 11
    elif valor > 10:
        return int(str(valor)[0])  
    else:
        return valor 

defun_21['CLAVEOCUPACIONHABITUAL'] = defun_21['CLAVEOCUPACIONHABITUAL'].apply(transformar_clave_ocupacion)

defun_21[['CLAVEOCUPACIONHABITUAL']].head()


# In[82]:


defun_21.head()


# In[83]:


causaDef = pd.read_csv('diccionarios/causa_defuncion.csv')
causaDef.head()


# In[84]:


capitulo = pd.read_csv('diccionarios/capitulo_grupo.csv')
capitulo.head()


# In[85]:


defun_21['CODIGOCIECAUSA_A_1'] = defun_21['CODIGOCIECAUSA_A_1'].str[:3]


# In[86]:


defun_21.head()


# In[87]:


capitulo_data = pd.read_csv('diccionarios/capitulo_grupo2.csv')
capitulo_data.head()


# In[88]:


import re
def buscar_descripcion(codigo):
    """Busca la descripción y devuelve el grupo y capítulo si hay un match en la descripción."""
    letra = codigo[0]  
    numero = int(codigo[1:])  

    for index, row in capitulo_data.iterrows():
        descripcion = row['DESCRIP']
        match = re.match(r'([A-Z])(\d{2})-([A-Z])(\d{2})', descripcion)
        
        if match:
            inicio_letra, inicio_numero, fin_letra, fin_numero = match.groups()
            inicio_numero = int(inicio_numero)
            fin_numero = int(fin_numero)
            # Verifica si la letra coincide
            if letra == inicio_letra or letra == fin_letra or (inicio_letra < letra < fin_letra):
                # Luego verifica si el número está en el rango correspondiente
                if (letra == inicio_letra and numero >= inicio_numero) and \
                   (letra == fin_letra and numero <= fin_numero) and \
                   (inicio_letra < letra < fin_letra) or \
                   (inicio_letra == fin_letra and inicio_numero <= numero <= fin_numero):
                    return int(row['GPO']), int(row['CAP'])  # Retorna la coincidencia

    return None, None  


# In[89]:


defun_21[['GRUPO', 'CAPITULO']] = defun_21['CODIGOCIECAUSA_A_1'].apply(buscar_descripcion).apply(pd.Series)


# In[90]:


defun_21


# In[91]:


defun_21.info()


# In[92]:


filas_nan_capitulo = defun_21[defun_21['CAPITULO'].isna()]
filas_nan_capitulo


# In[93]:


defun_21['GRUPO'] = defun_21['GRUPO'].fillna(8)
defun_21['CAPITULO'] = defun_21['CAPITULO'].fillna(18)
filas_nan_capitulo = defun_21[defun_21['CAPITULO'].isna()]
filas_nan_capitulo


# In[94]:


def concatenar_capitulo_grupo(row):
    capitulo = int(row['CAPITULO'])  # Convertir CAPITULO a entero
    grupo = int(row['GRUPO'])  # Convertir GRUPO a entero
    
    # Si el grupo es menor a 10, se le agrega un 0 adelante
    if grupo < 10:
        return int(f"{capitulo}0{grupo}")
    else:
        return int(f"{capitulo}{grupo}")

# Aplicar la función
defun_21['CAPITULO'] = defun_21.apply(concatenar_capitulo_grupo, axis=1)

# Eliminar la columna 'GRUPO'
defun_21 = defun_21.drop(columns=['GRUPO'])

defun_21


# In[95]:


print(defun_21['EDAD'].unique())


# In[96]:


bins = [-1, 0, 1, 2, 3, 4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 84, 89, 94, 99, 104, 109, 114, 119, 200]

cve_labels = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29 
]

defun_21['EDAD_AGRU'] = pd.cut(defun_21['EDAD'], bins=bins, labels=cve_labels, right=True)

defun_21


# In[97]:


# Cambiar los nombres de las columnas
defun_21 = defun_21.rename(columns={
    'ENTIDADRESIDENCIA': 'ENT_RESID',
    'MUNICIPIORESIDENCIA': 'MUN_RESID',
    'ENTIDADDEFUNCION': 'ENT_OCURR',
    'MUNICIPIODEFUNCION': 'MUN_OCURR',
    'SEXO': 'SEXO',  
    'ANIO': 'ANIO_OCUR',
    'CLAVEOCUPACIONHABITUAL': 'OCUPACION',
    'ESCOLARIDADD': 'ESCOLARIDA',
    'EDAD': 'EDAD',  
    'EDAD_AGRU': 'EDAD_AGRU',  
    'CAPITULO': 'CAPITULO' 
})

defun_21


# In[98]:


#Defunciones 2022
defun_22 = pd.read_csv('./datos/DEFUN22.csv', low_memory=False, encoding='UTF-8')
defun_22.columns = defun_22.columns.str.upper()
defun_22.head()


# In[99]:


columnasdeseadas = [
    'ENTIDADRESIDENCIA', 'MUNICIPIORESIDENCIA', 'LOCALIDADRESIDENCIA', 
    'ENTIDADDEFUNCION', 'MUNICIPIODEFUNCION', 'SEXO', 'ANIO', 'CLAVEOCUPACIONHABITUAL', 'ESCOLARIDADD', 'CODIGOCIECAUSA_A_1', 'EDAD'
]
defun_22 = defun_22[columnasdeseadas]

defun_22.head()


# In[100]:


# Homologando Escolaridad
print(defun_22['ESCOLARIDADD'].unique())


# In[101]:


diccionario_escolaridad = {
    'NINGUNA': 1,
    'PREESCOLAR COMPLETA': 2,
    'PRIMARIA INCOMPLETA': 3,
    'PRIMARIA COMPLETA': 4,
    'SECUNDARIA INCOMPLETA': 5,
    'SECUNDARIA COMPLETA': 6,
    'BACHILLERATO O PREPARATORIA INCOMPLETA': 7,
    'BACHILLERATO O PREPARATORIA COMPLETA': 8,
    'LICENCIATURA O PROFESIONAL INCOMPLETO': 7,  
    'LICENCIATURA O PROFESIONAL COMPLETO': 9,
    'POSGRADO COMPLETO': 10,
    'NO APLICA': 88,
    'SE IGNORA': 99,
    'NO ESPECIFICADO': 99
}
defun_22['ESCOLARIDADD'] = defun_22['ESCOLARIDADD'].map(diccionario_escolaridad)


# In[102]:


# Homologando ocupación
def transformar_clave_ocupacion(valor):
    if valor == 0:
        return 99
    elif valor in [1, 2, 3, 4]:
        return 11
    elif valor > 10:
        return int(str(valor)[0])  
    else:
        return valor 

defun_22['CLAVEOCUPACIONHABITUAL'] = defun_22['CLAVEOCUPACIONHABITUAL'].apply(transformar_clave_ocupacion)

defun_22[['CLAVEOCUPACIONHABITUAL']].head()


# In[103]:


defun_22['CODIGOCIECAUSA_A_1'] = defun_22['CODIGOCIECAUSA_A_1'].str[:3]


# In[104]:


capitulo_data = pd.read_csv('diccionarios/capitulo_grupo2.csv')
capitulo_data.head()


# In[105]:


defun_22[['GRUPO', 'CAPITULO']] = defun_22['CODIGOCIECAUSA_A_1'].apply(buscar_descripcion).apply(pd.Series)


# In[106]:


filas_nan_capitulo = defun_22[defun_22['CAPITULO'].isna()]
filas_nan_capitulo


# In[107]:


defun_22['GRUPO'] = defun_22['GRUPO'].fillna(8)
defun_22['CAPITULO'] = defun_22['CAPITULO'].fillna(18)
filas_nan_capitulo = defun_22[defun_22['CAPITULO'].isna()]
filas_nan_capitulo


# In[108]:


def concatenar_capitulo_grupo(row):
    capitulo = int(row['CAPITULO'])  # Convertir CAPITULO a entero
    grupo = int(row['GRUPO'])  # Convertir GRUPO a entero
    
    # Si el grupo es menor a 10, se le agrega un 0 adelante
    if grupo < 10:
        return int(f"{capitulo}0{grupo}")
    else:
        return int(f"{capitulo}{grupo}")

# Aplicar la función
defun_22['CAPITULO'] = defun_22.apply(concatenar_capitulo_grupo, axis=1)

# Eliminar la columna 'GRUPO'
defun_22 = defun_22.drop(columns=['GRUPO'])

defun_22


# In[109]:


bins = [-1, 0, 1, 2, 3, 4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 84, 89, 94, 99, 104, 109, 114, 119, 200]

cve_labels = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29 
]

defun_22['EDAD_AGRU'] = pd.cut(defun_22['EDAD'], bins=bins, labels=cve_labels, right=True)

defun_22


# In[110]:


# Cambiar los nombres de las columnas
defun_22 = defun_22.rename(columns={
    'ENTIDADRESIDENCIA': 'ENT_RESID',
    'MUNICIPIORESIDENCIA': 'MUN_RESID',
    'ENTIDADDEFUNCION': 'ENT_OCURR',
    'MUNICIPIODEFUNCION': 'MUN_OCURR',
    'SEXO': 'SEXO',  
    'ANIO': 'ANIO_OCUR',
    'CLAVEOCUPACIONHABITUAL': 'OCUPACION',
    'ESCOLARIDADD': 'ESCOLARIDA',
    'EDAD': 'EDAD',  
    'CAPITULO': 'CAPITULO', 
    'EDAD_AGRU': 'EDAD_AGRU',  
})

defun_22


# In[111]:


#Defunciones 2023
defun_23 = pd.read_csv('./datos/DEFUN23.csv', low_memory=False, encoding='UTF-8')
defun_23.columns = defun_23.columns.str.upper()
defun_23.head()


# In[112]:


columnasdeseadas = [
    'ENTIDADRESIDENCIA', 'MUNICIPIORESIDENCIA', 'LOCALIDADRESIDENCIA', 
    'ENTIDADDEFUNCION', 'MUNICIPIODEFUNCION', 'SEXO', 'ANIO', 'CLAVEOCUPACIONHABITUAL', 'ESCOLARIDADD', 'CODIGOCIECAUSA_A_1', 'EDAD'
]
defun_23 = defun_23[columnasdeseadas]

defun_23.head()


# In[113]:


# Homologando Escolaridad
print(defun_23['ESCOLARIDADD'].unique())


# In[114]:


diccionario_escolaridad = {
    'NINGUNA': 1,
    'PREESCOLAR COMPLETA': 2,
    'PRIMARIA INCOMPLETA': 3,
    'PRIMARIA COMPLETA': 4,
    'SECUNDARIA INCOMPLETA': 5,
    'SECUNDARIA COMPLETA': 6,
    'BACHILLERATO O PREPARATORIA INCOMPLETA': 7,
    'BACHILLERATO O PREPARATORIA COMPLETA': 8,
    'LICENCIATURA O PROFESIONAL INCOMPLETO': 7,  
    'LICENCIATURA O PROFESIONAL COMPLETO': 9,
    'POSGRADO COMPLETO': 10,
    'NO APLICA': 88,
    'SE IGNORA': 99,
    'NO ESPECIFICADO': 99
}
defun_23['ESCOLARIDADD'] = defun_23['ESCOLARIDADD'].map(diccionario_escolaridad)


# In[115]:


# Homologando ocupación
def transformar_clave_ocupacion(valor):
    if valor == 0:
        return 99
    elif valor in [1, 2, 3, 4]:
        return 11
    elif valor > 10:
        return int(str(valor)[0])  
    else:
        return valor 

defun_23['CLAVEOCUPACIONHABITUAL'] = defun_23['CLAVEOCUPACIONHABITUAL'].apply(transformar_clave_ocupacion)

defun_23[['CLAVEOCUPACIONHABITUAL']].head()


# In[116]:


defun_23['CODIGOCIECAUSA_A_1'] = defun_23['CODIGOCIECAUSA_A_1'].str[:3]


# In[117]:


defun_23[['GRUPO', 'CAPITULO']] = defun_23['CODIGOCIECAUSA_A_1'].apply(buscar_descripcion).apply(pd.Series)


# In[118]:


defun_23['GRUPO'] = defun_23['GRUPO'].fillna(8)
defun_23['CAPITULO'] = defun_23['CAPITULO'].fillna(18)
filas_nan_capitulo = defun_23[defun_23['CAPITULO'].isna()]
filas_nan_capitulo


# In[119]:


def concatenar_capitulo_grupo(row):
    capitulo = int(row['CAPITULO'])  # Convertir CAPITULO a entero
    grupo = int(row['GRUPO'])  # Convertir GRUPO a entero
    
    # Si el grupo es menor a 10, se le agrega un 0 adelante
    if grupo < 10:
        return int(f"{capitulo}0{grupo}")
    else:
        return int(f"{capitulo}{grupo}")

# Aplicar la función
defun_23['CAPITULO'] = defun_23.apply(concatenar_capitulo_grupo, axis=1)

# Eliminar la columna 'GRUPO'
defun_23 = defun_23.drop(columns=['GRUPO'])

defun_23


# In[120]:


bins = [-1, 0, 1, 2, 3, 4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 84, 89, 94, 99, 104, 109, 114, 119, 200]

cve_labels = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29 
]

defun_23['EDAD_AGRU'] = pd.cut(defun_23['EDAD'], bins=bins, labels=cve_labels, right=True)

defun_23


# In[121]:


# Cambiar los nombres de las columnas
defun_23 = defun_23.rename(columns={
    'ENTIDADRESIDENCIA': 'ENT_RESID',
    'MUNICIPIORESIDENCIA': 'MUN_RESID',
    'ENTIDADDEFUNCION': 'ENT_OCURR',
    'MUNICIPIODEFUNCION': 'MUN_OCURR',
    'SEXO': 'SEXO',  
    'ANIO': 'ANIO_OCUR',
    'CLAVEOCUPACIONHABITUAL': 'OCUPACION',
    'ESCOLARIDADD': 'ESCOLARIDA',
    'EDAD': 'EDAD',  
    'EDAD_AGRU': 'EDAD_AGRU',  
    'CAPITULO': 'CAPITULO'  
})

defun_23


# In[122]:


#Combinar dataset

dataframes = [defun_98, defun_99, defun_00, defun_01, defun_02, defun_03, defun_04, defun_05, defun_06, defun_07, defun_08, defun_09, defun_10, defun_11, defun_12,
             defun_13, defun_14, defun_15, defun_16, defun_17, defun_18, defun_19, defun_20, defun_21, defun_22, defun_23] 

columnas_deseadas = [
    'ENT_RESID', 'MUN_RESID', 'ENT_OCURR', 'MUN_OCURR', 'SEXO', 'ANIO_OCUR', 'OCUPACION', 'ESCOLARIDA', 'CAPITULO', 'EDAD_AGRU'
]

dataframes_filtrados = [df[columnas_deseadas] for df in dataframes]

defun = pd.concat(dataframes_filtrados, ignore_index=True)

defun['OCUPACION'] = defun['OCUPACION'].astype(int)

defun


# In[123]:


#Diccionario de municipios
dmun = pd.read_csv('dmun.csv', low_memory=False, encoding='latin1')
dmun


# In[124]:


#Eliminar columna cve_loc
dmun = dmun.drop(columns=['CVE_LOC'])
dmun


# In[125]:


#Solo cve_ent = 20 : Oaxaca
dmun = dmun.query('CVE_ENT == 20')
dmun


# In[126]:


#Eliminando duplicados
dmun = dmun.drop_duplicates(subset=['CVE_MUN'], keep='first')
dmun


# In[127]:


#Csv de Oaxaca
defun_oaxaca = defun.query('ENT_RESID == 20')
defun_oaxaca.to_csv('defun_oaxaca.csv', index=False)
defun_oaxaca


# In[128]:


#Solo los municipios de la subcuenca
mun_subcuenca2 = [
    "San Andrés Zautla", "Santiago Suchilquitongo", "Reyes Etla", "Magdalena Apasco", "San Pablo Huitzo",
    "Nazareno Etla", "San Lorenzo Cacaotepec", "Soledad Etla", "Guadalupe Etla", "San Francisco Telixtlahuaca",
    "Oaxaca de Juárez", "San Jacinto Amilpas", "Santa María Atzompa", "Villa de Etla", "Tlalixtac de Cabrera",
    "San Antonio de la Cal", "Santa Cruz Amilpas", "Santa María del Tule", "Santa Lucía del Camino", "San Sebastián Tutla",
    "Rojas de Cuauhtémoc", "San Juan Guelavía", "San Sebastián Abasolo", "Santa Cruz Papalutla", "Santa María Guelacé",
    "San Pablo Villa de Mitla", "Tlacolula de Matamoros", "Santa Cruz Xoxocotlán", "San Agustín de las Juntas",
    "Santa María Coyotepec", "Ánimas Trujano", "San Bartolo Coyotepec", "Santa Ana Zegache", "Villa de Zaachila",
    "San Pablo Huixtepec", "Santa Catarina Quiané", "Ciénega de Zimatlán", "Zimatlán de Álvarez"
]
mun_subcuenca =[
 'Heroica Ciudad de Ejutla de Crespo',
 'Magdalena Mixtepec',
 'Magdalena Teitipac',
 'Nuevo Zoquiápam',
 'Oaxaca de Juárez',
 'Ocotlán de Morelos',
 'San Andrés Zautla',
 'San Antonino el Alto',
 'San Bartolomé Quialana',
 'San Bernardo Mixtepec',
 'San Felipe Tejalápam',
 'San Francisco Telixtlahuaca',
 'San Jerónimo Taviche',
 'San José del Progreso',
 'San Juan del Estado',
 'San Juan Teitipac',
 'San Lorenzo Albarradas',
 'San Lucas Quiaviní',
 'San Miguel Mixtepec',
 'San Miguel Tilquiápam',
 'San Pablo Cuatro Venados',
 'San Pablo Huitzo',
 'San Pablo Villa de Mitla',
 'Santa Ana Tlapacoyan',
 'Santa Catarina Ixtepeji',
 'Santa Cruz Mixtepec',
 'Santa Lucía del Camino',
 'Santa María Peñoles',
 'Santiago Matatlán',
 'Santiago Suchilquitongo',
 'Santiago Tenango',
 'Santo Tomás Mazaltepec',
 'Teococuilco de Marcos Pérez',
 'Teotitlán del Valle',
 'Tlacolula de Matamoros',
 'Tlalixtac de Cabrera',
 'Villa Díaz Ordaz',
 'Zimatlán de Álvarez'
]

dmun = dmun[dmun['NOM_LOC'].isin(mun_subcuenca)]

dmun.to_csv('diccionario_mun_subcuenca.csv', index=False)
dmun


# In[129]:


#Deben ser 38 municipios
dmun.shape


# In[130]:


# Eliminamos datos de defunciones no pertenecientes a los años 1998-2020 tales como 1900, 1956, 9999
defun_filtered = defun[(defun['ANIO_OCUR'] >= 1998) & (defun['ANIO_OCUR'] <= 2023)]

# Verificar los datos filtrados
print(defun_filtered['ANIO_OCUR'].unique())


# In[131]:


#Filtrar el df para obtener los resultados de defunciones de residentes de los municipios de la subcuenca
dmun.rename(columns={'CVE_ENT': 'ENT_RESID', 'CVE_MUN': 'MUN_RESID'}, inplace=True)
#merge
defun_subcuenca = pd.merge(defun_filtered, dmun[['ENT_RESID', 'MUN_RESID']], on=['ENT_RESID', 'MUN_RESID'], how='inner')
defun_subcuenca.head()


# In[132]:


#Convertir el df a csv
defun_subcuenca.to_csv('defun_subcuenca.csv', index=False)


# In[133]:


print(defun_subcuenca['CAPITULO'].unique())


# In[ ]:




