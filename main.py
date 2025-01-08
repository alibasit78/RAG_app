from rag_engineering.application.crawlers.linkedin import LinkedinCrawler

if __name__ == "__main__":
    linkedin_crawler = LinkedinCrawler(is_deprecated=False)
    link = r"https://www.linkedin.com/feed/"
    linkedin_crawler.extract(link=link)