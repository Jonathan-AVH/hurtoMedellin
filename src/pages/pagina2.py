import pandas as pd
from taipy.gui import Gui, Html
from taipy.gui import Gui 
import taipy.gui.builder as tgb 
from taipy.gui import Markdown, Gui
import locale




# Lee el archivo CSV en un DataFrame
df = pd.read_csv('src/data/tu_archivo.csv', sep=';', engine='python')
#eliminamos las columnas vacias
df.drop(['seguridad.nivel_academico', 'seguridad.testigo','seguridad.color'], axis=1, inplace=True)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Asignar nuevos nombres a todas las filas
df.columns =  ['id', 'fecha_hecho', 'latitud','longitud','sexo','edad','estado_civil','medio_transporte','conducta','modalidad','conducta_especial','arma_medio','nombre_barrio','codigo_barrio','codigo_comuna','lugar_hecho','sede_receptora','bien','categoria_bien']

#tipo de medio_transporte
medio_transporte = df.groupby("medio_transporte").size()

medio_transporte1 = medio_transporte.sort_values(ascending=False)

tabla_medio_transporte = pd.DataFrame({'medio_transporte': medio_transporte1.index, 'Numero_casos': medio_transporte1.values})

##hora con mas casos
# Convertir la columna 'Fecha_Hora' a tipo datetime
df['fecha_hecho'] = pd.to_datetime(df['fecha_hecho'], format="%d/%m/%Y %H:%M", dayfirst=True)

# Crear columnas separadas para la fecha y la hora
df['Fecha'] = df['fecha_hecho'].dt.date
df['Hora'] = df['fecha_hecho'].dt.time
# Convertir la columna 'Hora_24' a tipo datetime
df['Hora_24'] = pd.to_datetime(df['Hora'], format='%H:%M:%S')
# Crear una nueva columna con el formato de 12 horas
df['Hora_12'] = df['Hora_24'].dt.strftime('%H:%M')

print(df['Hora_12'])

tabla_hora = df.groupby("Hora_12").size()

top_10_hora_robo = tabla_hora.sort_values(ascending=False).head(10)

tabla_hora_robo = pd.DataFrame({'Hora': top_10_hora_robo.index, 'Numero_casos': top_10_hora_robo.values})

print(tabla_hora_robo)
##AÑO CON MAS CASOS
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Año'] = df['Fecha'].dt.year

tabla_año = df.groupby("Año").size()

top_10_tabla_año = tabla_año.sort_values(ascending=False)

tabla_año_robo = pd.DataFrame({'Año': top_10_tabla_año.index, 'Numero_casos': top_10_tabla_año.values})

marker = {
    "color": "Colors",
    "size": "Sizes",
    "opacity": "Opacities"
}

##MESES CON MAS CASOS
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Mes'] = df['Fecha'].dt.strftime('%B')

tabla_mes = df.groupby("Mes").size()



top_10_tabla_mes = tabla_mes.sort_values(ascending=False)


tabla_mes_robo = pd.DataFrame({'Mes': top_10_tabla_mes.index, 'Numero_casos': top_10_tabla_mes.values})
options = {
    # Lines connecting boxes are thick, dotted and green
    "connector": {
        "line": {
            "color": "green",
            "dash": "dot",
            "width": 4
        }
    }
}




pagina_2 = Markdown("""
<center><|navbar|></center>

<|toggle|theme|>

<|layout|columns=1fr 1fr|

## LOS MEDIOS DE TRANSORTE EN DONDE SE PRESENTAN MAS **CASOS**{: .color-primary}<|{tabla_medio_transporte}|chart|type=bar|x=medio_transporte|y=Numero_casos|>
                    
## TOP 10 DE LAS HORAS DONDE MAS SE PRESENTAN **HURTOS**{: .color-primary}<|{tabla_hora_robo}|chart|type=bar|x=Hora|y=Numero_casos|>

## INCREMENTO DE CASOS DE HURTO DESDE EL AÑO **2002 AL 2019**{: .color-primary}<|{tabla_año_robo}|chart|mode=markers|x=Año|y=Numero_casos|marker={marker}|>

## NUMERO DE CASOS QUE SE PRESENTAN EN CADA **MES**{: .color-primary}<|{tabla_mes_robo}|chart|type=funnel|x=Numero_casos|y=Mes|marker={marker}|options={options}|>                
|>
""")
