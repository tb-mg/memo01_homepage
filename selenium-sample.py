from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# WebDriver�̃Z�b�g�A�b�v�iChrome���g�p�j
driver = webdriver.Chrome()

# Web�y�[�W���J��
driver.get("https://example.com")  # �����ɑΏۂ�URL���w��

# �����N�������ăN���b�N
link = driver.find_element(By.LINK_TEXT, "�����N�̃e�L�X�g")  # �e�L�X�g���猟��
# link = driver.find_element(By.PARTIAL_LINK_TEXT, "�ꕔ�̃e�L�X�g")  # �ꕔ�̃e�L�X�g���猟��
# link = driver.find_element(By.XPATH, "//a[@href='�����N��URL']")  # XPath���g��
link.click()

# ���΂炭�ҋ@�i�y�[�W�J�ڂȂǂ̂��߁j
time.sleep(5)

# �u���E�U�����
driver.quit()

