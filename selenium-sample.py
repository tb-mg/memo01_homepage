from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

##################################################################
# WebDriverのセットアップ（Chromeを使用）
driver = webdriver.Chrome()

##################################################################
# Seleniumでページを取得
driver.get("https://example.com")  # ここに対象のURLを指定

##################################################################
# リンクを見つけてクリック
link1 = driver.find_element(By.LINK_TEXT, "リンクのテキスト")  # テキストから検索
link1.click()
link2 = driver.find_element(By.PARTIAL_LINK_TEXT, "一部のテキスト")  # 一部のテキストから検索
link2.click()
link3 = driver.find_element(By.XPATH, "//a[@href='リンクのURL']")  # XPathを使う
link3.click()

##################################################################
# しばらく待機（ページ遷移などのため）
time.sleep(5)

##################################################################
# ページのHTMLを取得
html = driver.page_source
print("---------------------------html: ", html)

##################################################################
element = driver.find_element("tag name", "body")
print("--------------------------- body: ", element.get_attribute("outerHTML"))

##################################################################
# 要素を取得
element2 = driver.find_element(By.ID, "example_id")
# 属性値を取得
attribute_value = element2.get_attribute("href")
print("--------------------------- href: ", attribute_value)

##################################################################
# ページのHTMLを取得
html2 = driver.page_source
time.sleep(5)
print("---------------------------html2: ", html)
# BeautifulSoupで解析 
soup1 = BeautifulSoup(html2, "lxml")
title=soup1.find("title").text
print("---------------------------html2 soup title: ", title)
# BeautifulSoupで解析 ALL!!!
soup2 = BeautifulSoup(html2, "lxml")
title=soup2.find_all(class_="title")
print("---------------------------html2 soup title: ", title)

##################################################################
time.sleep(60)
# WebDriverを閉じる
driver.quit()
##################################################################
