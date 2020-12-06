from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from constants import FORM_URL, CHROME_DRIVER_LOCATION


class FillForm:
    def __init__(self, form = FORM_URL):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_LOCATION)
        self.driver.get(form)
        sleep(5)


    def fill_now(self, data: dict):
        """Must have 3 dictionary items of data['addresses'], data['prices'], data['links']"""

        # form[0].send_keys('222')
        # self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("sdf")
        for address, price, link, in zip(data['addresses'], data['prices'], data['links']):
            form = self.driver.find_elements_by_class_name('exportInput')
            form[0].send_keys(address)
            form[1].send_keys(price)
            form[2].send_keys(link)

            self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()
            sleep(4)
            self.driver.find_element_by_link_text('Submit another response').click()
            sleep(5)
