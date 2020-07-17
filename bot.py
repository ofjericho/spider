
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


class Spider:
    def __init__(self, url):
        self.url = url

    def extract(self, field):
        req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        # webpage = web_byte.decode('utf-8')
        soup = BeautifulSoup(web_byte, 'html.parser')

        return soup.find(id=field)['value']


if __name__ == "__main__":

    dolar_comercial = Spider(
        'https://www.melhorcambio.com/dolar-hoje').extract('comercial')

    euro_comercial = Spider(
        'https://www.melhorcambio.com/euro-hoje').extract('comercial')

    print(dolar_comercial)
    print(euro_comercial)
