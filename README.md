# Qdrant Semantic Search Practice 🚀

A beginner-friendly hands-on project to learn **vector databases, embeddings, semantic search, and metadata filtering** using **Qdrant + Python**.

This project was built as part of an **AI Engineering learning roadmap** to understand how modern **RAG (Retrieval-Augmented Generation)** systems work.

---

# 📌 What This Project Covers

This project demonstrates:

* Setting up **Qdrant locally**
* Creating a **collection**
* Storing vectors with **payload metadata**
* Running **cosine similarity search**
* Running **metadata-filtered search**
* Using **real text embeddings**
* Understanding **RAM vs persistent storage**
* Foundation concepts for **semantic search and RAG**

---

# 🧠 Core Concepts Covered

## 1. Embeddings

Embeddings convert text into numerical vectors that capture semantic meaning.

Example:

```text
"salary issue" → [0.12, 0.88, 0.31, ...]
```

Similar meanings stay close in vector space.

Example:

```text
salary issue
payroll problem
billing failed
```

These are expected to have similar vectors.

---

## 2. Vector Database

Unlike traditional SQL databases that store rows and columns, Qdrant stores:

```text
id | vector | payload
```

Example:

```text
1 | [0.1, 0.2, 0.3] | {"department": "HR"}
```

This allows **semantic similarity search**.

---

## 3. Cosine Similarity

Qdrant compares vectors using cosine similarity.

Formula:

```text
similarity = (A · B) / (|A| |B|)
```

Higher score → more similar meaning.

---

# 📁 Project Structure

```text
qdrant-practice/
│
├── requirements.txt
├── .env
├── docker-compose.yml
├── main.py
├── insert_data.py
├── query_data.py
├── filter_query.py
├── real_embedding_search.py
└── README.md
```

---

# ⚙️ Setup Instructions

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Local Qdrant (Persistent Storage)

```bash
docker run -p 6333:6333 -p 6334:6334 -v "$(pwd)/qdrant_storage:/qdrant/storage:z" qdrant/qdrant
```

This starts a local Qdrant server using Docker.

---

# 💾 Qdrant Storage Flow

This project supports **two storage modes**.

---

## 1) In-Memory Mode (Learning / Testing)

```python
client = QdrantClient(":memory:")
```

### Where data is stored

* stored in **RAM**
* temporary
* deleted when script ends

Best for:

* learning
* experiments
* testing embeddings

---

## 2) Persistent Local Storage (Recommended)

```python
client = QdrantClient(url="http://localhost:6333")
```

With Docker:

```yaml
volumes:
  - qdrant_storage:/qdrant/storage
```

### Storage flow

```text
Python App
   ↓
Qdrant Client
   ↓
Local Qdrant Server
   ↓
Docker Volume
   ↓
Disk Storage
```

This means data persists across restarts.

---

# 🔄 End-to-End Flow

```text
Text
   ↓
Embedding Model
   ↓
Vector Representation
   ↓
Store in Qdrant
   ↓
Similarity Search
   ↓
Top Matching Results
```

This is the base workflow of **RAG systems**.

---

# 🔍 Example Semantic Search Flow

Query:

```text
salary issue
```

System flow:

```text
Query text
   ↓
Embedding vector
   ↓
Cosine similarity search
   ↓
Finance chunk returned
```

Example output:

```text
Finance → 0.99998
IT       → 0.87764
HR       → 0.84529
```

---

# 🏷️ Metadata Filtering

This project also supports payload filtering.

Example:

```python
query_filter=Filter(
    must=[
        FieldCondition(
            key="department",
            match=MatchValue(value="HR")
        )
    ]
)
```

This restricts results to only the selected department.

---

# 🧪 Sample Use Cases

* HR policy search
* finance document retrieval
* IT issue knowledge base
* internal company assistant
* semantic search practice
* RAG foundation learning

---

# 🎯 Learning Outcome

By completing this project, I understood:

* how embeddings work
* how vector databases store meaning
* cosine similarity in practice
* metadata filtering
* difference between RAM and persistent storage
* how semantic search powers AI assistants

---

# 🚀 Future Improvements

Planned next steps:

* integrate with OpenAI / local embedding models
* build mini RAG chatbot
* connect with FastAPI / NestJS backend
* add document chunking pipeline
* integrate with PDF ingestion

---

# 👨‍💻 Author

Built by **Madhan** as part of GenAI hands-on practice.

# start qdrant
Docker compose up -d

# install packages
pip install -r requirements.txt

# create collection
python main.py

# insert data
python insert_data.py

# normal query
python query_data.py

# metadata filter query
python filter_query.py


