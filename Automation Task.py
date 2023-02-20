from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import re

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

#1. Google Chrome opening automatically
chrome.get('https://transfermate.io/?lng=en')
sleep(2)

#2. Click on "Agree" cookies button
chrome.find_element(By.CSS_SELECTOR, value='#cookies-read-more-link').click()
sleep(3)

chrome.find_element(By.XPATH, '//*[@id="menu_485_115_28617"]').click()
sleep(4)

chrome.find_element(By.CSS_SELECTOR, value='#register_account_type_individual_form_input > label').click()
sleep(3)

chrome.execute_script("window.scrollBy(0, 500)")
sleep(3)
chrome.find_element(By.CSS_SELECTOR, value='#first_name').send_keys('Hurjui')
sleep(3)

chrome.find_element(By.CSS_SELECTOR, value='#last_name').send_keys('Denisa')
sleep(3)

chrome.find_element(By.CSS_SELECTOR, value='#email').send_keys('hurjui.denisa@yahoo.com')
sleep(3)

chrome.find_element(By.CSS_SELECTOR, value='#__pin_mobile_number_mobile_phone').send_keys('0758474001')
sleep(3)

chrome.find_element(By.CSS_SELECTOR, value='#register_terms_of_use_agree_form_input > label').click()
sleep(3)

chrome.find_element(By.CSS_SELECTOR, value='#register_newsletter_and_privacy_policy_agree_form_input > label').click()
sleep(3)

captcha = chrome.find_element(By.XPATH, '//*[@id="register_calc_captcha"]')
captcha_text = chrome.find_element(By.CSS_SELECTOR, value='#cal_captcha_f10_question')
num1_operator_num2 = re.findall(r'\d+|[+\-*]', captcha_text.text)
num1, operator, num2 = num1_operator_num2[0], num1_operator_num2[1], num1_operator_num2[2]
result = eval(num1 + operator + num2)
chrome.find_element(By.CSS_SELECTOR, value='#__calc_captcha_text').send_keys(result)
sleep(3)
chrome.find_element(By.XPATH,'//*[@id="button_subscribe"]').click()
sleep(4)
