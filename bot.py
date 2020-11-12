from random import randint
# import pandas as pd
from config import USERNAME, PASSWORD, HASHTAGS
from extensions import InstaBot

homepage = InstaBot(USERNAME, PASSWORD)
homepage.login()


#homepage.follow_by_hashtag(HASHTAGS)




