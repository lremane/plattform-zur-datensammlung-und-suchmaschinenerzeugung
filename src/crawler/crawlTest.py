import RdfaCrawler

if __name__ == "__main__":
    crawler = rdfaCrawler.RdfaCrawler()
    crawler.get_rdfa(site ="https://www.wikidata.org/wiki/Q2079", name ="test")
