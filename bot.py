from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Instargram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.baseUrl = "https://www.instagram.com/"
        print("[LOG] Driver Loaded Main")

    def login(self):
        self.driver.get(f"{self.baseUrl}accounts/login/")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username);
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password);
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click();
        time.sleep(3)
        print("[LOG] Login ...")
         
        if self.driver.find_elements(By.XPATH, "//*[@id='slfErrorAlert']"):
            print("[LOG] Login Failed")
            #self.driver.quit()
        else:
            time.sleep(1)
            x = 1
            for x in range(2):
                self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Not Now')]")[0].click()
                print(f"[LOG] Click Not Now Buttons {x}")
        time.sleep(3)

    def search(self, username):
        self.driver.get(f"{self.baseUrl}{username}")
        
        print("[LOG] Search " + username)
        time.sleep(2)
        
    def follow(self, username):
        self.search(username)
        self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Follow')]")[0].click()
        print("[LOG] Follow")
    
    def like(self, linkpost):
        self.driver.get(f"{self.baseUrl}p/{linkpost}")
        print("[LOG] Like " + linkpost)
        time.sleep(2)
        self.driver.find_elements(By.CLASS_NAME, "_aamw")[0].click()
        print("[LOG] Like Seccess")

mybot = Instargram("Username","password")
mybot.login()
mybot.follow("IG Username")
mybot.like('Linkpost')




