# mini-rag

A small starter project for retrieval-augmented generation (RAG) question answering.

## Requirements

- Python 3.12 (the version used for local setup)
- Conda, or another Python environment manager

The project dependencies are pinned in [`src/requirements.txt`](src/requirements.txt):

- **FastAPI** — web API framework
- **Uvicorn** — ASGI server
- **python-multipart** — multipart form-data parsing

## Setup

Create and activate a Conda environment, then install the project dependencies:

```bash
conda create -n mini-rag python=3.12
conda activate mini-rag
python -m pip install -r src/requirements.txt
```

To install the dependencies in an already active Python environment:

```bash
python -m pip install -r src/requirements.txt
```

## Running

From the repository root, start the FastAPI server with:

```bash
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 5000
```

## Installation

### Install the required packages

```bash
python -m pip install -r src/requirements.txt
```

### Run the FastAPI server

> 💡

```bash
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 5000
```

### POSTMAN Collection

> 💡

Download the POSTMAN collection from [/assets/mini-rag.postman_collection.json](/assets/mini-rag.postman_collection.json)

---
