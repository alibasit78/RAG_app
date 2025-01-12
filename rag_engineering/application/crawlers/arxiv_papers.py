import os
from tempfile import mkdtemp

import arxiv
import requests
from loguru import logger
from PyPDF2 import PdfReader

# from .base import BaseCrawler
from rag_engineering.application.crawlers.base import BaseCrawler
from rag_engineering.domain.documents import ArxivDocument, UserDocument


class ArxivCrawler(BaseCrawler):
    model = ArxivDocument
    def __init__(self):
        super().__init__()
        # pass
    
    def extract(self, query: str = None, **kwargs):
        # print(dir(arxiv))
        search = arxiv.Search(
            query=query,
            max_results=1,  # Limiting to one result for demonstration
            sort_by=arxiv.SortCriterion.Relevance,
            sort_order=arxiv.SortOrder.Descending
        )
        for result in search.results():
            kwargs['title'] = result.title
            self.extract_page(link=result.pdf_url, **kwargs)    
    
    def extract_page(self, link:str, **kwargs):
        logger.info(f"Starting scraping from the arxiv: {link}")
        # repo_name = arxiv_result.title
        title = kwargs['title']
        pdf_response = requests.get(link)
        pdf_filename = f"{title.replace(':', '').replace(' ', '_')}.pdf"
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
        user = kwargs['user']
        data = {"title": title, "content": main_content}
        # print(self.model)
        instance = self.model(
            platform = "arxiv",
            content = data,
            link = link,
            author_id = user.id,
            author_full_name = user.full_name            
        )
        instance.save()
        logger.info(f'successfully scraped and saved arxiv paper- {title}')


if __name__ == "__main__":
    user = UserDocument.get_or_create(first_name = "Basit", last_name = "Ali")
    arxiv_crawler = ArxivCrawler()
    arxiv_crawler.extract(query="transformer attention all you need", user=user)