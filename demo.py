import time

from selenium import webdriver
APP_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

def enter_valid_credentials():
    print('1. launch th chrome browser...')
    chromeDriver = webdriver.Chrome(executable_path="E:\py_work\pythonprojects\drivers\chromedriver.exe")

    print('2. Enter the URl into address bar...!')
    chromeDriver.get(APP_URL)
    chromeDriver.maximize_window()
    time.sleep(5)

    print('3. Identify the element-- username,password,login_btn')
    username_element = chromeDriver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
    password_element = chromeDriver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
    login_btn = chromeDriver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

    print('4. Enter the data--such as/password click on login button')
    username_element.send_keys('Admin')
    password_element.send_keys('admin123')
    login_btn.click()
    time.sleep(5)

enter_valid_credentials()


# webdriver.Firefox()
# webdriver.Ie()
# webdriver.Edge()
# webdriver.Safari()
