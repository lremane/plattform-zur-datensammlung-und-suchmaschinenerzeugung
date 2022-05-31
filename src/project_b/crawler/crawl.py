import os
import sys

# example: python3 crawl.py https://www.wikidata.org/wiki/Q10784 test
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing URL")
    elif len(sys.argv) < 3:
        print("Missing identifier")
    else:
        os.system("./apache-any23/bin/any23 rover -f ntriples " + sys.argv[1] + "> " + sys.argv[2] + ".nt")
