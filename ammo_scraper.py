import requests
from bs4 import BeautifulSoup
import csv
import time


class MyParser:
    def __init__(self, url: str):
        self.url = url
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.content, 'lxml')

    def find_names(self) -> list[BeautifulSoup]:
        # Find all elements names with class "link-overlay"
        return self.soup.find_all('a', class_='link-overlay')

    def find_divs(self) -> list[BeautifulSoup]:
        # Find all div elements with class "price"
        return self.soup.find_all('div', class_='price')

    def find_links(self) -> list[str]:
        # Find all href attributes of "link-overlay" class
        base_url = 'https://www.jahipaun.ee/'
        links = [base_url + link.get('href').lstrip('/') for link in self.soup.find_all('a', class_='link-overlay')]
        return links

    def match_check(self, name_elements, price_elements, link_elements):
        # Make sure we have the same number of names, prices, and links
        assert len(name_elements) == len(price_elements) == len(link_elements), "Mismatch in number of names, prices, and links"

    def zip_ammo(self, name_elements, price_elements, link_elements):
        ammo_list = []
        for name_elem, price_elem, link_elem in zip(name_elements, price_elements, link_elements):
            name = name_elem.get('title', 'Name not found')
            price = price_elem.text.strip()
            link = link_elem
            ammo_list.append({'name': name, 'price': price, 'link': link})
        return ammo_list

    def save_ammo_in_csv(self, ammo_list: list[dict], filename: str):
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'price', 'link']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for ammo in ammo_list:
                writer.writerow(ammo)

    def add_time(self: 'MyParser') -> tuple[str, int]:
        current_time = time.localtime()
        day = current_time.tm_mday
        month = time.strftime('%B', current_time)
        return month, day


if __name__ == '__main__':
    urls = {
        'handgun': 'https://www.jahipaun.ee/en/online-shop/kategooria/ammo/handgun/show-500/online-shop/basket-price',
        'shotgun': 'https://www.jahipaun.ee/en/online-shop/kategooria/ammo/shotgun/show-500/online-shop/basket-price',
        'rifle': 'https://www.jahipaun.ee/en/online-shop/kategooria/ammo/rifle/show-500/online-shop/basket-price',
        'smallbore': 'https://www.jahipaun.ee/en/online-shop/kategooria/ammo/smallbore/show-500/online-shop/basket-price'
    }

    for ammo_type, url in urls.items():
        parser = MyParser(url)

        name_elements = parser.find_names()
        price_elements = parser.find_divs()
        link_elements = parser.find_links()
        parser.match_check(name_elements, price_elements, link_elements)

        ammo_list = parser.zip_ammo(name_elements, price_elements, link_elements)

        month, day = parser.add_time()
        filename = f"{ammo_type}_ammo_{month}_{day}.csv"
        parser.save_ammo_in_csv(ammo_list, filename)
