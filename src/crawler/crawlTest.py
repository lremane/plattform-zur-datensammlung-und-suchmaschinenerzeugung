import rdfaCrawler

if __name__ == "__main__":
    crawler = rdfaCrawler.rdfaCrawler()
    crawler.parseRdfa(site = "https://www.wikidata.org/wiki/Q2079", name = "test")
    