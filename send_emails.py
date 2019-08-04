from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

def sendEmail(driver,csv_file,Email, Password, subject, body ):
    
    browser = webdriver.Chrome(driver)
    browser.get("https://gmail.com/")

    email = browser.find_element_by_name('identifier')

    email.send_keys(Email)
    email.send_keys(Keys.ENTER)
    browser.implicitly_wait(1)
    password= browser.find_element_by_name("password")
    password.send_keys(Password)
    password.send_keys(Keys.ENTER)

    try: 
        
        create_email = browser.find_element_by_xpath('//div[@class="T-I J-J5-Ji T-I-KE L3 T-I-KL"]')
        create_email.click();

    except:

        create_email = browser.find_element_by_xpath('//div[@class="T-I J-J5-Ji T-I-KE L3 T-I-KL"]')
        create_email.click();

    file = open(csv_file)
    emailString = file.read()
    
    to = browser.find_element_by_xpath('//textarea[@name="to"]')
    to.send_keys(emailString)
    file.close()
    
    subject_box = browser.find_element_by_xpath('//input[@name="subjectbox"]')
    subject_box.send_keys(subject)

    bodybox = browser.find_element_by_xpath('//div[@class="Am Al editable LW-avf"]')
    bodybox.send_keys(body)

    sendButton = browser.find_element_by_xpath('//div[@class="T-I J-J5-Ji aoO v7 T-I-atl L3 T-I-KL"]')
    sendButton.click()

chrome_driver_file_name = input("Enter your chrome driver file name >> ")
csv_file_name = input("Enter your csv file name containing the email list >> ")
email = input("Enter your email (Gmail) >> ")
password = input("Enter your password >> ")
subject = input("Enter email subject >> ")
body = input ("Enter email body >> ")

sendEmail(chrome_driver_file_name, csv_file_name, email, password, subject, body)

#Just to keep the browser window open until the emails are sent
done = input("")

