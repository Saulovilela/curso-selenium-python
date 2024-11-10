import unittest, base64, time, os, subprocess, allure, json, urllib3, behave, behave_html_formatter
from behave import *
from selenium import webdriver
from support.ambiente import *
from selenium.webdriver.common.by import By

class PageUtils(unittest.TestCase):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-site-isolation-trials')
    chrome_options.add_argument('--ignore-certifate-erros')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)

    def abrir_um_browser(context, base_url):
        context.driver.get(base_url)

    def limpar_browser(context):
        context.driver.delete_all_cookies()

    def fechar_browser(context):
        context.driver.quit()
    
    def clica_elemento_login(context, login):
        context.driver.find_element(By.ID, login).click()

    def inserir_login(context):
        context.driver.find_element(By.ID, 'user-name').send_keys("standard_user")
    
    def inserir_senha(context):
        context.driver.find_element(By.ID, 'password').send_keys("secret_sauce")