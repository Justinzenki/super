from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('http://jeremydomasian.github.io/supercalc_v1-4/SuperCalc-v2.html')

browser.maximize_window()

twoButton = browser.find_element_by_name('two')
nineButton = browser.find_element_by_name('nine')
count = 0
while(count < 5):
    twoButton.click()
    time.sleep(.25)
    count = count +1

nineButton.click()

time.sleep(.25)

minusButton = browser.find_element_by_name('minus')
minusButton.click()

time.sleep(.25)

oneButton = browser.find_element_by_name('one')
oneButton.click()

zeroButton = browser.find_element_by_name('zero')
zeroButton.click()

time.sleep(.25)

equalButton = browser.find_element_by_name('DoIt')
equalButton.click()
