import pandas as pd
import numpy as np
import streamlit as st

# Coordenadas del centro de Tlaxcal (19.318889, -98.237778)
brasil_data = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [19.318889, -98.237778],
    columns=['lat', 'lon'],
    index=range(500))

# Coordenadas del centro de Roma (41.9028, 12.4964)
kazakhstan_data = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [41.9028, 12.4964],
    columns=['lat', 'lon'],
    index=range(500, 1000))

# Combina los datos de Brasil y Kazajistán en un solo DataFrame
map_data = pd.concat([brasil_data, kazakhstan_data])

# Crea el título para la aplicación web
st.title("Tlaxcal and Roma Map")
st.header("Using Streamlit and Mapbox")

# Muestra ambos países en el mapa
st.map(map_data)

def circulo(num_datos=100, R=1, minimo=0, maximo=1):
    pi = np.pi
    r = R * np.sqrt(np.random.truncnorm(minimo, maximo, size=num_datos)) * 10
    theta = np.random.truncnorm(minimo, maximo, size=num_datos) * 2 * pi + 10
    #print(len(r)) 
    #print(len(theta))
    x = np.cos(theta) * r
    y = np.sin(theta) * r

    y = y.reshape((num_datos, 1))
    x = x.reshape((num_datos, 1))

    #Vamos el numero de elementos para que no cause overflow
    x = np.round(x, 3)
    y = np.round(y, 3)

    df = np.column_stack((x, y))
    #print(df)
    return df