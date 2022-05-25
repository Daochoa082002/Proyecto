#!/usr/bin/env python
# coding: utf-8

# # Segunda Entrega Proyecto

# ## Importar librerias. 

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import matplotlib.pyplot as plt
import altair as alt
from vega_datasets import data


# In[3]:


pd.set_option('display.max_columns', None) #Mostrar todas las columnas
sns.set(rc={'figure.figsize':(12.7,8.6)})


# ## Importar Datos 

# Datos extraidos de los datos recogidos por el Banco Mundial. 
# Url = Fuente: https://datos.bancomundial.org/tema/desarrollo-social?view=chart

# In[4]:


df_proyecto2 = pd.read_csv("C:/Users/fabia/Downloads/Juan_Bohorquez_Pedro_Ochoa_Entrega_Proyecto_2/Datos_proyectodefinitivo2.csv", 
                 sep = ',',
                )


# In[5]:


df_proyecto2.head()


# ## Pre-procesamiento de los datos.

# In[6]:


df_proyecto_2 = pd.pivot_table(df_proyecto2, 
                                values=['2000',"2001","2002","2003","2004","2005","2006","2007","2008","2009",
                                       "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"], 
                                index=["Indicator Name"],
                                    columns=['Country Name',"Sexo_o_clase","Income_Group","Region"], 
                                aggfunc=np.mean)
df_proyecto_2 = pd.DataFrame(df_proyecto_2)


# In[7]:


df_proyecto_2 = df_proyecto_2.transpose().reset_index()


# In[8]:


df_proyecto_2.head()


# In[9]:


df_proyecto_2 = df_proyecto_2.rename(columns = {"level_0" : "Año"})


# In[10]:


df_proyecto_2['Año'] = pd.to_datetime(df_proyecto_2['Año'],format='%Y')


# In[11]:


df_proyecto_2['Año'].value_counts()


# ## Grafico de lineas

# In[12]:


df_desempleo = pd.pivot_table(df_proyecto_2, 
                                values=["Desempleo"], 
                                index=["Sexo_o_clase"],
                                    columns=["Año","Income_Group"], 
                                aggfunc=np.mean)
df_desempleo = pd.DataFrame(df_desempleo)


# In[13]:


df_desempleo.reset_index().head()


# In[14]:


df_desempleo = df_desempleo.transpose().reset_index()


# In[15]:


df_desempleo.head()


# In[16]:


df_desempleo = df_desempleo.rename(columns = {"Income_Group" : "Claisificacion de paises por ingreso"})


# In[28]:


import matplotlib.ticker as mtick

sns.lineplot(data=df_desempleo, x="Año", y = "Hombre",hue = "Claisificacion de paises por ingreso")
plt.ticklabel_format(style='', axis='y')
ax = plt.gca()
ax.yaxis.set_major_formatter('{x:1.0f}%')
plt.title('Porcentaje de Desempleo hombres segun clasificacion de paises por ingreso',size =20)
plt.ylabel('',size=5)
plt.show()


# ### Tareas
#     Datos:
#         Se usa tabla para clasificar los datos, y se une mediante lineas. 
#     Tareas:
#         Comparar tendencias y similitudes con muchos en este caso la clasificacion.
#         Localizar datos atipicos. 
#     Representacion visual: 
#         linea, posicion vertical, tono de color. 

# ### Insights 
# Lo curioso de esta visualizacion, la tasa de desempleo para paises de ingreso bajo, ingreso mediano bajo son bajas respecto a los de mayor ingreso y no presentan cambios variados. Otro dato fue el del año 2020 en el que en todos los paises subio debido a la propagacion del Virus Covid-19. 
#     En el caso del pais no clasificado hace referencia a Venezuela, unico pais que el Bnaco Mundial no tiene prestamos activos, por lo     que tiene esa clasificacion. 

# # Grafico de area radial 

# Los siguientes codigos es para visualizar los datos de cada pais que vamos a usar. 

# In[19]:


df_col = df_proyecto2[df_proyecto2["Indicator Name"] == "Tasa de fertilidad"]


# In[20]:


df_col = df_col[df_col["Country Name"] == "Colombia"]


# In[21]:


df_mex = df_proyecto2[df_proyecto2["Indicator Name"] == "Tasa de fertilidad"]


# In[22]:


df_mex = df_mex[df_mex["Country Name"] == "México"]


# In[23]:


df_ecu = df_proyecto2[df_proyecto2["Indicator Name"] == "Tasa de fertilidad"]


