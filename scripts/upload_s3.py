import boto3
import os
from utils.env import get_secrets  # Importar la configuración de secrets.toml
from pathlib import Path

path_base = Path(__file__).resolve().parents[1]

# Obtener la configuración de secrets
secrets = get_secrets()

# Configurar AWS S3 usando las credenciales y el bucket
s3_client = boto3.client("s3")

# Archivos específicos que se deben subir (usando rutas absolutas)
files_to_upload = [
    path_base / "models/isolation_forest_model.pkl",
    path_base / "data/chunk_1.json",
    path_base / "data/chunk_2.json",
    path_base / "data/chunk_3.json",
    path_base / "data/chunk_4.json",
    path_base / "data/chunk_5.json",
    path_base / "data/chunk_6.json"
]

for file in files_to_upload:
    count = 0
    if os.path.exists(file):
        print(f"🆗 El archivo {file} existe.")
    else:
        print(f"⛔ El archivo {file} NO existe o no es un archivo válido.")
        count += 1
    if count > 0:
        raise Exception(f"No se encontraron {count} archivos para subir.")

# Función para subir archivos específicos a S3
