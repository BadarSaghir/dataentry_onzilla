# from time import sleep
from bs4 import BeautifulSoup
import requests
from constants import SCRAPING_URL
# import lxml


class ZillowScraper:
    def __init__(self, url: str = SCRAPING_URL):
        self.url = SCRAPING_URL
        headers = {'accept': '*/*',
                   'accept-encoding': 'gzip, deflate, br',
                   'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7,la;q=0.6',
                   'cache-control': 'no-cache',
                   'dnt': '1',
                   'pragma': 'no-cache',
                   'referer': 'https',
                   'sec-fetch-mode': 'no-cors',
                   'sec-fetch-site': 'cross-site',
                   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
                   }

        response = requests.get(SCRAPING_URL, headers=headers)
        response.raise_for_status()
        # sleep(3)
        self.soup = BeautifulSoup(response.text, 'html.parser')
        # print(self.soup)

    def scrap_now(self) -> dict:
        data = {'addresses': [add.text for add in self.soup.select('address')]}
        price = [price.get_text().split("+")[0] for price in self.soup.select(".list-card-details li") if "$" in price.text]
        data['prices'] = price
        links = [link.attrs['href'] for link in self.soup.select('.list-card-top a')]
        for link in range(0, len(links)):
            if links[link][0]== '/':
                links[link]='https://www.zillow.com'+links[link]

        data['links']=links
        for i in data['prices']:
            print(i)
        print(len(data['prices']), len(data['addresses']), len(data['links']))
        return data
