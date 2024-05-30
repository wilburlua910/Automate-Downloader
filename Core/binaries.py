from Utilities.utils import UtilitiesManager
from selenium.webdriver import EdgeOptions
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.db import Database
import re
import os
import glob
import time

class BinariesDownloader:
    options = None
    driver = None
    database = None
    def __init__(self):
        self.driver = self.initDriver()
        print('Init Edge Web Driver complete')
        self.utilsMgr = UtilitiesManager()
        print('Init Utils Manager complete')
        self.database = Database()
        print('Init Database complete')
        print('binaries downloader class initialized')

    def initDriver(self) -> EdgeOptions:
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        # options.add_experimental_option("prefs", {"download.default_directory": r"C:\Users\ZZ03HT834\Downloads\nodejs"})
        options.add_experimental_option("prefs", {"user_experience_metrics": {"personalization_data_consent_enabled": True}})
        self.driver = webdriver.Edge(options = options)
        return self.driver

    def nodeJs(self):
        if self.driver is not None:
            self.nodeJs18_ver = '18.20.0'
            self.nodeJs20_ver = '20.13.0'
            self.driver.get('https://nodejs.org/en/download/prebuilt-binaries')

            # Download nodejs18
            dropmenu1 = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, ":Rintff6dta:")))
            dropmenu1.click()
            selectNodejs18 = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[starts-with(text(),'v18')]")))
            selectNodejs18.click()

            # Check with operating system on dropmenu2
            opsSys = self.driver.find_element(By.XPATH, "//*[contains(@aria-label,'Operating System')]").text

            if opsSys == 'Windows': # change to 'Windows' or 'macOS'
                downloadNodejs18 = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Download Node.js v18")))
                downloadNodejs18.click()
            else:
                dropmenu2 = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, ":R12ntff6dta:")))
                dropmenu2.click()
                selectWindows = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[starts-with(text(),'Windows')]")))
                selectWindows.click()
                downloadNodejs18 = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Download Node.js v18")))
                downloadNodejs18.click()

            # Get the path to the Downloads folder
            downloadsPath = os.path.join(os.path.expanduser("~"), "Downloads")
            s3FolderName = os.path.join(os.path.expanduser("~"), "Downloads\\nodejs")

            if self.utilsMgr.downloadWait(downloadsPath):

                # List all files in the Downloads folder
                files = glob.glob(os.path.join(downloadsPath, "*node-v18*"))

                # Check if there are any files in the folder
                if files:
                    # Extract the first filename (or handle it as needed)
                    filename = os.path.basename(files[0])
                    version = re.search(r'(\d+\.\d+\.\d+)', filename).group(1)
                    
                    if self.nodeJs18_ver != version:
                        print(f"Moving '{filename}' into '{s3FolderName}'")
                        if not os.path.exists(s3FolderName):
                            os.mkdir(s3FolderName)
                        os.rename(os.path.join(downloadsPath, filename), os.path.join(s3FolderName, filename))
                    else:
                        print("No updates")
                        os.remove(os.path.join(downloadsPath, filename))  

            else:
                print("No nodejs18 binaries found in binaries folder.")

            
            # Download nodejs20
            dropmenu1 = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, ":Rintff6dta:")))
            dropmenu1.click()
            selectNodejs20 = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[starts-with(text(),'v20')]")))
            selectNodejs20.click()

            # Check with operating system on dropmenu2
            opsSys = self.driver.find_element(By.XPATH, "//*[contains(@aria-label,'Operating System')]").text

            if opsSys == 'Windows': # change to 'Windows' or 'macOS'
                downloadNodejs20 = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Download Node.js v20")))
                downloadNodejs20.click()
            else:
                dropmenu2 = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, ":R12ntff6dta:")))
                dropmenu2.click()
                selectWindows = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[starts-with(text(),'Windows')]")))
                selectWindows.click()
                downloadNodejs20 = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Download Node.js v20")))
                downloadNodejs20.click()

            if self.utilsMgr.downloadWait(downloadsPath):

                # List all files in the Downloads folder
                files = glob.glob(os.path.join(downloadsPath, "*node-v20*"))

                # Check if there are any files in the folder
                if files:
                    # Extract the first filename (or handle it as needed)
                    filename = os.path.basename(files[0])
                    version = re.search(r'(\d+\.\d+\.\d+)', filename).group(1)
                    
                    if self.nodeJs20_ver != version:
                        print(f"Moving '{filename}' into '{s3FolderName}'")
                        if not os.path.exists(s3FolderName):
                            os.mkdir(s3FolderName)
                        os.rename(os.path.join(downloadsPath, filename), os.path.join(s3FolderName, filename))
                    else:
                        print("No updates")
                        os.remove(os.path.join(downloadsPath, filename))
                    
            else:
                print("No nodejs20 binaries found in binaries folder.")






            # # Download nodejs20 original
            # self.driver.find_element(By.ID, ":Rintff6dta:").click()
            # self.driver.find_element(By.XPATH, "//*[starts-with(text(),'v20')]").click()

            # if self.driver.find_element(By.XPATH, "//*[contains(text(),'Windows')]"): # change to 'Windows' or 'macOS'
            #     self.driver.find_element(By.PARTIAL_LINK_TEXT, "Download Node.js v20").click()
            # else:
            #     self.driver.find_element(By.ID, ":R12ntff6dta:").click()
            #     self.driver.find_element(By.XPATH, "//*[contains(text(),'Windows')]").click()
            #     self.driver.find_element(By.PARTIAL_LINK_TEXT, "Download Node.js v20").click()

            # time.sleep(10)

            # # Get the path to the Downloads folder
            # downloadsPath = os.path.join(os.path.expanduser("~"), "Downloads")
            # s3FolderName = os.path.join(os.path.expanduser("~"), "Downloads\\nodejs")

            # # List all files in the Downloads folder
            # files = glob.glob(os.path.join(downloadsPath, "*node-v20*"))

            # # Check if there are any files in the folder
            # if files:
            #     # Extract the first filename (or handle it as needed)
            #     filename = os.path.basename(files[0])
            #     version = re.search(r'(\d+\.\d+\.\d+)', filename).group(1)
            #     print(version)
                
            #     if self.nodeJs20_ver != version:
            #         print(f"Moving '{filename}' into '{s3FolderName}'")
            #         if not os.path.exists(s3FolderName):
            #             os.mkdir(s3FolderName)
            #         os.rename(os.path.join(downloadsPath, filename), os.path.join(s3FolderName, filename))
            #     else:
            #         print("No updates")
            #         os.remove(os.path.join(downloadsPath, filename))
                    
            # else:
            #     print("No nodejs20 binaries found in binaries folder.")

      

                

    #         # self.driver.find_element(By.XPATH, "//*[contains(text(),'v18.20.2 (LTS)')]").click()
    #         # self.driver.find_element(By.ID, ":R1intff6dta:").click()
    #         # self.driver.find_element(By.XPATH, "//*[contains(text(),'x64')]").click() # change to 'x64' or 'ARM64'
    #         # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))

   
    #         # # Check if there are any files in the folder
    #         if files:
    #             # Extract the first filename (or handle it as needed)
    #             filename = os.path.basename(files[0])
    #             version = re.split("[-]", filename)[1]
    #             print("First file version in Downloads folder:", version)
    #         else:
    #             print("No files found in the Downloads folder.")