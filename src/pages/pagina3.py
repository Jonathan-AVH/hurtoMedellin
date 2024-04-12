import pandas as pd
from taipy.gui import Gui, Html
from taipy.gui import Gui 
import taipy.gui.builder as tgb 
from taipy.gui import Markdown, Gui
import locale

# Lee el archivo CSV en un DataFrame
df = pd.read_csv('src/data/tu_archivo.csv', sep=';', engine='python')
df1 = pd.read_csv('src/data/tu_archivo.csv', sep=';', engine='python')
#eliminamos las columnas vacias
df.drop(['seguridad.nivel_academico', 'seguridad.testigo','seguridad.color'], axis=1, inplace=True)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
df1.drop(['seguridad.nivel_academico', 'seguridad.testigo','seguridad.color'], axis=1, inplace=True)

# Asignar nuevos nombres a todas las filas
df.columns =  ['id', 'fecha_hecho', 'latitud','longitud','sexo','edad','estado_civil','medio_transporte','conducta','modalidad','conducta_especial','arma_medio','nombre_barrio','codigo_barrio','codigo_comuna','lugar_hecho','sede_receptora','bien','categoria_bien']
df1.columns =  ['id', 'fecha_hecho', 'latitud','longitud','sexo','edad','estado_civil','medio_transporte','conducta','modalidad','conducta_especial','arma_medio','nombre_barrio','codigo_barrio','codigo_comuna','lugar_hecho','sede_receptora','bien','categoria_bien']


#tipo de medio_transporte
edad = df.groupby("edad").size()

# Definir los rangos de edades
bins = [0, 19, 29, 39, 49, 59, 69, 79, 90]
labels = ['0-19', '20-29', '30-39', '40-49', '50-59','60-69', '70-79', '80-90' ]

# Crear una nueva columna con los rangos de edades
df['Rango_Edad'] = pd.cut(df['edad'], bins=bins, labels=labels)

Rango_Edad = df.groupby("Rango_Edad").size()

Rango_Edad_organizados = Rango_Edad.sort_values(ascending=False)

Rango_edades = pd.DataFrame({'Rango_edad': Rango_Edad_organizados.index, 'Numero_casos': Rango_Edad_organizados.values})

# Filtarr datos en donde el genero sea masculino, esto con el fin de obtener la modalidad de hurto 
df_masculino = df1[df1['sexo'] == 'Hombre']

modalidad = df_masculino.groupby("modalidad").size()

top_5_modalidad = modalidad.sort_values(ascending=False).head(5)

tabla_modalidad_hombre = pd.DataFrame({'Modalidad': top_5_modalidad.index, 'Numero_casos': top_5_modalidad.values})

# Filtarr datos en donde el genero sea masculino, esto con el fin de obtener la modalidad de hurto 
df_mujer = df1[df1['sexo'] == 'Mujer']

modalidad_mujer = df_mujer.groupby("modalidad").size()

top_5_modalidad_mujer = modalidad_mujer.sort_values(ascending=False).head(5)

tabla_modalidad_mujer = pd.DataFrame({'Modalidad': top_5_modalidad_mujer.index, 'Numero_casos': top_5_modalidad_mujer.values})

marker = {
    "Sizes":  [60, 80, 100],
    
    "colors": [
        "rgb(93, 164, 214)",
        "rgb(44, 160, 101)",
        "rgb(255, 65, 54)",
    ]
}
n_slices = 20
# List: [1..n_slices]
# Slices are bigger and bigger
values = list(range(1, n_slices+1))

marker = {
    # Colors move around the Hue color disk
    "colors": [f"hsl({360*(i-1)/(n_slices-1)},90%,60%)" for i in values]
}

marker1 = {
    # Colors move around the Hue color disk
    "colors": [f"hsl({360*(i-1)/(n_slices-1)},350%,85%)" for i in values]
}


pagina_3 = Markdown("""
<center><|navbar|></center>

<|toggle|theme|>

<|layout|columns=1fr 1fr|

## NÚMERO DE CASOS POR RANGO DE EDADES **CASOS**{: .color-primary}<|{Rango_edades}|chart|mode=markers|x=Rango_edad|y=Numero_casos|marker={marker}|>

## TOP 5 DE MODALIDADES DE HURTOS EN **HOMBRES**{: .color-primary}<|{tabla_modalidad_hombre}|chart|type=pie|values=Numero_casos|labels=Modalidad|marker={marker}|>

## TOP 5 DE MODALIDADES DE HURTOS EN **MUJERES**{: .color-primary}<|{tabla_modalidad_mujer}|chart|type=pie|values=Numero_casos|labels=Modalidad|marker={marker1}|>

|>
""")