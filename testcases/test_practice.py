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
import pytest #1st


class Test_automation():#2nd
    @pytest.fixture #3rd
    def startup(self):#4th
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install())) #5th
        yield #6th
        self.driver.quit() #7th
      
    def test_text_box(self,startup): #8th
        self.driver.get(data.Data().url) #9th
        self.driver.implicitly_wait(10) #10th
        if self.driver.current_url=='https://testautomationpractice.blogspot.com/':
        #textbox
           self.driver.find_element(by=By.ID,value=locator.Locator().Name).send_keys(data.Data().Name_textbox)
           self.driver.find_element(by=By.ID,value=locator.Locator().Email).send_keys(data.Data().Email_textbox)
           self.driver.find_element(by=By.ID,value=locator.Locator().Number).send_keys(data.Data().Number_textbox)
           self.driver.find_element(by=By.ID,value=locator.Locator().Address).send_keys(data.Data().Address_textarea)

    def test_radio(self,startup):
        self.driver.get(data.Data().url) #9th
        if self.driver.current_url=='https://testautomationpractice.blogspot.com/':
        #radio button using action chains
           gender=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,locator.Locator().Gender)))
           gender.click()
           
           #self.driver.find_element(by=By.ID,value=locator.Locator().Gender)
           #self.driver.execute_script("arguments[0].scrollIntoView();",gender)
           #self.driver.find_element(by=By.ID,value=locator.Locator().Gender).click()

    def test_multiple_checkbox(self,startup):
        self.driver.get(data.Data().url) #9th
        self.driver.implicitly_wait(10) #10th
        if self.driver.current_url=='https://testautomationpractice.blogspot.com/':

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

    def test_drop_down(self,startup):
        self.driver.get(data.Data().url) #9th
        self.driver.implicitly_wait(10) #10th
        if self.driver.current_url=='https://testautomationpractice.blogspot.com/':
        #scroll upto colors
           #con=self.driver.find_element(by=By.ID,value=locator.Locator().Country)
           #self.driver.execute_script("arguments[0].scrollIntoView();",con)

        #country
           con=self.driver.find_element(by=By.ID,value=locator.Locator().Country)
           country_dropdown=Select(con)
           country_dropdown.select_by_visible_text("India")
           
        #colors
         
           col=self.driver.find_element(by=By.ID,value=locator.Locator().Colors)
           color_dropdown=Select(col)
           color_dropdown.select_by_value("white")

    def test_date_picker(self,startup):
        self.driver.get(data.Data().url) #9th
        if self.driver.current_url=='https://testautomationpractice.blogspot.com/':
           #selecting date from datepicker  
           #1stMETHOD
           #datepic=self.driver.find_element(by=By.ID,value=locator.Locator().Date)
           #datepic.click()
           #self.driver.find_element(by=By.XPATH,value=locator.Locator().previous).click()
           #self.driver.find_element(by=By.XPATH,value=locator.Locator().december).click() 
           #2nd METHOD
           datesel=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,locator.Locator().Date)))
           datesel.click() 
           pre=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,locator.Locator().previous)))
           pre.click()
           dec=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,locator.Locator().december)))
           dec.click()
        

    def test_link(self,startup):
        self.driver.get(data.Data().url)
        self.driver.implicitly_wait(10) #10th
        if self.driver.current_url=='https://testautomationpractice.blogspot.com/':
           #selecting link
           cart=self.driver.find_element(by=By.XPATH,value=locator.Locator().opencart)
           self.driver.execute_script("arguments[0].scrollIntoView();",cart)
           cart.click()
           self.driver.back()

    def test_home_link(self,startup):
        self.driver.get(data.Data().url)
        self.driver.implicitly_wait(10) #10th
        if self.driver.current_url=='https://testautomationpractice.blogspot.com/':
           home=self.driver.find_element(by=By.XPATH,value=locator.Locator().homelink)
           home.is_displayed()
    