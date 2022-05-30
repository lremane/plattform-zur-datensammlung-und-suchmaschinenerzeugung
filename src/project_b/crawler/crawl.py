import os
import sys

# example: python3 crawl.py https://www.wikidata.org/wiki/Q10784 test

def crawlSite(site : str, name : str) -> None:
    os.system("./apache-any23/bin/any23 rover -e rdf-jsonld,rdf-nq,rdf-nt,rdf-trix,rdf-turtle,rdf-xml,html-rdfa11 -f ntriples -l ./logs/"+  name + ".log " + site + "> ./rdfData/" + name + ".nt")
    print("Crawled: " + site)
    print("Generated: ./logs/" + name + ".log ./rdfData/" + name + ".nt")

def crawlInit() -> bool:
    os.system("./init.sh")
    if len(sys.argv) < 2:
        print("Missing URL")
        return False
    elif len(sys.argv) < 3:
        print("Missing identifier")
        return False
    return True

if __name__ == "__main__":
    if crawlInit() == True:
        crawlSite(sys.argv[1], sys.argv[2])

