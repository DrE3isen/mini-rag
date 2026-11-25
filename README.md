# mini-rag

A small starter project for retrieval-augmented generation (RAG) question answering.

## Requirements

- Python 3.12 (the version used for local setup)
- Conda, or another Python environment manager

The project dependencies are pinned in [`requirements.txt`](requirements.txt):

- **FastAPI** — web API framework
- **Uvicorn** — ASGI server
- **python-multipart** — multipart form-data parsing

## Setup

Create and activate a Conda environment, then install the project dependencies:

```bash
conda create -n mini-rag python=3.12
conda activate mini-rag
python -m pip install -r requirements.txt
```

To install the dependencies in an already active Python environment:

```bash
python -m pip install -r requirements.txt
```

## Running

This repository currently contains the dependency setup but does not yet include an application entry point or API routes to run.

## Installation

### Install the required packages

```bash
pip install -r requirements.txt
## Run the FastAPI server
💡
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
