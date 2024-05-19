import settings
from document_indexing import read_and_index_documents
from search import setup_search, retrieve_documents

# Read and index documents
index = read_and_index_documents("../articles")

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
