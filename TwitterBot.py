# Author: Diego Caraballo
# GitHub: https://github.com/DiegoCaraballo
# web: http://www.pythondiario.com

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time, random
from bs4 import BeautifulSoup
import Screen


class TwitterBot:

    def __init__(self):
        # Chrome
        self.driver = webdriver.Chrome(executable_path="assets/webdriver/chromedriver.exe")
        self.userName = "userName"
        self.password = "password"
        self.contentFile = open("listKeywords.txt").readlines()

    def twitterLogin(self):
        self.driver.get('https://twitter.com/login')
        time.sleep(5)
        text_area1 = self.driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
        text_area1.clear()
        #text_area1.send_keys(account["username"])
        text_area1.send_keys(self.userName)
        text_area = self.driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
        text_area.clear()
        #text_area.send_keys(account["password"])
        text_area.send_keys(self.password)
        #text_area = driver.find_element_by_name('remember_me').click()
        submit_button = self.driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
        submit_button.click()
        time.sleep(5)

    def checkTwitterLogin(self):
        self.driver.get('https://twitter.com/')
        return self.check_exists_by_xpath('//*[contains(concat(" ", normalize-space(@class), " "), " logged-out")]')


    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def searchKeyword(self):
        time.sleep(2)
        try:
            search = self.driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/form[1]/input[1]')
            search.clear()

            content = self.getListKeywords()

            # Random KeywordList
            keyword = random.choice(content)

            search.send_keys(keyword)

            submit_button = self.driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/form[1]/span[1]/button[1]')
            submit_button.click()
            time.sleep(5)
        except NoSuchElementException as e:
            print("Error in searchKeyword: " + str(e))
        except Exception as i:
            print("Uncontrolled error: " + str(i))

    def likeTweet(self):
        try:

            # Recent Tweets
            submit_button = self.driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[6]/a[1]')
            submit_button.click()
            time.sleep(5)

            #Selenium hands the page source to Beautiful Soup
            soup_top = BeautifulSoup(self.driver.page_source, 'lxml')

            for link in soup_top.find_all("li", class_="stream-items-id"):
                print("Entró")
                print(link)
                input("Waiting..")
            
        except Exception as e:
            ("Uncontrolled error: " + str(e))
    
    def retweet(self):
        pass

    def follow(self):
        pass
    
    def unFollow(self):
        pass

    def getListKeywords(self):
        try:
            # Content of the listKeywords.txt
            content = [x.strip() for x in self.contentFile]
            return content
        except Exception as e:
            print(e)
            input("Press any key to continue...")

if __name__ == "__main__":
    
    # Initialize
    tBot = TwitterBot()
    if(tBot.checkTwitterLogin()):
        tBot.twitterLogin()

    tBot.searchKeyword()
    tBot.likeTweet()

    #while True:
    #    pass