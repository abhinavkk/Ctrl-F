import os
import requests
from sys import platform
from selenium import webdriver
from xml.etree import ElementTree

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DRIVER_NAME = "chromedriver.exe" if platform == "win32" else "chromedriver"
DRIVER_DIR = os.path.join(BASE_DIR, "drivers", DRIVER_NAME)

JS_SCRIPT = 'if(yt.config_.TTS_URL.length) window.location.href=yt.config_.TTS_URL+"&kind=asr&fmt=srv1&lang=en"'


def getTranscribedUrl(url):
    """ Get transcribed URL."""

    driver = webdriver.Chrome(DRIVER_DIR)
    driver.get(url)
    driver.execute_script(JS_SCRIPT)
    transcribed_url = driver.current_url
    driver.quit()
    return transcribed_url
