from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from Test_Data import data
from Test_Locator import locator


class automation():
    def __init__(self,url):
        self.url=url
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
    def text_box(self): 
        #textbox
        self.driver.find_element(by=By.ID,value=locator.Locator().Name).send_keys(data.Data().Name_textbox)
        self.driver.find_element(by=By.ID,value=locator.Locator().Email).send_keys(data.Data().Email_textbox)
        self.driver.find_element(by=By.ID,value=locator.Locator().Number).send_keys(data.Data().Number_textbox)
        self.driver.find_element(by=By.ID,value=locator.Locator().Address).send_keys(data.Data().Address_textarea)

    def radio(self):
        #radio button using action chains
         gender=self.driver.find_element(by=By.ID,value=locator.Locator().Gender)
         self.driver.execute_script("arguments[0].scrollIntoView();",gender)
         gender.click()

    def multiple_checkbox(self):
        #scroll untill saturday
        fri=self.driver.find_element(by=By.ID,value=locator.Locator().Day1)
        self.driver.execute_script("arguments[0].scrollIntoView();",fri)

        #select single checkbox 
        self.driver.find_element(by=By.ID,value=locator.Locator().Day1).click()

        #select multiple checkbox
        self.driver.find_element(by=By.ID,value=locator.Locator().Day2).click()
        self.driver.find_element(by=By.ID,value=locator.Locator().Day3).click()
    
        #deselect one checkbox
        satday=self.driver.find_element(by=By.ID,value=locator.Locator().deselectday)
        act=ActionChains(self.driver)
        act.double_click(on_element=satday) 

    def drop_down(self):
        #scroll upto open cart
        cart=self.driver.find_element(by=By.XPATH,value=locator.Locator().opencart)
        self.driver.execute_script("arguments[0].scrollIntoView();",cart)

        #country
        con=self.driver.find_element(by=By.ID,value=locator.Locator().Country)
        country_dropdown=Select(con)
        country_dropdown.select_by_visible_text("India")
        #colors
        col=self.driver.find_element(by=By.ID,value=locator.Locator().Colors)
        color_dropdown=Select(col)
        color_dropdown.select_by_value("white")


    def date_picker(self):
        #selecting date from datepicker  
        self.driver.find_element(by=By.ID,value=locator.Locator().Date).click()  
        self.driver.find_element(by=By.XPATH,value=locator.Locator().previous).click()
        self.driver.find_element(by=By.XPATH,value=locator.Locator().december).click() 

    def link(self):
        #selecting link
        cart=self.driver.find_element(by=By.XPATH,value=locator.Locator().opencart)
        cart.click()
        self.driver.back()

    def home_link(self):
        home=self.driver.find_element(by=By.XPATH,value=locator.Locator().homelink)
        self.driver.execute_script("arguments[0].scrollIntoView();",home)
        if home.is_displayed():
            print("home link is visible")

    def shutdown(self):
        self.driver.quit()

o= automation(data.Data().url)
o.text_box()
o.radio()
o.multiple_checkbox()
o.drop_down()
o.date_picker()
o.link()
o.home_link()
o.shutdown()


        
        

        
