#browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
#time.sleep(2)
# Instagram cookies akzeptieren
#insta_cc = browser.find_element_by_xpath('//div[2]/div/div/div/div[2]/button[1]').click()

# Einloggen
#browser.find_element_by_name('username').send_keys(config.username)
#browser.find_element_by_name('password').send_keys(config.password)
#browser.find_element_by_xpath('//section/main/div/article/div/div[1]/div/form/div/div[3]/button').click()

import time
import random


class InstaBot:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        self.browser.find_element_by_xpath('//div[2]/div/div/div/div[2]/button[1]').click()  # Cookies akzeptieren

    def login(self, username, password):
        self.browser.find_element_by_name('username').send_keys(username)
        self.browser.find_element_by_name('password').send_keys(password)
        self.browser.find_element_by_xpath('//section/main/div/div/div[1]/div/form/div/div[3]/button').click()
        time.sleep(0.5)

    def follow_by_hashtag(self, hashtags):
        self.browser.find_element_by_tag_name('a')
        for tag in hashtags:
            self.browser.get('https://www.instagram.com/explore/tags/' + tag + '/')
            time.sleep(10)
            element = self.browser.find_element_by_tag_name('a')
            self.browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/%s;' % 6, element)
            # langsam scrollen %6 = 1/6 vom Display usw.
            self.browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/%s;' % 4, element)
            self.browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/%s' % 3, element)
            self.browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/%s' % 2, element)
            time.sleep(1)
        num_scroll = 0

        while num_scroll != 10:
            num_scroll += 1
            self.browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', element)
            if num_scroll % 10 == 0:
                print('!')





