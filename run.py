from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os 
import sqlite3

class FireFoxBinariesDownloader:

    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('')
        self.driver = webdriver.Firefox()

        db = sqlite3.connect('sql.db')

    def downloadNodeJS():
        driver = webdriver.Firefox()

        driver.get('https://nodejs.org/en')

        button = driver.find_element(By.LINK_TEXT, 'Download Node.js (LTS)')
        button.click()
        driver.close()

    def SetUpBrowser():
        options = webdriver.FirefoxOptions()
        downloadsPath = "/home/downloads"
        os.makedirs(downloadsPath)
    
    def downloadOracle():
        driver = webdriver.Firefox()
        driver.get('https://www.oracle.com/my/java/technologies/downloads/#java11-windows')

        javaBtnElement = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.ID, 'rt01tab1-jdk22-windows'))

        if javaBtnElement is not None:
            print('Able to locate java 22 button')
            javaBtnElement.click()
        else:
            print('Unable to locate java 22 button')

        downloadWindows = driver.find_elements(By.CSS_SELECTOR, 'a')

        for a in downloadWindows:
            print(a.get_attribute('href'))

            if a.get_attribute('href') == 'https://download.oracle.com/java/22/latest/jdk-22_linux-aarch64_bin.tar.gz':
                driver.get(a.get_attribute('href'))
                
if __name__ == "__main__":
    #Main method to create objects
    
