import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


class Header():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.header_links = []
        self.header_respondes = []
        self.header_titles = []

    def teardown_method(self):
        self.driver.quit()

    def h_links(self):
        self.driver.get("http://158.160.56.133/app/pets")
        self.driver.find_element(By.LINK_TEXT, "Питомцы").click()
        self.header_links.append(self.driver.current_url)
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "О нас").click()
        self.header_links.append(self.driver.current_url)
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Контакты").click()
        self.header_links.append(self.driver.current_url)
        self.driver.close()

    def h_responses_titles(self):
        for hlink in self.header_links:
            h_url = str(hlink)
            self.header_respondes.append(f"{h_url} - {requests.get(h_url)}")
            response = requests.get(h_url)
            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.title.string
            self.header_titles.append(f"{h_url} - {title}")


    def links_print(self):
        print(self.header_links)
        print(self.header_respondes)
        print(self.header_titles)
