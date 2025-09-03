import boto3
from utils.env import get_secrets
import time

# Obtener la configuración de secrets
secrets = get_secrets()

# Configurar CloudFront usando boto3
cloudfront_client = boto3.client(
    'cloudfront',
)

# ID de distribución de CloudFront (deberías tenerlo desde tu configuración)
cloudfront_distribution_id = secrets["AWS_CLOUDFRONT_ID"]

# Rutas de los archivos que quieres invalidar en CloudFront
files_to_invalidate = [
    "/etl/chunk_1.json",
    "/etl/chunk_2.json",
    "/etl/chunk_3.json",
    "/etl/chunk_4.json",
    "/etl/chunk_5.json",
    "/etl/chunk_6.json",
    "/etl/isolation_forest_model.pkl"
]


def invalidate_cache(distribution_id, paths_to_invalidate):
    """Solicita la invalidación de los archivos cacheados en CloudFront."""
    try:
        # Crear una solicitud de invalidación
        invalidation_batch = {
            'Paths': {
                'Quantity': len(paths_to_invalidate),
                'Items': paths_to_invalidate
            },
            'CallerReference': str(time.time())  # Usamos el tiempo actual como referencia única
        }

        # Enviar solicitud de invalidación
        response = cloudfront_client.create_invalidation(
            DistributionId=distribution_id,
            InvalidationBatch=invalidation_batch
        )

        # Mostrar el ID de la invalidación para seguimiento
        print(f"Invalidación solicitada con ID: {response['Invalidation']['Id']}")
        return response

    except Exception as e:
        print(f"Error al solicitar la invalidación de la caché: {e}")
        raise


if __name__ == "__main__":
    # Llamar a la función de invalidación con las rutas que deseas invalidar
    invalidate_cache(cloudfront_distribution_id, files_to_invalidate)
