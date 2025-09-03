import boto3
from utils.env import get_secrets
import time

secrets = get_secrets()

cloudfront_client = boto3.client(
    'cloudfront',
)

cloudfront_distribution_id = secrets["AWS_CLOUDFRONT_ID"]

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
    try:
        invalidation_batch = {
            'Paths': {
                'Quantity': len(paths_to_invalidate),
                'Items': paths_to_invalidate
            },
            'CallerReference': str(time.time())
        }

        response = cloudfront_client.create_invalidation(
            DistributionId=distribution_id,
            InvalidationBatch=invalidation_batch
        )

        print(f"Invalidación solicitada con ID: {response['Invalidation']['Id']}")
        return response

    except Exception as e:
        print(f"Error al solicitar la invalidación de la caché: {e}")
        raise


if __name__ == "__main__":
    invalidate_cache(cloudfront_distribution_id, files_to_invalidate)
