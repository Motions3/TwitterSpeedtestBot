import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from dotenv import load_dotenv

load_dotenv()

# Environment Constants
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
PROMISED_DOWN = os.getenv("PROMISED_DOWN")
PROMISED_UP = os.getenv("PROMISED_UP")
CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
TIMETODAY = datetime.datetime.now()


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(3)
        self.driver.find_element(by=By.ID, value='onetrust-accept-btn-handler').click()
        sleep(3)
        self.driver.find_element(by=By.CLASS_NAME, value='start-text').click()
        sleep(60)
        self.down = self.driver.find_element(by=By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                   '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(by=By.XPATH,
                                           value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                 '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        sleep(5)

        email = self.driver.find_element(by=By.XPATH,
                                         value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                               '2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_USERNAME, Keys.RETURN)
        sleep(5)

        password = self.driver.find_element(by=By.XPATH,
                                            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                  '2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div['
                                                  '2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD, Keys.RETURN)
        sleep(5)

        writeMessage = self.driver.find_element(by=By.XPATH,
                                               value='//*[@id="react-root"]/div/div/div['
                                                     '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                                     '1]/div/div/div/div[2]/div['
                                                     '1]/div/div/div/div/div/div/div/div/div/div/div/div['
                                                     '1]/div/div/div/div/div/div[2]/div/div/div/div')
        writeMessage.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up, when I "
                              f"pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
                              f"Speedtest taken on {TIMETODAY}")
        sleep(5)
        self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button').click()
        sleep(5)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
