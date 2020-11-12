from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import time
from random import randint
import pandas as pd
from config import USERNAME, PASSWORD, HASHTAGS
from extensions import InstaBot

#browser = wd.Firefox()

homepage = InstaBot(USERNAME, PASSWORD)
homepage.login()


#homepage.follow_by_hashtag(HASHTAGS)




