import boto3
import os
from utils.env import get_secrets
from pathlib import Path

path_base = Path(__file__).resolve().parents[1]

secrets = get_secrets()

s3_client = boto3.client("s3")

files_to_upload = [
    path_base / "models/isolation_forest_model.pkl",
    path_base / "data/chunk_1.json",
    path_base / "data/chunk_2.json",
    path_base / "data/chunk_3.json",
    path_base / "data/chunk_4.json",
    path_base / "data/chunk_5.json",
    path_base / "data/chunk_6.json"
]

count = 0
for file in files_to_upload:
    if os.path.exists(file):
        print(f"🆗 El archivo {file} existe.")
    else:
        print(f"⛔ El archivo {file} NO existe o no es un archivo válido.")
        count += 1
if count > 0:
    raise Exception(f"No se encontraron {count} archivos para subir.")


def get_content_type_and_disposition(file_path):
    if file_path.endswith(".json"):
        return "application/json", "inline"
    elif file_path.endswith(".csv"):
        return "text/csv", "inline"
    elif file_path.endswith(".pkl"):
        return "application/octet-stream", "attachment"
    else:
        return "application/octet-stream", "attachment"


def upload_files_to_s3(files):
    for file_path in files:
        file_name = os.path.basename(file_path)

        s3_file_path = os.path.join("etl", file_name).replace(os.sep, "/")

        content_type, content_disposition = get_content_type_and_disposition(str(file_path))

        try:
            print(f"Subiendo {file_name} a S3...")

            s3_client.upload_file(
                str(file_path),
                secrets["AWS_S3_BUCKET"],
                s3_file_path,
                ExtraArgs={
                    "ContentType": content_type,
                    "ContentDisposition": content_disposition
                }
            )
            print(f"✅ Archivo {file_name} subido exitosamente.")
        except Exception as e:
            print(f"❌ Error al subir {file_name} a S3: {e}")


if __name__ == "__main__":
    upload_files_to_s3(files_to_upload)
