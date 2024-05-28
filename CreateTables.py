import requests
import json
import sqlite3
from tqdm import tqdm

# Hacer la solicitud a la API y obtener los datos JSON
url = "https://nycopendata.socrata.com/resource/erm2-nwe9.json"
response = requests.get(url)
data = response.json()

# Mostrar estado
print("Datos obtenidos de la API.")

# Guardar los datos en un archivo JSON
with open("nyc_311_data.json", "w") as outfile:
    json.dump(data, outfile)

# Conexión a la base de datos SQLite
conn = sqlite3.connect('nyc_311.db')
c = conn.cursor()

# Crear la tabla para almacenar los datos
c.execute('''CREATE TABLE IF NOT EXISTS nyc_311_service_requests (
                unique_key TEXT,
                created_date TEXT,
                closed_date TEXT,
                agency TEXT,
                agency_name TEXT,
                complaint_type TEXT,
                descriptor TEXT,
                borough TEXT
             )''')

# Mostrar estado
print("Tabla creada en la base de datos.")

# Guardar los datos en la tabla
total_entries = len(data)
with tqdm(total=total_entries, desc="Insertando datos en la base de datos", unit="entry") as pbar:
    for entry in data:
        c.execute('''INSERT INTO nyc_311_service_requests VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                    (entry.get('unique_key'), entry.get('created_date'), entry.get('closed_date'),
                     entry.get('agency'), entry.get('agency_name'), entry.get('complaint_type'),
                     entry.get('descriptor'), entry.get('borough')))
        pbar.update(1)

# Mostrar estado
print("Datos insertados en la base de datos.")

# Commit y cerrar la conexión a la base de datos
conn.commit()
conn.close()

# Mostrar mensaje de finalización
print("Proceso completado.")
