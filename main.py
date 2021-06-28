from selenium import webdriver

import time

class CookieClicker:
    def __init__(self):
        self.SITE_LINK = "https://orteil.dashnet.org/cookieclicker/"

        self.SITE_MAP = {
            "buttons": {
                "cookie": {
                    "xpath": "/html/body/div[2]/div[2]/div[15]/div[8]/div[1]"
                },
                "upgrade": {
                    "xpath": "/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[$$NUMBER$$]"
                }
            },
            "labels": {
                "money": {
                    "xpath": "/html/body/div[2]/div[2]/div[15]/div[4]"
                }
            }
        }

        self.driver = webdriver.Chrome(executable_path='C:\\WebDrivers\\chromedriver.exe')
        self.driver.maximize_window()

    def open_website(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(10)
    
    def click_on_cookie(self):
        self.driver.find_element_by_xpath(self.SITE_MAP["buttons"]["cookie"]["xpath"]).click()

    def get_current_money(self):
        money = self.driver.find_element_by_xpath(self.SITE_MAP["labels"]["money"]["xpath"]).text
        return money.split(" ")[0]

    def get_best_upgrade(self):
        found = False
        i = 2
        while not found:
            objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(i))
            classes_objeto = self.driver.find_element_by_xpath(objeto).get_attribute("class")

            if not "enabled" in classes_objeto:
                found = True
            else:
                i += 1
        return i - 1

    def comprar_upgrade(self):
        objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(self.get_best_upgrade()))
        self.driver.find_element_by_xpath(objeto).click()

cookie = CookieClicker()
cookie.open_website()

i = 0

while True:
    if i % 500 == 0 and i != 0:
        time.sleep(1)
        cookie.comprar_upgrade()
        time.sleep(1)

    cookie.click_on_cookie()
    i += 1