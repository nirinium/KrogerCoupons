from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

ios6ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25"
 
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
options.add_argument("--user-agent=" + ios6ua);
options.binary_location = "C:\Python27\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(options.binary_location)
driver.get('https://www.kroger.com/coupons/login?program=DigitalCoupons&redirectUrl=https%3A%2F%2Fkroger.softcoin.com%2Fp%2Fnp%2F4230%2Flogin%2Fpayload%2Fprocess%3Fdestination%3D%2Fprograms%2Fkroger%2Fdigital_coupons%2F%26banner%3DKroger%26origin%3DDigitalCoupons')

#login 
username = driver.find_element_by_xpath('//*[@id="SignIn-emailInput"]')
password = driver.find_element_by_xpath('//*[@id="SignIn-passwordInput"]')
#send keys for login
username.clear()
username.send_keys("email@email.com")
time.sleep(5)
password.clear()
password.send_keys("password")
time.sleep(5)
#click sign in button
driver.find_element_by_xpath('//*[@id="SignIn-submitButton"]').click()



