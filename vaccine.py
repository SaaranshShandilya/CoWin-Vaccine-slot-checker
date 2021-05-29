from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from twilio.rest import Client
options = webdriver.ChromeOptions()
account_sid = ''
auth_token = ''
phone_number={}
client = Client(account_sid, auth_token)
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = r"C:\Users\saara\OneDrive\Desktop\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
driver.maximize_window()
driver.get("https://selfregistration.cowin.gov.in/")
time.sleep(20)
ph=driver.find_element_by_xpath('//*[@id="mat-input-0"]')
ph.send_keys(phone_number)
time.sleep(20)
driver.find_element_by_xpath('//*[@id="main-content"]/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/ion-grid/form/ion-row/ion-col[2]/div/ion-button').click()
otp= input("Enter the otp")
time.sleep(60)
ot=driver.find_element_by_xpath('//*[@id="mat-input-1"]')
ot.send_keys(otp)
driver.find_element_by_xpath('//*[@id="main-content"]/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col/ion-grid/form/ion-row/ion-col[3]/div/ion-button').click()
time.sleep(10)
driver.find_element_by_xpath('//*[@id="main-content"]/app-beneficiary-dashboard/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid[1]/ion-row[2]/ion-col/ion-grid/ion-row[4]/ion-col[2]').click()
time.sleep(10)
driver.find_element_by_xpath('//*[@id="main-content"]/app-beneficiary-dashboard/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid[1]/ion-row[2]/ion-col/ion-grid/ion-row[4]/ion-col[2]/ul/li/a').click()
pin = input("Enter the pin for your locality")
i=1
while(i==1):    
    pi=driver.find_element_by_xpath('//*[@id="mat-input-2"]')
    pi.send_keys(pin)
    driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row[1]/ion-col[4]/ion-button').click()
    age = int(input("Enter age"))
    if(age>18 and age<=45):
        driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row[2]/ion-col[1]/div/div[1]/label').click()
        stat=driver.find_element_by_class_name('ng-star-inserted')
        # slots = stat.getText()
        if(stat!=None):
            i=0
            message = client.messages\
                .create(
                    body='Vaccines slots for 18+8 available. Kindly login and register into your slot.',
                    from_= '+17087616284',
                    to = '+91{phone_number}'
                )
        else:
            driver.refresh()
            time.sleep(10)
    elif(age>45):
        driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row[2]/ion-col[1]/div/div[2]/label').click()
        stat=driver.find_element_by_class_name('ng-star-inserted')
        slots = stat.getText()
        if(stat!=None):
            i=0
            message = client.messages\
                .create(
                    body='Vaccines slots for 45+ {slots} available. Kindly login and register into your slot.',
                    from_= '+17087616284',
                    to = '+91{phone_number}'
                )
        else:
            driver.refresh()
            time.sleep(10)
            
time.sleep(20000)
driver.close()