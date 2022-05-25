#!/usr/bin/env python
# coding: utf-8

# # Segunda entrega Proyecto

# ## Importar librerias

# In[1]:


#!pip install --upgrade geopandas
#!pip install --upgrade pyshp
#!pip install --upgrade shapely
#!pip install --upgrade descartes
#!pip install --upgrade topojson
#!pip install --upgrade plotly


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


# # Importar Datos

# In[4]:


df_proyecto2 = pd.read_csv("C:/Users/fabia/Downloads/Juan_Bohorquez_Pedro_Ochoa_Entrega_Proyecto_2/Datos_proyectodefinitivo3.csv", 
                 sep = ',',
                )


# In[5]:


df_proyecto2.head()


# In[6]:


df_proyecto2 = df_proyecto2.drop(["Unnamed: 0"], axis=1)


# In[7]:


df_proyecto22 = df_proyecto2[df_proyecto2["Indicator Name"] == "Porcentaje de niños economicamente activos"]


# In[8]:


df_proyecto2_codigo = pd.read_csv("C:/Users/fabia/Downloads/Juan_Bohorquez_Pedro_Ochoa_Entrega_Proyecto_2/world-countries.csv", 
                 sep = ',',
                )


# In[9]:


df_proyecto2_codigo = df_proyecto2_codigo.drop(["name"], axis=1)


# In[10]:


df_unida = df_proyecto22.merge(df_proyecto2_codigo, 
                             left_on='Country Code_x', 
                             right_on='id', 
                             how = 'right')


# In[11]:


df_proyecto_2 = pd.pivot_table(df_unida, 
                                values=['2000',"2001","2002","2003","2004","2005","2006","2007","2008","2009",
                                       "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"], 
                                index=["Indicator Name"],
                                    columns=['Country Name',"Sexo_o_clase","Income_Group","Region","id","lat","lon"], 
                                aggfunc=np.mean)
df_proyecto_2 = pd.DataFrame(df_proyecto_2)


# In[12]:


df_proyecto_2 = df_proyecto_2.transpose().reset_index()


# In[13]:


df_proyecto_2 = df_proyecto_2[df_proyecto_2["Sexo_o_clase"] == "Hombre"]


# In[14]:


df_proyecto_2 = df_proyecto_2.rename(columns = {"Income_Group" : "Clasificacion de paises segun sus ingresos"})


# In[15]:


df_proyecto_2 = df_proyecto_2.rename(columns = {"level_0" : "Año"})


# # Mapa de Burbujas

# In[16]:


import plotly.graph_objects as go
px.set_mapbox_access_token("pk.eyJ1IjoiZGFvY2hvYTA4MjAwMiIsImEiOiJjbDFtdzZraTIwajdnM2p1a3Q1d2EwemtjIn0.HKAYriGAUUaNXeVBc9Bxjg")


# In[17]:


fig = px.scatter_mapbox(df_proyecto_2,
                        lat='lat',
                        lon='lon',
                        hover_name='Country Name',
                        zoom=3,
                        color="Clasificacion de paises segun sus ingresos",
                        size="Porcentaje de niños economicamente activos",
                        animation_frame="Año", 
                        center = {"lat": 4.570868, "lon": -74.297333})
fig.update_layout(
        title_text = 'Porcentaje de prevalencia de VIH en Hombres entre 15 y 24 años de edad',
        showlegend = True,
    )
fig.show()


# ### Tareas 
#     Datos: Datos de geometria geografica. 
#     codificacion: Utiliza circulos de diefrentes tamaños para reprersentar un valor numerico en un territorio. 
#         marcas de puntos.
#         Tamaño.
#         Color. 

# ### Insights
# Los paises que presentan un mayor porcentaje de hombres con prevalencia de VIH see encuentran al sur de Africa y en el caso de America en el Caribe. "Sin la adecuada nutrición, atención sanitaria y medicamentos (tales como los antirretrovirales) que están disponibles en los países desarrollados, un gran número de personas en África desarrollarán la enfermedad del sida por completo."

# # Mapa de Hexagonos

# In[18]:


df_proyecto2_2 = df_proyecto2[df_proyecto2["Indicator Name"] == "Esperanza de vida al nacer"]


# In[19]:


df_proyecto2_2 = df_proyecto2_2[df_proyecto2_2["Sexo_o_clase"] == "Mujer"]


# In[20]:


df_unida_2 = df_proyecto2_2.merge(df_proyecto2_codigo, 
                             left_on='Country Code_x', 
                             right_on='id', 
                             how = 'right')


# In[21]:


df_proyecto_22 = pd.pivot_table(df_unida_2, 
                                values=['2000',"2001","2002","2003","2004","2005","2006","2007","2008","2009",
                                       "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"], 
                                index=["Indicator Name"],
                                    columns=['Country Name',"Sexo_o_clase","Income_Group","Region","id","lat","lon"], 
                                aggfunc=np.mean)
df_proyecto_22 = pd.DataFrame(df_proyecto_22)


# In[22]:


df_proyecto_22 = df_proyecto_22.transpose().reset_index()


# In[23]:


df_proyecto_22 = df_proyecto_22.rename(columns = {"level_0" : "Año"})


# In[24]:


df_proyecto_22


# In[29]:


import plotly.figure_factory as ff
fig = ff.create_hexbin_mapbox(df_proyecto_22, 
                              lat="lat", 
                              lon="lon",
                              color="Esperanza de vida al nacer",
                              animation_frame='Año',
                              nx_hexagon=150,
                              opacity=0.5,
                              min_count=1,
                              labels={"color": "Esperanza de vida al nacer por años",
                                     "frame": "Año"},
)
fig.update_layout(
        title_text = 'Esperanza de vida al nacer Mujer por años',
        showlegend = True,
    )
fig.show()


# ### Tareas 
#     Datos: Datos de geometria geografica. 
#     codificacion: Utiliza circulos de diefrentes tamaños para reprersentar un valor numerico en un territorio. 
#         marcas de puntos.
#         Color. 

# ### Insights
# la esperanza de vida para las mujeres desde el año de 2010 al sur de Africa ha tenido una mejoria respecto a años anteriores. 
# Debido a la accesibilidad a medicamentos y mejores recursos pra el sutento de la poblacion en enfermedades y tratamientos

# In[ ]:




