import requests
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import pandas as pd

data = []
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
def get_data(url,headers):
    req = Request(url, headers=headers)
    webpage = urlopen(req).read()
    ## Testing
    # webpage = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(webpage, "html.parser")
    links = soup.find_all('li', class_="item")
    for a in links:
        #link = []
        for l in a.find_all('a', class_="border", href=True):
            link = l['href']
        items = a.find_all(class_="item-detail")
        for item in items:
            info = {
                "Title" : item.find('h2', class_="item-title").text,
                "Price" : item.find('span', class_="price").text,
                "Location": item.find('ul', class_="list-unstyled").find('li').text,
                "Description": item.find('p', class_="description").text,
                "Posted_time": item.find('ul', class_="list-unstyled").find('time').text,
                # "Tel": item.find('p', class_="description").find('i').text,
                "link": link
            }
            data.append(info)
    return data
def export_data(data):
    df = pd.DataFrame(data)
    print(df)
    # df.to_excel("ABCKh24.xlsx")

if __name__ == '__main__':
    pages = int(input('How many pages do you want to scrap? : '))
    for page in range(0, pages):
        data = get_data(f"https://www.khmer24.com/en/c-computer-and-accessories.html?per_page={pages * 50}",headers)

        # data = get_data(f"https://www.khmer24.com/en/c-computer-and-accessories.html?per_page={pages * 50}", headers)
    export_data(data)
    print("done")
        # data = get_data(f"https://www.khmer24.com/en/property/search.html?q=&category=house-for-rent&location=&per_page={pages}",headers)
