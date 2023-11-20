import os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


PROMISED_DOWN = 150
PROMISED_UP = 100
TWITTER_EMAIL = os.environ["email"]
TWITTER_PASSWORD = os.environ["password"]

class InternetSpeedTwitterBot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--detach")
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options)

        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://fast.com/')
        time.sleep(20)
        show_more_info_btn = self.driver.find_element(By.ID, 'show-more-details-link').click()

        self.down = int(self.driver.find_element(By.ID, 'speed-value').text)
        print(self.down)

        self.up = int(self.driver.find_element(By.ID, 'upload-value').text)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        time.sleep(10)
        email_input = self.driver.find_element(By.XPATH,
                                               "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email_input.send_keys(TWITTER_EMAIL)
        time.sleep(1)
        email_input.send_keys(Keys.ENTER)
        time.sleep(5)
        try:
            pass_input = self.driver.find_element(By.XPATH,
                                                  "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            pass_input.send_keys(TWITTER_PASSWORD)
            pass_input.send_keys(Keys.ENTER)
        except NoSuchElementException:
            username = self.driver.find_element(By.XPATH,
                                           "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
            username.send_keys("InternetTe10")
            username.send_keys(Keys.ENTER)
            time.sleep(5)
            pass_input = self.driver.find_element(By.XPATH,
                                             "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            pass_input.send_keys(TWITTER_PASSWORD)
            pass_input.send_keys(Keys.ENTER)

        time.sleep(5)

        input = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        input.send_keys(f"Digi, de ce viteza internetului este de {self.down}/down si {self.up}/up cand platesc pentru {PROMISED_DOWN}/down si {PROMISED_UP}/up ?")
        time.sleep(3)

        tweet = self.driver.find_element(By.XPATH,
                                         '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span').click()
        time.sleep(5)
        print("Tweet Done")
        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    bot.tweet_at_provider()

