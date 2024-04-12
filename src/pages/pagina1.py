import pandas as pd
from taipy.gui import Gui, Html
from taipy.gui import Gui 
import taipy.gui.builder as tgb 
from taipy.gui import Markdown, Gui




# Lee el archivo CSV en un DataFrame
df = pd.read_csv('src/data/tu_archivo.csv', sep=';', engine='python')

#eliminamos las columnas vacias
df.drop(['seguridad.nivel_academico', 'seguridad.testigo','seguridad.color'], axis=1, inplace=True)


# Asignar nuevos nombres a todas las filas
df.columns =  ['id', 'fecha_hecho', 'latitud','longitud','sexo','edad','estado_civil','medio_transporte','conducta','modalidad','conducta_especial','arma_medio','nombre_barrio','codigo_barrio','codigo_comuna','lugar_hecho','sede_receptora','bien','categoria_bien']


conteo_ciudades = df.groupby('nombre_barrio').size()


top_10_valores = conteo_ciudades.sort_values(ascending=False).head(10)



# Convertir la serie en un dataframe
dataframe_ejemplo = pd.DataFrame({'Nombres_barrios': top_10_valores.index, 'Numero_casos': top_10_valores.values})

#tabla de casos por genero
tabla_sexo = df.groupby("sexo").size()

tabla_sexo_1 = pd.DataFrame({'sexo': tabla_sexo.index, 'Numero_casos': tabla_sexo.values})

#tabla de modalidad de hurto
modalidad = df.groupby("modalidad").size()

top_5_modalidad = modalidad.sort_values(ascending=False).head(5)

tabla_modalidad = pd.DataFrame({'Modalidad': top_5_modalidad.index, 'Numero_casos': top_5_modalidad.values})


#tipo de bien robado
bien_robado = df.groupby("bien").size()

top_7_bien_robado = bien_robado.sort_values(ascending=False).head(7)

tabla_bien_robado = pd.DataFrame({'bien': top_7_bien_robado.index, 'Numero_casos': top_7_bien_robado.values})

layout = {
    # Stack the areas
    "funnelmode": "stack",
    # Hide the legend
    "showlegend": False
}


pagina_1 = Markdown("""
<center><|navbar|></center>                   


<|toggle|theme|>


# 📊 Casos de hurtos en **la ciudad de Medellin**{: .color-primary}

<|layout|columns=1fr 1fr|

## TOP 10 BARRIOS CON MAS **CASOS**{: .color-primary}<|{dataframe_ejemplo}|chart|type=bar|x=Nombres_barrios|y=Numero_casos|>

## CUAL ES EL GENERO CON MAS NUMEROS DE **CASOS**{: .color-primary}<|{tabla_sexo_1}|chart|type=pie|values=Numero_casos|labels=sexo|>

## TOP 5 DE LAS MODALIDADES DE **HURTOS**{: .color-primary}<|{tabla_modalidad}|chart|type=bar|x=Modalidad|y=Numero_casos|>

## TOP 7 DE LOS BIENES MAS **ROBADOS**{: .color-primary}<|{tabla_bien_robado}|chart|type=funnelarea|values=Numero_casos|text=bien|layout={layout}|>                
|>

""")

