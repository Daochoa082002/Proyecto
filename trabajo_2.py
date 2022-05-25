import dash
from dash import dcc
from dash import html
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#app = dash.Dash(__name__)

df_datos = pd.read_csv('Datos_trabajo2.csv', 
                 sep = ','
                 )
df_datos = df_datos.drop(["Unnamed: 0"], axis=1)

df_datos2 = pd.read_csv("Datos_mapa2.csv", 
                 sep = ',')
df_datos2 = df_datos2.drop(["Unnamed: 0"], axis=1)

available_region = df_datos['Region'].unique()
available_region2 = df_datos['Region'].unique()
available_sexo = df_datos['Sexo_o_clase'].unique()
available_ingreso = df_datos['Income_Group'].unique()
available_region3 = df_datos['Region'].unique()
available_sexo6 = df_datos['Sexo_o_clase'].unique()

app.layout = html.Div(
    children=[
        html.H1(children="Situación de Niños y Niñas en la Fuerza Laboral (7 a 14 años de edad)",
            style = {
                        'textAlign': 'center',
            }),
        html.H2(children="Clasificación de Países"),
        html.P(
            children="En ésta visualización se puede observar "
            "la distribución de los países alrededor del mundo "
            "en este caso por región y como se clasifican "
            "por su nivel de ingreso clasificados por el Banco Mundial."
            ),
    html.Div([
        html.Div(children='''
            Región
        '''),#
        dcc.Dropdown(
            id='crossfilter_region',
            options=[{'label': i, 'value': i} for i in available_region],
            value=''
        ),
        dcc.Graph(
            id='example-graph-1'
        ),
        html.H2(children='Insigth'),
            html.P(
            children="El caso de Venezuela se debe a que no tiene deuda pública con el Banco Mundial, a lo que este lo clasifica "
            "como 'No clasificado', en la base de datos.  "
            "Una de las regiones mas favorables se encuentra en Europa y Asia Central, pues muchos países se clasifican en nivel de Ingreso Alto. Caso contrario con África al sur del Sahara."
            ),  
    ]),
    html.Div([
        html.Div([
            html.H1(children='Mapa de Burbujas'),#
            html.H2(children='Tarea'),
            html.P(
            children="Por medio de la siguiente gráfica se quiere encontrar "
            "tendencias y correlaciones entre las variables niños economicamente activos  "
            "y si solo trabajan y estudian. Por lo el usario podra interactuar por medio de las regiones "
            "logrando encontar datos atipicos y distribuciones y relaciones entre regiones, "
            "para el caso de la región de America del Norte y Oceanía no presentan datos en la base a lo que no se muestra al momento de interactuar. "
            "El tamaño de las burbujas se ve influnciado por el porcentaje de los valores de niños economicamente activos. "
            ),
            html.Div(children='''
                Región
            '''),#
            dcc.Checklist(id='crossfilter_region2',
                options=[{'label': i, 'value': i} 
                            for i in available_region2],
                value = [''],
                labelStyle={'display': 'inline-block'}
                ),
            dcc.Graph(
                id='example-graph-2'
            ),
            html.H2(children='Insigth'),
            html.P(
            children="Existe una relación de orden entre la clasificación de países segun su ingreso, "
            "pues la gran mayroia de datos para países de ingreso bajo los niños solo trabajan  "
            "mientras que para los de ingreso alto se posicionan en espectativas de que los niños trabajan y estudian. "
            "La region mayor afectada por lo anterior es África al sur del Sahara, America Latina y el Caribe, Europa y Asia central y Asia oriental y el Pacífico "
            "caso contrario lo encontramos con Oriente Medio y Norte de África. "
            ),  
        ], className='six columns'),
        html.Div([
            html.H1(children='Histograma'),#
            html.H2(children='Tarea'),
            html.P(
            children="Por medio de un Histograma podemos encontar distribuciones por medio de los conteos que tenga un valor "
            "en la base de datos, aqui sucede lo mismo para las regiones de America del Norte y Oceanía, pues no tienen porcentajes en este indicador.  "
            "El usuario podra interactuar con la variable Tipo en la que puede seleccionar entre tres variables Hombre, Hombre y Mujer, Mujer. En el caso de Hombre y Mujer "
            "es una estimación que se haya con los datos recogidos de las variables Hombre, Mujer. Además, podra seleccionar la región de interés para ver sus respectivas "
            "distribuciones, encontrar datos atípicos y rangos en el histograma. "
            ),
            html.Div(children='''
                Tipo
            '''),#
            dcc.Checklist(id='crossfilter_sexo',
                options=[{'label': i, 'value': i} 
                            for i in available_sexo],
                value = [''],
                labelStyle={'display': 'inline-block'}
                ),
            dcc.Graph(
                id='example-graph-3'
            ), 
            html.H2(children='Insigth'),
            html.P(
            children="A nivel general los datos se tienden a acumular en los porcentajes del 0% - 60%, se debe a que hay países que no presentan datos "
            "o la información proporcionada es escasa debido a que los niños son abalados por los padres y otras entidades por lo que muchas veces  "
            "estos datos no se consideran muy seguido. "
            "Además se logra visualizar un dato atípico que se posiciona al rango cercano del 100%, en el que podemos ver la situación en esa región "
            "y como la situación a nivel social va desmejorando en el mundo. "
            ), 
        ], className='six columns'),
    ], className='row'),
    html.Div([
        html.Div([
            html.H1(children='Gráfico de Lineas'),#
            html.H2(children='Tarea'),
            html.P(
            children="En este caso podremos comparar tendencias y similitudes con las variables de Tipo y si existe alguna relación. "
            "Para este caso se recomienda seleccionar de una sola región y de un solo nivel de ingreo, pués se pueden presentar variaciones  "
            "ya que para un mismo año se puedo registar datos pero estos pueden ser diferentes para cada selección. "
            "Se hace esta recomendación para no confundir al usuario. Tambien se resalta de las anteriores para la Región de America del Norte y Oceanía."
            ),
            html.Div(children='''
                
                Región
            
            '''),#
            dcc.Dropdown(
                id='crossfilter_region3',
                 options=[{'label': x, 'value': x} 
                            for x in available_region3],
                value = [''],
                multi = True
                ),
            html.Div(children='''
                
                Nivel de Ingreso
            
            '''),#
            dcc.Dropdown(
                id='crossfilter_ingreso',
                 options=[{'label': x, 'value': x} 
                            for x in available_ingreso],
                value = [''],
                multi = True
                ),
            dcc.Graph(
                id='example-graph-4'
            ),
            html.H2(children='Insigth'),
            html.P(
            children="Se puede visualizar que para el nivel de ingreso Mediano Alto, durante la crisis Financiera de 2008, los porcentajes se posicionan  "
            "a valores altos, quizas se deba a empleos con relación a la mano de obra barata o a la crisis que conllevo a que la familia aportara "
            "de manera general. En el caso de America Latina y el Caribe se ha visto una tndencia a la baja desde que fue el año de 2000. "
            ),   
        ], className='six columns'),
        html.Div([
            html.H1(children='Matríz de Dispersión'),#
            html.H2(children='Tarea'),
            html.P(
            children="Es un modismo en el que podremos localizar varias variables y encontar correlaciones, tendencias, similitudes y puntos atípicos.  "
            "Por medio de la iteración de la región podemos ver que relacion existen entre las variables para cada región. Y verla para el tipo de Hombre, Hombre y Mujer, Mujer.  "
            "El usuario podra seleccionar la region y buscar correlaciones entre estas o tienen una tendencia."
            "También se resalta de las anteriores para la Región de America del Norte y Oceanía no presentan datos."
            ),
            html.Div(children='''
                Región
            '''),#
            dcc.Checklist(id='crossfilter_region4',
                options=[{'label': i, 'value': i} 
                            for i in available_region2],
                value = [''],
                labelStyle={'display': 'inline-block'}
                ),
            dcc.Graph(
                id='example-graph-5'
            ),
            html.H2(children='Insigth'),
            html.P(
            children="A nivel general de todas las regiones la variable Mujer se tienden a acumular en porcentajes altos en solo trabajan y estudian. "
            "Además de la relación que existe entre las variables de Solo trabajan y estudian y Solo trabajan, muestra que la gran mayoria de niños  "
            "trabajan y estudian. "
            ),  
        ], className='six columns'),
    ], className='row'),
    html.Div([
        html.H1(children='Mapa'),
        html.H2(children='Tarea'),
            html.P(
            children="Este se utiliza para reprsentar el porcentaje en cada país, permitiendo comparar entre países, buscar relaciones entre estos. "
            "El usuario podra interactuar con la variable tipo en la que puede viualizar el comportamiento de los datos de manera general para cada país y comparar  "
            "usnado las anteriores gráficas, para hallar estimaciones. A mayor claridad tambien puede movilizarse a través del tiempo para ver los cambios. "
            "También se resalta que a mayor tamaño de la nurbuja se refiere a un porcentaje alto en ese país. "
            ),
        html.Div(children='''
            Tipo
        '''),#
        dcc.Dropdown(
            id='crossfilter_sexo6',
            options=[{'label': i, 'value': i} for i in available_sexo6],
            value=''
        ),
        dcc.Graph(
            id='example-graph-6',
            style={'height': 800, 'width': 1700}
        ),
        html.H2(children='Insigth'),
            html.P(
            children="El mayor porcentaje se ubica en la región de Africa al sur del Sahara. "
            ),    
    ]),
])  

