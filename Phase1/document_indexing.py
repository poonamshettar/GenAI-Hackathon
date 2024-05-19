from llama_index.core import SimpleDirectoryReader, VectorStoreIndex


def read_and_index_documents(directory):
    documents = SimpleDirectoryReader(directory).load_data()
    # Additional document refinement
    refined_documents = []
    for doc in documents:
        if (
            "Member-only story" in doc.text
            or "The Data Entrepreneurs" in doc.text
            or " min read" in doc.text
        ):
            continue
        refined_documents.append(doc)

    index = VectorStoreIndex.from_documents(refined_documents)
    return index
