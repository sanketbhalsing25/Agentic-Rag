from langchain_community.document_loaders import TextLoader,PyPDFLoader
def load_documents(path: str):
    if path.endswith(".pdf"):
        loader = PyPDFLoader(path)
    else:
        loader = TextLoader(path)
    return loader.load()