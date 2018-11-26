import requests
from bs4 import BeautifulSoup 

def get_html(url):
    r = requests.get(url)
    return r.text

def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    tds = soup.find('div', class_ = 'news-list').find_all('h4') 

    links = []

    for td in tds:
        a = td.find('a').get('href')
        #link = 'https://coinmarketcap.com' + a 
        links.append(a)
    return links

def main():
    url = 'https://pythondigest.ru/feed/'

    all_links = get_all_links(get_html(url))

    for i in all_links:
        print i
    #print(len(all_links))    
        


if __name__ == '__main__':
    main()