import pandas as pd
import time
import os
import numpy as np

# Cargar el archivo CSV
file_path = 'thermistor_log.csv'
data = pd.read_csv(file_path)

# Definir la asignación de termistores a módulos
mapeo_modulos = {
    1: [41], 2: [43], 3: [46], 4: [47, 48], 5: [49, 50], 6: [51], 7: [54, 55],
    8: [56], 9: [57, 58], 10: [22], 11: [21, 25], 12: [23, 24], 13: [27, 28],
    14: [29, 30], 15: [31, 32], 16: [33, 34], 17: [35], 18: [39], 19: [37, 38],
    20: [13, 14], 21: [11, 12], 22: [7, 8], 23: [10], 24: [6], 25: [4], 26: [1],
    27: [36], 28: [np.nan]
}

# Invertir el mapeo para facilitar la asignación
mapeo_termistores = {}
for modulo, termistores in mapeo_modulos.items():
    for termistor in termistores:
        mapeo_termistores[termistor] = modulo

columnas = data.columns[5:65]

def assign_module_to_row(row):
    module_info = {}
    for termistor in columnas:
        termistor_number = int(termistor.split(' ')[-1])  # Asumiendo que los termistores tienen nombres con un número al final
        module_info[termistor] = mapeo_termistores.get(termistor_number, np.nan)
    return pd.Series(module_info)

# Añadir columnas de módulos al DataFrame

print(data)

'''# Función para mostrar las filas reemplazando el contenido cada segundo, hasta la columna 65
def display_rows(data):
    for index, row in data.iterrows():
        # Limpiar la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')
        for col in columnas:
            termistor_value = row[col]
            module_value = row[f"{col} module"]
            print(f"{col}: {termistor_value}, Módulo: {module_value}")
        time.sleep(1)

# Ejecutar la función
display_rows(data)'''
