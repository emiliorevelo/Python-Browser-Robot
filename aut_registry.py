#Emilio Revelo

#Automated user registry written in Python with selenium library
#This just an example, you can use it for any task that you need

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

tupla=("user1@example.com,user2@example.com,usern@example.com") 
sec="none"

menu=raw_input ("Login - l\nRegister - r\n")
    
def register():
    driver = webdriver.Chrome() # You can use Firefox as well
    driver.get('https://example.com')
    print ("Connected!")
    for i in range(0, 7,2):
        
        a = driver.find_element_by_id('EXAMPLE_REGISTER')
        a.click()
        print ("Register...")
        sleep(5)
        
        b = driver.find_element_by_id('EXAMPLE_NAME')
        b.send_keys(tupla[i])
        print ("Email set...")

        c = driver.find_element_by_id('EXAMPLE_PSWD')
        c.send_keys(tupla[i+1])
        print ("Pass set...")
        
        c = driver.find_element_by_id('EXAMPLE_CONFPSWD')
        c.send_keys(tupla[i+1])
        print ("Confirm pass...")

        men = Select (driver.find_element_by_id("EXAMPLE_QUESTION_ID"))
        men.select_by_value('10')
                      
        d = driver.find_element_by_id('EXAMPLE_QUESTION_ANSWER')          
        d.send_keys(sec)
        print ("Secret...")
        
        e=driver.find_element_by_id('EXAMPLE_REGISTER_BUTTON')
        e.click()
        sleep(15)
        g = driver.find_element_by_id('EXAMPLE_CONFIRM')
        g.click()
        sleep(4)
        r = driver.find_element_by_id('EXAMPLE_Yes')
        r.click()
        sleep(4)
    driver.quit() 
    
def login():
    for i in range(0, 7,2):
        driver = webdriver.Chrome()
        driver.get('https://example.com')
        print ("Connected!")
        sleep(1)

        a = driver.find_element_by_id('EXAMPLE_NAME')
        a.send_keys(tupla[i])
        print ("User sent...")
        sleep(1)

        b = driver.find_element_by_id('EXAMPLE_PSWD')
        b.send_keys(tupla[i+1])
        print ("Password sent...")

        c = driver.find_element_by_id('EXAMPLE_BUTTON')
        c.click()
        print ("Done!")

        sleep(10)
    driver.quit()
        
if menu=="l":
    login()
if menu=="r":
    register()
else:
    print ("Invalid option...")

