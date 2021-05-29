from azure.storage.blob import BlobServiceClient

STORAGE_CONNECTION_STRING = 'DefaultEndpointsProtocol=https;AccountName=finalstoragealik;AccountKey=gymY/VlzPuAWokj4s0jcWpjYB56UTAG3eKoiI/Q/PF+erCsE8NhauoPNGZmS5nB/jZXPWtDV/GbrXJAfwgM8aQ==;EndpointSuffix=core.windows.net'
CONTAINER_NAME = 'final'
blob_service_client = BlobServiceClient.from_connection_string(STORAGE_CONNECTION_STRING)

file_name = 'image.jpg'
test = 5
blob_name = f'image-{test}.jpg'
blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)

with open(file_name, 'rb') as f:
    blob_client.upload_blob(f)
