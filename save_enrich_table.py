import os
import weaviate
from weaviate.auth import Auth
from weaviate.classes.config import Configure
from dotenv import load_dotenv
load_dotenv()

import pandas as pd


def save_enrich_table(url: str):
    dataset = pd.read_csv(url)
    print(dataset.head())

    weaviate_url = os.environ["WEAVIATE_URL"]
    weaviate_api_key = os.environ["WEAVIATE_API_KEY"]
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=weaviate_url,
        auth_credentials=Auth.api_key(weaviate_api_key),
    )
    print(client.is_ready())  # Should print: `True`

    weviate_collection_name = url.split('/')[-1].split('.')[0]

    # remove collection if it already exists
    if client.collections.exists(weviate_collection_name):
        client.collections.delete(weviate_collection_name)

    client.collections.create(
        weviate_collection_name,
        description="A dataset that lists rows from csv",
        vector_config=Configure.Vectors.text2vec_weaviate(),
    )

    dataset_collection = client.collections.use(weviate_collection_name)

    with dataset_collection.batch.fixed_size(batch_size=200) as batch:
        for row_record in dataset.to_dict('records'):
            batch.add_object(properties=row_record)

    failed_objects = dataset_collection.batch.failed_objects
    if failed_objects:
        print(f"Number of failed imports: {len(failed_objects)}")
        print(f"First failed object: {failed_objects[0]}")
    print(f"Size of the {weviate_collection_name} dataset: {len(dataset_collection)}")

    # add german translation of row
    from weaviate.agents.classes import Operations
    from weaviate.collections.classes.config import DataType
    add_german_translation = Operations.append_property(
        property_name="german_translation",
        data_type=DataType.TEXT,
        view_properties=dataset.columns,
        instruction="Translate the row to German.",
    )

    from weaviate.agents.transformation import TransformationAgent

    agent = TransformationAgent(
        client=client,
        collection=weviate_collection_name,
        operations=[
            add_german_translation
        ],
    )
    response = agent.update_all()
    print(response)
    print(agent.get_status(workflow_id=response.workflow_id))

    client.close()  # Free up resources

if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/VladKha/cura-data/refs/heads/main/demo_data/tabular/toy_transactions.csv'
    save_enrich_table(url=url)
