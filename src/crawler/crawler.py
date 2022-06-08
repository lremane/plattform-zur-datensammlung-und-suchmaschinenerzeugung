import os
import sys


class Crawler:
    def __init__(self, site : str, name : str):
        if self.crawlInit() == True:
            self.crawlSite(site, name)

    def crawlSite(self, site : str, name : str) -> None:
        os.system("./apache-any23/bin/any23 rover -e rdf-jsonld,rdf-nq,rdf-nt,rdf-trix,rdf-turtle,rdf-xml,html-rdfa11 -f ntriples -l ./logs/"+  name + ".log " + site + "> ./rdfData/" + name + ".nt")
        print("Crawled: " + site)
        print("Generated: ./logs/" + name + ".log ./rdfData/" + name + ".nt")

    def crawlInit(self) -> bool:
        os.system("./init.sh")
        if len(sys.argv) < 2:
            print("Missing URL")
            return False
        elif len(sys.argv) < 3:
            print("Missing identifier")
            return False
        return True

# if __name__ == "__main__":
#     Crawler = Crawler(sys.argv[1], sys.argv[2])



