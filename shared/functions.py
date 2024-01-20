from langchain_community.document_loaders import PyPDFium2Loader
from .variables import DEFAULT_PDF_URL

def load_pdf_from_url(url=DEFAULT_PDF_URL):
    # Your code here
    loader = PyPDFium2Loader(url)
    return loader.load()
