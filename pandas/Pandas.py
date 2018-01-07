
# coding: utf-8

# # Se importa la librería pandas como pd

# In[12]:


import pandas as pd


# # Se extrae los datos del archivo wine_data.csv y se define el nombre de las columnas.

# In[13]:


wine = pd.read_csv('wine_data.csv', names = ["Cultivator", "Alchol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium", "Total_phenols", "Falvanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280", "Proline"])


# # Se muestra los primeros datos

# In[14]:


wine.head()


# # Se muestra las dimensiones de la tabla de los datos

# In[15]:


wine.shape


# # Se muestra las 2 primeras filas de la tabla

# In[16]:


wine.loc[[0,1]]


# # Se muestra las dos primeras filas y las columnas Cultivator y Alchol.

# In[17]:


wine.loc[[0,1]][["Cultivator","Alchol"]]


# In[ ]:




