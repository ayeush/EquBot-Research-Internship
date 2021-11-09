from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

root = 'https://www.google.com/'
link = 'https://www.google.com/search?q=interest+rate&tbs=sbd:1,qdr:y&tbm=nws&sxsrf=AOaemvK49p6VXILZacIiSWroz9cghJ0uag:1636422498488&source=lnt&sa=X&ved=2ahUKEwjCu-XtlIr0AhXdFzQIHRi2AeUQpwV6BAgBECQ&biw=1440&bih=695&dpr=1'

def newsscrape(link):
    req = Request(link, headers={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    with requests.session() as c:
        soup = BeautifulSoup(webpage, 'html5lib')
        for item in soup.find_all('div', attrs={'class': 'ZINbbc xpd O9g5cc uUPGi'}):
            raw_link = item.find('a', href=True)['href']
            link = (raw_link.split('/url?q=')[1]).split('&sa=U&')[0]
            title = (item.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'})).get_text()
            title = title.replace(',', '')
            description = (item.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})).get_text()
            description = description.replace(',', '')
            descripttime = description.split("·")[0]
            descripttime = descripttime.replace(',', '')
            descripttext = description.split("·")[1]
            descripttext = descripttext.replace(',', '')
            print(title)
            print(descripttime)
            print(descripttext)
            print(link)
            document = open('data.csv', 'a')
            document.write('{}, {}, {}, {} \n'.format(title, descripttime, descripttext, link))
            document.close()
        next = soup.find('a', attrs={'aria-label': 'Next page'})
        next = next['href']
        link = root + next
        newsscrape(link)
newsscrape(link)
