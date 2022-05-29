import os
import sys

# any23 must be installed and added to PATH
# add to project and switch to relativ path?

# example: python3 crawl.py https://www.wikidata.org/wiki/Q10784 test
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing URL")
    elif len(sys.argv) < 3:
        print("Missing identifier")
    else:
        os.system("any23 rover -f ntriples " + sys.argv[1] + "> " + sys.argv[2] + ".nt")