# In[24]:


df_ecu = df_ecu[df_ecu["Country Name"] == "Ecuador"]


# In[25]:


df_ven = df_proyecto2[df_proyecto2["Indicator Name"] == "Tasa de fertilidad"]


# In[26]:


df_ven = df_ven[df_ven["Country Name"] == "Venezuela"]


# In[27]:


from math import pi
# Datos
df_fertilidad = pd.DataFrame({
'group': ['Colombia','Mexico','Ecuador','Venezuela'],
'2008': [80.3788, 69.43, 83.4192, 89.4832],
'2009': [78.6136, 68.565, 83.2504, 89.0674],
'2010': [76.8484, 67.7, 83.0816, 88.6516],
'2011': [75.0832, 66.835, 82.9128, 88.2358],
'2012': [73.318, 65.97, 82.744, 87.82],
'2013': [71.9846, 64.849, 82.0474, 87.3234],
'2014': [70.6512, 63.728, 81.3508, 86.8268],
'2015': [69.3178, 62.607, 80.6542, 86.3302],
'2016': [67.9844, 61.486, 79.9576, 85.8336],
'2017': [66.651, 60.365, 79.261, 85.337],
'2018': [65.482, 59.4542, 78.7626, 84.9792],
'2019': [64.313, 58.5434, 78.2642, 84.6214], 
})
df_fertilidad


# In[28]:


# ------- PARTE 1: Crear el backgroud
 
# Número de variables numéricas
categories=list(df_fertilidad)[1:]
N = len(categories)
print(categories)
print(N)


# In[29]:


maxnum = df_fertilidad[categories].values.max()
maxnum


# In[30]:


# ¿Cuál será el ángulo de cada eje en el gráfico? (dividimos la parcela / número de variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Iniciar el gráfico de area radial (alias spider plot)
ax = plt.subplot(111, polar=True)
 
# Si tu quieres que el primer eje quede en el top
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

# Dibujar un por uno el eje y agregar labels
plt.xticks(angles[:-1], categories)
 
# Dibujar los labels de y (ojo con el min y max)
ax.set_rlabel_position(0)
plt.ylim(55,maxnum)

# ------- PARTE 2: Agregar gráficos (uno por uno :( )
 
# Pais de Colombia
values=df_fertilidad.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Colombia")
ax.fill(angles, values, 'blue', alpha=0.1)
 
# Pais de Mexico
values=df_fertilidad.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Mexico")
ax.fill(angles, values, 'blue', alpha=0.1)

# Pais de Ecuador
values=df_fertilidad.loc[2].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Ecuador")
ax.fill(angles, values, 'blue', alpha=0.1)
 
# Pais de Venezuela
values=df_fertilidad.loc[3].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Venezuela")
ax.fill(angles, values, 'blue', alpha=0.1)
 
# Agregar leyenda
plt.title('Tasa de fertilidad en adolescentes mujeres entre los 15 a 19 años en porcentajes',size =20)
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# TARAAAAN
plt.show()


# ### Tareas 
#     Datos: Tabla donde usa paises y años, una linea de tiempo.
#     Tareas:
#         Comparar tendencias (por años).
#         Localizar valores atipicos. 
#     Representacion visual:
#         linea, posicion radial, tono de color. 

# ### Insights
# Lo curioso que se puede detallar de este grafico el cambio inversamente que han tenido Colombia y Mexico respecto a esta tasa. En cambio Venezuela y ECuador que segun la organizacion UNICEF son uno de los paises con mayor tasa en latinoamerica y el Caribe. Lo que trae consecuencias como: "El embarazo en la adolescencia y la maternidad temprana no solo impactan sobre las trayectorias educativas, 
# laborales y de salud de niñas y adolescentes madres, sino que también perjudican el desarrollo y el crecimiento 
# económico del país. Esto es porque frente a una Tasa Específica de Fecundidad Adolescente (TEFA) alta, es decir, 
# frente a una alta proporción de mujeres que fueron madres entre los 10 y 19 años, se ve comprometido el potencial 
# que ofrece la fase del bono demográfico. Este fenómeno ocurre cuando la población en edad de trabajar supera en 
# cantidad a la población económicamente dependiente (niños y adultos mayores)." En pocas palabras la poblacion que depende economicamente de terceros es alta, la demanda aumenta hacia a ellos frente a una poblacion que no dependa, superando el costo de de adquisicion para la poblacion no dependiente.  