## Visualizacion 1 

@app.callback(
    dash.dependencies.Output('example-graph-1', 'figure'),
    [dash.dependencies.Input('crossfilter_region', 'value')]
    )

def update_graph(region_value):
    df_datos_region = df_datos[df_datos['Region'] == region_value]

    viz_1 = px.treemap(df_datos_region, 
                 path=['Income_Group','Country Name']
                )
    viz_1.update_layout({
                "margin": dict(l=20, r=20, t=20, b=20),
                "showlegend": True,
                "paper_bgcolor": "rgba(0,0,0,0)",
                "plot_bgcolor": "rgba(0,0,0,0)",
                "font": {"color": "white"},
                "autosize": True,
            })

    return viz_1 

## Visualizacion 2

@app.callback(
    dash.dependencies.Output('example-graph-2', 'figure'),
    [dash.dependencies.Input('crossfilter_region2', 'value')]
    )
def update_graph(tipo_region2_value):

	df_proyecto_4 = df_datos[df_datos['Region'].isin(tipo_region2_value)]
	df_proyecto_4 = pd.pivot_table(df_proyecto_4, 
                                values=['2000',"2001","2002","2003","2004","2005","2006","2007","2008","2009",
                                       "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"], 
                                index=["Indicator Name"],
                                    columns=["Income_Group","Sexo_o_clase","Region"], 
                                aggfunc=np.mean)
	df_proyecto_4 = df_proyecto_4.transpose().reset_index()
	df_proyecto_4 = df_proyecto_4.rename(columns = {"Income_Group" : "Clasificacion de paises por ingreso"})
	vis_2 = px.scatter(df_proyecto_4, x="Porcentaje de niños que solo trabajan y estudian", y="Porcentaje de niños economicamente activos",
         				size="Porcentaje de niños economicamente activos", color="Clasificacion de paises por ingreso",
                  		size_max=60)
	vis_2.update_layout({
                "margin": dict(l=20, r=20, t=20, b=20),
                "showlegend": True,
                "paper_bgcolor": "rgba(0,0,0,0)",
                "plot_bgcolor": "rgba(0,0,0,0)",
                "font": {"color": "white"},
                "autosize": True,
            })
	return vis_2

