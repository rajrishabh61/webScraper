from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import csv 
class webScrape():
    def __init__(self):
        
        with open('books.csv', 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)  
            writer.writerow(['TITLE', 'URL', 'PRICE', 'AVAILABILITY']) 
            
    def add_in_csv(self, row):
        # Append new row (don’t overwrite old data)
        with open('books.csv', 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(row)

    def scrape(self,url):
        url = "https://books.toscrape.com/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        seen = set()  # to track duplicates

        for book in soup.find_all(class_='product_pod'):
            title = book.h3.a['title']                     # book title
            relative_url = book.h3.a['href']               # relative link
            price = book.find('p', class_='price_color').text
            availability = book.find('p', class_='instock availability').text.strip()
            full_url = urljoin(url, relative_url)          # make absolute link
            if full_url not in seen:  # skip duplicates
                seen.add(full_url)
                self.add_in_csv([title, full_url, price, availability])  # write one row
                print(title, " || ", full_url, " || ", price, " || ", availability)

obj = webScrape()
obj.scrape()
