# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:20:11 2023

@author: mhouts
"""

import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.linkedin.com/in/max-van-houts-676263133/")
soup = BeautifulSoup(page.content, 'html.parser')

#links =[link.get("href") for link in soup.find_all("a")]

print(soup)