## Visualizacion 3

@app.callback(
    dash.dependencies.Output('example-graph-3', 'figure'),
    [dash.dependencies.Input('crossfilter_sexo', 'value')]
    )
def update_graph(tipo_sexo_value):

	df_proyecto_5 = df_datos[df_datos['Sexo_o_clase'].isin(tipo_sexo_value)]
	df_proyecto_5 = pd.pivot_table(df_proyecto_5, 
                                values=['2000',"2001","2002","2003","2004","2005","2006","2007","2008","2009",
                                       "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"], 
                                index=["Indicator Name"],
                                    columns=["Income_Group","Sexo_o_clase","Region"], 
                                aggfunc=np.mean)
	df_proyecto_5 = df_proyecto_5.transpose().reset_index()
	vis_3 = px.histogram(df_proyecto_5, x="Porcentaje de niños que solo trabajan", color="Region")
	vis_3.update_layout({
                "margin": dict(l=20, r=20, t=20, b=20),
                "showlegend": True,
                "paper_bgcolor": "rgba(0,0,0,0)",
                "plot_bgcolor": "rgba(0,0,0,0)",
                "font": {"color": "white"},
                "autosize": True,
            })
	return vis_3

# Visualizacion 4 

@app.callback(
    dash.dependencies.Output('example-graph-4', 'figure'),
    [dash.dependencies.Input('crossfilter_region3', 'value'),
     dash.dependencies.Input('crossfilter_ingreso', 'value')]
    )

def update_graph(tipo_region3_value, tipo_ingreso_value):
    df_proyecto_2 = df_datos[df_datos['Region'].isin(tipo_region3_value)]
    df_proyecto_2 = df_proyecto_2[df_proyecto_2['Income_Group'].isin(tipo_ingreso_value)]

    df_proyecto_2 = pd.pivot_table(df_proyecto_2, 
                                values=['2000',"2001","2002","2003","2004","2005","2006","2007","2008","2009",
                                       "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"], 
                                index=["Indicator Name"],
                                    columns=["Sexo_o_clase","Region","Income_Group"], 
                                aggfunc=np.mean)
    df_proyecto_2 = df_proyecto_2.transpose().reset_index()
    df_proyecto_2 = df_proyecto_2.rename(columns = {"Sexo_o_clase" : "Clase"})
    df_proyecto_2 = df_proyecto_2.rename(columns = {"level_0" : "Año"})

    vis_4 = px.line(df_proyecto_2, x="Año", y="Porcentaje de niños economicamente activos", color='Clase')
    vis_4.update_layout({
                "margin": dict(l=20, r=20, t=20, b=20),
                "showlegend": True,
                "paper_bgcolor": "rgba(0,0,0,0)",
                "plot_bgcolor": "rgba(0,0,0,0)",
                "font": {"color": "white"},
                "autosize": True,
            })

    return vis_4

