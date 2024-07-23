This Python scraper extracts data and images from the website https://www.jahipaun.ee/en. It saves hundreds of images in four separate folders named "handguns", "rifle", "shotgun", and "smallbore". Additionally, it generates CSV files containing the scraped data and includes unit tests in a separate file.

Installation
Clone the repository to your local machine - git clone https://github.com/boiko88/ammo_scraper
Install an env - pip install virtualenv venv
Install the required dependencies by running pip install -r requirements.txt.
To run the program  - python ammo_scraper.py

The scraper may not save all the images due to the website's protection mechanisms, it seems. To improve the success rate, consider the following:
Use proxies to bypass any IP restrictions.
Play with time.sleep() functionality to introduce delays between requests and mimic human-like browsing behavior.
Explore asynchronous programming (async/await) or multithreading to enhance the scraper's efficiency and speed.

The project includes unit tests to ensure the scraper's functionality. To run the tests, execute the command python ammo_scraper_tests.py