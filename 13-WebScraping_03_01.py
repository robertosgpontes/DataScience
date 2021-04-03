# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# https://www.youtube.com/watch?v=Vxl5jUltHBo
# 
# 
# https://github.com/gabrielfroes/webscraping_python_selenium
# 
# 
# https://selenium-python.readthedocs.io/locating-elements.html
# 
# 

# %%
import pandas as pd
import numpy as np


# %%
import re


# %%
import requests
from bs4 import BeautifulSoup, Comment
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from time import sleep


# %%
url = 'https://www.nba.com/stats/players/traditional/'


# %%
option = Options()
#option.headless = True
driver = webdriver.Firefox(options=option)


# %%
driver.get(url)
driver.implicitly_wait(8)


# %%
driver.find_element_by_id('onetrust-accept-btn-handler').click()
driver.implicitly_wait(5)


# %%
driver.find_element_by_xpath(
        f"//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='AGE']").click()


# %%
driver.implicitly_wait(5)


# %%
element = driver.find_element_by_xpath(
        "//div[@class='nba-stat-table']//table")


# %%
html_content = element.get_attribute('outerHTML')


# %%
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')


# %%
df_full = pd.read_html(str(table))[0]


# %%
df_full


# %%
driver.find_element_by_xpath(
        f"//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='PTS']").click()


# %%
driver.implicitly_wait(5)


# %%
element = driver.find_element_by_xpath(
        "//div[@class='nba-stat-table']//table")
html_content = element.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')
df_full = pd.read_html(str(table))[0]


# %%
df_full


# %%
driver.implicitly_wait(10)


# %%
driver.quit()


# %%
option = Options()
driver = webdriver.Firefox(options=option)


# %%
url = 'https://dhui.cp2.g12.br/login'


# %%
driver.get(url)
driver.implicitly_wait(5) 


# %%
user =  driver.find_element_by_id('username')
#user.click()
user.send_keys('12345')
passwd = driver.find_element_by_id('password')
#passwd.click()
passwd.send_keys('senha')
driver.implicitly_wait(20) 
driver.find_element_by_id('_submit').click()


# %%
driver.implicitly_wait(120) 

sleep(6000)


# %%
driver.quit()


