import pandas as pd 
import numpy as np 
import requests 
import os 
from dotenv import load_dotenv
load_dotenv(override=True)
import pyshorteners

class urlShortener(): 
    def __init__(self): 
        pass

    def convert_long_to_short_url(self, long_url):
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        print(short_url)
        return short_url