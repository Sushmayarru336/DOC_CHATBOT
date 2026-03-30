import tempfile
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader

def load_files(files):
    documents = []

    for file in files:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(file.read())
            path = tmp.name

        if file.type == "application/pdf":
            loader = PyPDFLoader(path)
        elif file.type == "text/plain":
            loader = TextLoader(path)
        else:
            loader = Docx2txtLoader(path)

        documents.extend(loader.load())

    return documents