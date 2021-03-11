from azure.cosmos import CosmosClient, PartitionKey
import config


client = CosmosClient(config.COSMOS_DB_ENDPOINT, config.COSMOS_DB_PRIMARY_KEY)

DATABASE_NAME = 'PetsDatabase'
database = client.create_database_if_not_exists(id=DATABASE_NAME)

CONTAINER_NAME = 'PetsContainer'
container = database.create_container_if_not_exists(
    id=CONTAINER_NAME,
    partition_key=PartitionKey(path="/category"),
    offer_throughput=400
)


# LIST PETS
def get_pets():
    query = 'SELECT * FROM c'

    items = list(container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))

    return items


# CREATE PET
def create_pet(body):
    container.create_item(body=body)


# READ PET
def get_pet(item_id, partition_key):
    item_response = container.read_item(item=item_id, partition_key=partition_key)
    return item_response


# EDIT PET
def edit_pet(item_id, body):
    container.replace_item(item=item_id, body=body)


# DELETE PET
def delete_pet(item_id, partition_key):
    container.delete_item(item=item_id, partition_key=partition_key)
