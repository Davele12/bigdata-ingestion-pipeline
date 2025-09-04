from minio import Minio

# Conectar al MinIO
client = Minio(
    "minio:9000",
    access_key="admin",
    secret_key="admin123",
    secure=False
)

bucket_name = "datos"

# Listar archivos en el bucket
objects = list(client.list_objects(bucket_name))
print(f" El bucket '{bucket_name}' contiene {len(objects)} archivo(s):")
for obj in objects:
    print(" -", obj.object_name)
