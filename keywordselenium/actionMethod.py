from selenium import webdriver
import time
from base.find_element import FindElement
class ActionMethod:
    def __init__(self):
        pass
    def open_browser(self,browser):
        if browser=='Chrome':
            self.driver=webdriver.Chrome()
        elif browser=='Firfox':
            self.driver=webdriver.Firefox()
        else:
            self.driver=webdriver.Edge()

    def get_url(self,url):
        self.driver.get(url)

    def get_element(self,key):
        find_element=FindElement(self.driver)
        element=find_element.get_element(key)
        return element

    def element_send_keys(self,value,key):
        element=self.get_element(key)
        element.send_keys(value)

    def element_get_text(self, key):
        element = self.get_element(key)
        return element.text

    def click_element(self,key):
        self.get_element(key).click()

    def sleep_time(self):
        time.sleep(3)

    def close_browser(self):
        self.driver.close()

    def get_title(self):
        title= self.driver.title
        return title