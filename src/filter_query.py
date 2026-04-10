import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue

load_dotenv()

client = QdrantClient(url=os.getenv("QDRANT_URL"))
collection_name = os.getenv("COLLECTION_NAME")

result = client.query_points(
    collection_name=collection_name,
    query=[0.1, 0.2, 0.3, 0.39],
    query_filter=Filter(
        must=[
            FieldCondition(
                key="department",
                match=MatchValue(value="HR")
            )
        ]
    ),
    limit=3,
)

print("Filtered Search Results:")
for point in result.points:
    print(point)