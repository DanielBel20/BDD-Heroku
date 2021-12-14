from pytest_bdd import scenarios, when, then, given, parsers
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Constants

ADDREMOVEELEMENTSPAGE = 'https://the-internet.herokuapp.com/add_remove_elements/'
TITLE = (By.CSS_SELECTOR, "div h3")
ADD_ELEMENT_BUTTON = (By.CSS_SELECTOR, 'button[onclick="addElement()"]')
DELETE_BUTTON = (By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')

# Scenarios

scenarios('../features/herokuAddRemoveElementsPage.feature')

# Shared Given Steps

@given('the Heroku add remove elements page is displayed')
def add_remove_elements_page(browser):
    browser.get(ADDREMOVEELEMENTSPAGE)

# When Steps

@when('the user click on Add Element button')
def click_add_element_button(browser):
    addElementButton = browser.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    addElementButton.click()

@then('the delete button will be displayed')
def check_add_element_button_is_displayed(browser):
    deleteButton = browser.find_element(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
    assert deleteButton.is_displayed(), 'The delete button is not displayed'
