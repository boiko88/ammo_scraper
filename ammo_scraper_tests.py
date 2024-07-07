import unittest

if __name__ == '__main__':
    from ammo_scraper import MyParser

    class TestMyParser(unittest.TestCase):
        def test_url_validation(self):
            url = 'https://www.jahipaun.ee/en/online-shop/kategooria/ammo/handgun/show-500/online-shop/basket-price'
            parser = MyParser(url)
            self.assertEqual(parser.response.status_code, 200)

        def test_html_parsing(self):
            url = 'https://www.jahipaun.ee/en/online-shop/kategooria/ammo/handgun/show-500/online-shop/basket-price'
            parser = MyParser(url)
            name_elements = parser.find_names()
            price_elements = parser.find_divs()
            link_elements = parser.find_links()
            self.assertGreater(len(name_elements), 0)
            self.assertGreater(len(price_elements), 0)
            self.assertGreater(len(link_elements), 0)

        def test_data_extraction(self):
            url = 'https://www.jahipaun.ee/en/online-shop/kategooria/ammo/handgun/show-500/online-shop/basket-price'
            parser = MyParser(url)
            name_elements = parser.find_names()
            price_elements = parser.find_divs()
            link_elements = parser.find_links()
            ammo_list = parser.zip_ammo(name_elements, price_elements, link_elements)
            self.assertIn('name', ammo_list[0])
            self.assertIn('price', ammo_list[0])
            self.assertIn('link', ammo_list[0])

        def test_filename_generation(self):
            url = 'https://www.jahipaun.ee/en/online-shop/kategooria/ammo/handgun/show-500/online-shop/basket-price'
            parser = MyParser(url)
            month, day = parser.add_time()
            filename = f"handgun_ammo_{month}_{day}.csv"
            self.assertEqual(filename, "handgun_ammo_July_7.csv")  # Assuming today is July 7th

    unittest.main()
