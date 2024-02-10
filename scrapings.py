# 利用するためには以下をpipでインストールする必要がある
# pip install requests
# pip install bs4
# pip install selenium==3.141.0
# pip install pandas
# pip install chromedriver-binary==chromeのバージョン
# pip install openpyxl
#
# 以下からインストールされているChromeのバージョンと同じバージョンの
# chromedriverをダウンロードし、このファイルと同じ階層に置く必要がある。
# https://googlechromelabs.github.io/chrome-for-testing/

import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
import os
import datetime


class Singleton(object):
    @classmethod
    def get_instance(cls, input):
        if not hasattr(cls, "_instance"):
            cls._instance = cls(input)
        else:
            cls._instance.input = input
        return cls._instance

class Scraping(Singleton):
    _soup = None

    def __init__(self):
        driver_name = "./chromedriver"
        service = Service(executable_path=driver_name)
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(10)
        url = 'https://marumori-town.site.ktaiwork.jp/'
        driver.get(url)
        self._soup = BeautifulSoup(driver.page_source, features='html.parser')


    ## .post.type-postクラスを持つタグのリストを取得する。
    def _entries(self):
        return self._soup.select('.post.type-post')
    
    def _title(self, entry):
        return entry.select_one('.entry-title a').text
    
    def _post_date(self, entry):
        return entry.select_one('.entry-date').text
    
    def _content(self, entry):
        contents = entry.select_one('.entry-content p')
        content = ''
        for c in contents:
            content += c.text + '\n'
        return content
    
    def _get_entry(self, ward):
        entries = self._entries()
        posts = []
        for entry in entries:
            title = self._title(entry)
            if title.find(ward) == -1:
                continue
            post_date = self._post_date(entry)
            content = self._content(entry)
            posts.append((title, post_date, content))
        return posts

    def get_kama(self, ward):
        return self._get_entry(ward)