import requests
from bs4 import BeautifulSoup
import time
import os

url = 'https://www.jahipaun.ee/en/online-shop/kategooria/ammo/handgun/show-500/online-shop/basket-price'


def find_image_link(soup):
    image_element = soup.find('img', class_='product-image')
    if image_element:
        image_link = 'https://www.jahipaun.ee/' + image_element.get('src')
        return image_link
    return None


def save_image(image_link):
    if image_link:
        image_name = 'handgun_image.jpg'
        image_path = f'images/{image_name}'
        os.makedirs('images', exist_ok=True)
        response = requests.get(image_link)
        with open(image_path, 'wb') as file:
            file.write(response.content)
        print(f'Image saved to: {image_path}')
    else:
        print('Image not found or unable to save.')


def main():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    image_link = find_image_link(soup)
    time.sleep(5)  # Add a 5-second delay
    save_image(image_link)


if __name__ == '__main__':
    main()
