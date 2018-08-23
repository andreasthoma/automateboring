#! Python3
# Test run of Selenium

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://waltho.solar')

# Find element on page and click.


# Find element on page and send information.

for i in range(3):
    emailAddress = 'arjun' + str(i) + 'sbcglobal.com'
    idElem = browser.find_element_by_class_name('input_sol')
    idElem.send_keys(emailAddress)
    typeElem = browser.find_element_by_link_text('Comercial')
    typeElem.click()
    idElem.submit()
    browser.refresh()

# TODO: Refresh the browser and do it again.
