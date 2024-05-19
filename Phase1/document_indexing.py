from pinecone import Pinecone,ServerlessSpec
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core.indices.vector_store.base import VectorStoreIndex
from llama_index.core import SimpleDirectoryReader,StorageContext

def configure_pinecone(PINECONE_ID,index_name):
    pinecone=Pinecone(api_key=PINECONE_ID)
    if index_name not in pinecone.list_indexes().names():
        pinecone.create_index(
        name=index_name,
        dimension=2,
        metric="cosine",
        spec=ServerlessSpec(
          cloud='aws', 
          region='us-east-1'
        ) 
    ) 
    pinecone_index=pinecone.Index(index_name)
    return pinecone_index


def read_and_index_documents(directory,pinecone_index):
    documents = SimpleDirectoryReader(directory).load_data()
    vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context
    )
    return index
