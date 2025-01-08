import os
from tempfile import mkdtemp

import arxiv
import requests
from loguru import logger
from PyPDF2 import PdfReader

from rag_engineering.domain.documents import ArxivDocument

from .base import BaseCrawler


class ArxivCrawler(BaseCrawler):
    model = ArxivDocument
    def __init__(self):
        super().__init__()
    
    def extract(self, link:str, **kwargs):
        logger.info(f"Starting scraping from the arxiv: {link}")
        # repo_name = arxiv_result.title
        repo_name = kwargs['title']
        pdf_response = requests.get(link)
        pdf_filename = f"{repo_name.replace(':', '').replace(' ', '_')}.pdf"
        local_temp = mkdtemp()
        with open(os.path.join(local_temp, pdf_filename), "wb") as pdf_file:
            pdf_file.write(pdf_response.content)
            # pdf_file.write(pdf_response.text)
        logger.info(f"Downloaded PDF: {pdf_filename}")
        # Extract text from the PDF
        reader = PdfReader(os.path.join(local_temp, pdf_filename))
        main_content = ""
        for page in reader.pages:
            main_content += page.extract_text()
        
        
        
        
    