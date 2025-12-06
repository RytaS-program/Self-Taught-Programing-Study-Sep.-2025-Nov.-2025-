import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,site):
        self.site=site

    def scrape(self):
        response=urllib.request.urlopen(self.site)
        html=response.read()
        soup=BeautifulSoup(html,'html.parser')
        with open("output.txt","w") as f:
            for tag in soup.find_all("a"):
                url=tag.get("href")
                if not url:
                    continue
                if "read"in url:
                    full_url=urllib.parse.urljoin(self.site,url)
                    print(full_url)
                    f.write(full_url+"\n")

Scraper("https://news.google.com").scrape()