# Visualizacion 5 

@app.callback(
    dash.dependencies.Output('example-graph-5', 'figure'),
    [dash.dependencies.Input('crossfilter_region4', 'value')]
    )
def update_graph(tipo_region4_value):

    df_proyecto_1 = df_datos[df_datos['Region'].isin(tipo_region4_value)]
    df_proyecto_1 = pd.pivot_table(df_proyecto_1, 
                                values=['2000',"2001","2002","2003","2004","2005","2006","2007","2008","2009",
                                       "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"], 
                                index=["Indicator Name"],
                                    columns=["Sexo_o_clase","Region"], 
                                aggfunc=np.mean)
    df_proyecto_1 = df_proyecto_1.transpose().reset_index()
    df_proyecto_1 = df_proyecto_1.rename(columns = {"Sexo_o_clase" : "Clase"})
    df_proyecto_1 = df_proyecto_1.rename(columns = {"level_0" : "Año"})
    df_proyecto_1 = df_proyecto_1.rename(columns = {"Porcentaje de niños economicamente activos" : "Fuerza Laboral"})
    df_proyecto_1 = df_proyecto_1.rename(columns = {"Porcentaje de niños que solo trabajan" : "Solo trabajan"})
    df_proyecto_1 = df_proyecto_1.rename(columns = {"Porcentaje de niños que solo trabajan y estudian" : "Trabajan y Estudian"})

    vis_5 = px.scatter_matrix(df_proyecto_1, dimensions=["Fuerza Laboral", "Solo trabajan", "Trabajan y Estudian"], color="Clase")
    vis_5.update_layout({
                "margin": dict(l=20, r=20, t=20, b=20),
                "showlegend": True,
                "paper_bgcolor": "rgba(0,0,0,0)",
                "plot_bgcolor": "rgba(0,0,0,0)",
                "font": {"color": "white"},
                "autosize": True,
            })

    return vis_5

# Visualizacion 6

@app.callback(
    dash.dependencies.Output('example-graph-6', 'figure'),
    [dash.dependencies.Input('crossfilter_sexo6', 'value')]
    )

def update_graph(sexo_value2):
    df_proyecto_6 = df_datos2[df_datos2['Sexo_o_clase'] == sexo_value2]

    df_proyecto_6 = pd.pivot_table(df_proyecto_6, 
                                    values=['2000',"2001","2002","2003","2004","2005","2006","2007","2008","2009",
                                           "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"], 
                                    index=["Indicator Name"],
                                    columns=['Country Name',"Income_Group","Region","id","lat","lon"], 
                                    aggfunc=np.mean)
    df_proyecto_6 = df_proyecto_6.transpose().reset_index()
    df_proyecto_6 = df_proyecto_6.rename(columns = {"Income_Group" : "Clasificacion de paises segun sus ingresos"})
    df_proyecto_6 = df_proyecto_6.rename(columns = {"level_0" : "Año"})

    px.set_mapbox_access_token("pk.eyJ1IjoiZGFvY2hvYTA4MjAwMiIsImEiOiJjbDFtdzZraTIwajdnM2p1a3Q1d2EwemtjIn0.HKAYriGAUUaNXeVBc9Bxjg")
    vis_6 = px.scatter_mapbox(df_proyecto_6,
                            lat='lat',
                            lon='lon',
                            hover_name='Country Name',
                            zoom=3,
                            color="Clasificacion de paises segun sus ingresos",
                            size="Porcentaje de niños economicamente activos",
                            animation_frame="Año", 
                            center = {"lat": 4.570868, "lon": -74.297333})
    vis_6.update_layout(
        title_text = 'Porcentaje de niños economicamente activos',
        showlegend = True,
    )
    vis_6.update_layout({
                "margin": dict(l=20, r=20, t=20, b=20),
                "showlegend": True,
                "paper_bgcolor": "rgba(0,0,0,0)",
                "plot_bgcolor": "rgba(0,0,0,0)",
                "font": {"color": "white"},
                "autosize": True,
            })

    return vis_6

if __name__ == "__main__":
    app.run_server(debug=True)