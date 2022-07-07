from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
from bs4 import BeautifulSoup
import requests
import re
import random
import sqlite3
import psycopg2
from config_file import *


# PATH = '/Users/ategran/PycharmProjects/pythonProject3/chromedriver'
# options = webdriver.ChromeOptions()
# ser = Service('/Users/ategran/PycharmProjects/pythonProject3/chromedriver')
# driver = webdriver.Chrome(options=options, service=ser)

HEADERS = {
    'user-agents': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/93.0.4577.63 Safari/537.36 OPR/79.0.4143.22',
    'accept': '*/*'}

# con = sqlite3.connect('new_db.db')
# c = con.cursor()
# c.execute('CREATE TABLE IF NOT EXISTS cities ('
#           '    city_id     INTEGER NOT NULL PRIMARY KEY,'
#           '    name       text'
#           ');')

# driver.get('https://pixabay.com/ru/images/search/%D0%BA%D0%BE%D1%82%D1%8F%D1%82%D0%B0/')
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
# time.sleep(15)
# for i in range(100):
#     img = driver.execute_script(f"return document.getElementsByClassName('link--h3bPW')[{i}].getElementsByTagName('img')[0].src")
#     while re.match('gif', img):
#         print('рекурсия')
#         time.sleep(1)
#         img = driver.execute_script(f"return document.getElementsByClassName('link--h3bPW')[{i}].getElementsByTagName('img')[0].src")
#     print(img)
#     c.executescript(f"INSERT INTO cats VALUES (NULL, '{img}')")
#
# c.execute("SELECT link FROM cats WHERE cats.cat_id=1")
# print(c.fetchone()[0])

# def return_pet_img(pet):
#     if pet == 'cat':
#         n = random.randint(1, 200)
#         print(n)
#         c.execute(f"SELECT link FROM cats WHERE cats.cat_id={n}")
#         img = c.fetchone()
#         print(img[0])
#         return img[0]
#
# i = return_pet_img('cat')

# print(5 in range(1,10))
#
# print(isinstance('1jf', int))
# a = (1, 10)
# print(2 in range(a[0], a[1]))
# print(random.randint(0, 1))
# l = [1, 2, 3, 4, 5]
# print( l[1:] + l[:1] )
# print( l[-1:] + l[:-1] )

# driver.get('https://www.unipage.net/en/cities?page=10&per-page=100')
# city = driver.execute_script("return document.getElementsByTagName('tr')[2].getElementsByTagName('td')[3].textContent")
# print(city)

# URL = 'https://www.unipage.net/en/cities?page=1&per-page=100'
#
# def get_html(url, params=None):
#     r = requests.get(url, headers=HEADERS, params=params)
#     return r
#
# cities = []
# for i in range(474, 475):
#     print(f'parse {i}')
#     html = get_html(f'https://www.unipage.net/en/cities?page={i}&per-page=100')
#     soup = BeautifulSoup(html.text, 'html.parser')
#     tr_list = soup.findAll('tr')[2:]
#     for a in tr_list:
#         city = a.findAll('a')[1].get_text()
#         c.executescript(f"""INSERT INTO cities VALUES (null, "{city}")""")
#         cities.append(city)
#
# print(len(cities))

# print('z'.capitalize(), 'Z'.lower())

# con = psycopg2.connect(URI, sslmode="require")
# c = con.cursor()
