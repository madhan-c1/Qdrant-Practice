import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

load_dotenv()

client = QdrantClient(url=os.getenv("QDRANT_URL"))
collection_name = os.getenv("COLLECTION_NAME")

points = [
    PointStruct(
        id=1,
        vector=[0.1, 0.2, 0.3, 0.4],
        payload={"department": "HR", "topic": "leave policy"},
    ),
    PointStruct(
        id=2,
        vector=[0.9, 0.8, 0.7, 0.6],
        payload={"department": "Finance", "topic": "salary"},
    ),
    PointStruct(
        id=3,
        vector=[0.15, 0.25, 0.35, 0.45],
        payload={"department": "IT", "topic": "laptop issue"},
    ),
]

client.upsert(
    collection_name=collection_name,
    points=points,
)

print("Data inserted successfully")