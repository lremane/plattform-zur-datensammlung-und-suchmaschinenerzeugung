import os
import sys
import requests

class rdfaCrawler:

    def parseRdfa(self, site : str, name : str) -> None:

        if not os.path.exists("./rdfData"):
            os.mkdir("./rdfData")

        data = requests.get("http://www.w3.org/2012/pyRdfa/extract?format=nt&uri={}".format(site))
        
        if data.status_code == 200:

            with open("./rdfData/{}.nt".format(name), "w") as file:
                file.write(str(data.content, encoding='utf-8'))

        else:
            print("Error")