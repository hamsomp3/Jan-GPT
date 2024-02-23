# docs chroma https://docs.trychroma.com/usage-guide 

import chromadb
from chromadb.config import Settings
from chromadb.server.fastapi import FastAPI
settings = Settings()
client = chromadb.PersistentClient(path="./data/chroma_data")
server = FastAPI(settings)
app = server.app