from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from fastembed import TextEmbedding

# -----------------------
# Setup
# -----------------------
client = QdrantClient(":memory:")

collection_name = "company_docs"

# Small local embedding model
embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

# -----------------------
# Sample texts
# -----------------------
documents = [
    {"id": 1, "text": "leave policy for employees", "department": "HR"},
    {"id": 2, "text": "salary payment and payroll issue", "department": "Finance"},
    {"id": 3, "text": "laptop and system troubleshooting", "department": "IT"},
]

# -----------------------
# Generate embeddings
# -----------------------
texts = [doc["text"] for doc in documents]
vectors = list(embedding_model.embed(texts))

vector_size = len(vectors[0])

# -----------------------
# Create collection
# -----------------------
client.create_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
)

# -----------------------
# Insert data
# -----------------------
points = []
for doc, vector in zip(documents, vectors):
    points.append(
        PointStruct(
            id=doc["id"],
            vector=vector.tolist(),
            payload={
                "text": doc["text"],
                "department": doc["department"],
            },
        )
    )

client.upsert(collection_name=collection_name, points=points)

print("Inserted real text embeddings")

# -----------------------
# Query
# -----------------------
query_text = "salary issue"
query_vector = list(embedding_model.embed([query_text]))[0]

result = client.query_points(
    collection_name=collection_name,
    query=query_vector.tolist(),
    limit=3,
)

print("\nSearch Results:")
for point in result.points:
    print(point.payload, point.score)