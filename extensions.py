from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from random import randint


class InstaBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = wd.Firefox()

    def close_browser(self):
        self.browser.close()

    def login(self):
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        self.browser.find_element_by_xpath('//div[2]/div/div/div/div[2]/button[1]').click()  # Cookies akzeptieren
        self.browser.find_element_by_name('username').send_keys(self.username)
        self.browser.find_element_by_name('password').send_keys(self.password)
        self.browser.find_element_by_xpath('//section/main/div/div/div[1]/div/form/div/div[3]/button').click()
        time.sleep(5)
        self.browser.find_element_by_css_selector('button.sqdOP:nth-child(1)').click()  # Anmeldedaten nicht speichern
        self.browser.find_element_by_css_selector('button.aOOlW:nth-child(2)').click()  # Benachrichtigungen nicht aktivieren

    def follow_by_hashtag(self, hashtags):

        for tag in hashtags:
            self.browser.get('https://www.instagram.com/explore/tags/' + tag + '/')
            element = self.browser.find_element_by_tag_name('a')
            action = ActionChains(self.browser)
            for elem in element:
                action.move_to_element(elem)
                action.perform()
                action.click()











