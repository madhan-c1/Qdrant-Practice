import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client = QdrantClient(url=QDRANT_URL)

client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(size=4, distance=Distance.COSINE),
)

print(f"Collection '{COLLECTION_NAME}' created successfully")