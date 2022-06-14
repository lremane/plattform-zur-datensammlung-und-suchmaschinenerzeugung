import requests


class RdfaCrawler:

    @staticmethod
    def get_rdfa(site: str) -> str:

        req = requests.get(f"http://www.w3.org/2012/pyRdfa/extract?format=nt&uri={site}")

        if req.status_code == 200:
            return req.text
        else:
            print("Error")
