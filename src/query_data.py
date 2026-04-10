import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()

client = QdrantClient(url=os.getenv("QDRANT_URL"))
collection_name = os.getenv("COLLECTION_NAME")

result = client.query_points(
    collection_name=collection_name,
    query=[0.9, 0.8, 0.7, 0.61],
    limit=3,
)

print("Similarity Search Results:")
for point in result.points:
    print(point)