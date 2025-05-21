from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# WebDriverのセットアップ（Chromeを使用）
driver = webdriver.Chrome()

# Webページを開く
driver.get("https://example.com")  # ここに対象のURLを指定

# リンクを見つけてクリック
link = driver.find_element(By.LINK_TEXT, "リンクのテキスト")  # テキストから検索
# link = driver.find_element(By.PARTIAL_LINK_TEXT, "一部のテキスト")  # 一部のテキストから検索
# link = driver.find_element(By.XPATH, "//a[@href='リンクのURL']")  # XPathを使う
link.click()

# しばらく待機（ページ遷移などのため）
time.sleep(5)

# ブラウザを閉じる
driver.quit()

