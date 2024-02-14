# docs chroma https://docs.trychroma.com/usage-guide 

# #Server.py cambiar elnombre
# from fastapi import FastAPI
# import chromadb
# from chroma.server import configure_app
# from chroma.server.models import Settings

# settings = Settings(
#     chroma_db_impl="duckdb+parquet",
#     persist_directory="chroma_data",
# )

# # Se usa la nueva función `configure_app`
# app = configure_app(settings)

# server = FastAPI(app=app)


# # Se inicia el servidor FastAPI
# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(server, port=8000)

# # server.py
# import chromadb
# from chromadb.server.fastapi import FastAPI

# settings = chromadb.PersistentClient(path="chroma_data")
# server = FastAPI(settings)
# app = server.app

# # server.py
# import chromadb
# import chromadb.config
# from chromadb.server.fastapi import FastAPI

# settings = chromadb.config.Settings(
#     chroma_db_impl="duckdb+parquet", 
#     persist_directory='chroma_data'
# )
# server = FastAPI(settings)
# app = server.app


import chromadb
from chromadb.config import Settings
from chromadb.server.fastapi import FastAPI
# client = chromadb.Client() # this options is for in-memory database

# settings = Settings(chroma_db_impl="duckdb+parquet", persist_directory="chroma_data")
client = chromadb.PersistentClient(path="./data/chroma_data")

# client.heartbeat() # returns a nanosecond heartbeat. Useful for making sure the client remains connected.
# client.reset() # Empties and completely resets the database. ⚠️ This is destructive and not reversible.

# server = FastAPI(client)
# app = server.app
