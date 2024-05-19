import settings
from document_indexing import configure_pinecone,read_and_index_documents
from search import setup_search, retrieve_documents

# Read and index documents
PINECONE_ID="085adda2-3198-4495-a3f2-70e4a0d8e738"
index_name="b"
pinecone_index=configure_pinecone(PINECONE_ID,index_name)
index = read_and_index_documents("GenAI-Hackathon\Pdfs",pinecone_index)

# Setup search functionality
query_engine = setup_search(index)

# Query documents
while True:
    query = input("enter query:")
    response = retrieve_documents(query, query_engine)

    # Format and print response
    context = "Context:\n"
    for node in response.source_nodes:
        context += node.text + "\n\n"
    print(context)
