from minio import Minio

# Cliente MinIO
client = Minio(
    "minio:9000",
    access_key="admin",
    secret_key="admin123",
    secure=False
)

bucket_name = "datos"

# Crear bucket si no existe
if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)

# Nombre del archivo local
file_path = "pedestrian-counting-system-monthly-counts-per-hour.parquet"

# Subir parquet a MinIO
client.fput_object(bucket_name, file_path, file_path)

print(f" Archivo '{file_path}' subido al bucket '{bucket_name}' en MinIO")
