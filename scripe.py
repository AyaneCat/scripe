#!/usr/bin/env python
# coding=utf-8
import time
import sys, urllib
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.keys import Keys
from datetime import datetime


def filename():
    n = datetime.now()
    fname = str(n.strftime("%A_%d_%B_%Y_%I_%M%p_%f") + ".jpg")
    return fname

def download_image(url):
    img = urllib.urlopen(url)
    f = open(filename(), "wb")
    f.write(img.read())
    f.close()

def download_images(urls):
    for u in result_url:
        download_image(u)
        print(u)
        time.sleep(0.1)


def click_by_xpath(xpath):
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        print "xpath OK"
    except :
        print "Loading took too much time!"

    driver.find_element_by_xpath(xpath).click()

def scroll_down(height):
    driver.execute_script("window.scrollTo(0, " + str(height) + ");")
    time.sleep(5)

def get_url(urls):
    elements = []
    elements = driver.find_elements_by_class_name("rg_i")

    for e in elements:
        img_src_url = e.get_attribute("src")
        if img_src_url != None:
            urls.append(img_src_url)
    urls = list(set(urls))
    return urls

def exist_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except Exception as ElementNotVisibleException:
        return False
    return True

#URL
download_image("")


driver = webdriver.Firefox()
result_url = []
try:
    driver.get("") #URL
    # 検索実行
    search_word = u"佐倉綾音"
    print("tes1")
    search_box = driver.find_element_by_xpath("//*[@id='lst-ib']")
    print("tes2")
    search_box.send_keys(search_word)

    click_by_xpath("//*[@id='tsf']/div[2]/div[3]/center/input[1]")
    click_by_xpath("//*[@id='hdtb-msb']/div[2]/a")

    h = 0
    max_height = driver.execute_script("return document.body.scrollHeight;")
    while h < max_height:
        h += 500
        try:
            click_by_xpath('//*[@id="smb"]')
            print("buttun clilck")
        except:
            pass

        max_height = driver.execute_script("return document.body.scrollHeight;")
        print("max height is " + str(max_height))

        result_url = get_url(result_url)
        scroll_down(h)

    download_images(result_url)

    driver.close()




except:
    import traceback
    traceback.print_exc()
    driver.close()
