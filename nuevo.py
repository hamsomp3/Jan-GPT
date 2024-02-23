import chromadb
from chromadb.utils import embedding_functions

client = chromadb.HttpClient(host="localhost", port=8000)
print(client.get_version())

embedder = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

collection = client.create_collection(
    name="test",
    embedding_function=embedder,
    get_or_create=True
)

collection = client.get_collection(name="test",embedding_function=embedder)


import pandas as pd
import wikipedia


def get_wikipedia_summary(name):
    try: 
        summary = wikipedia.summary(name + ' company')
    except Exception:
        summary = None
    finally:
        return summary

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

df = pd.read_html(url, attrs = {"id": "constituents"}, flavor='lxml')[0]
df['company_summary'] = df['Security'].apply(lambda x: get_wikipedia_summary(x))

df.head()