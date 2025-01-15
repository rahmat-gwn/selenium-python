from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
import time

@given('I open the Google homepage')
def step_open_google_homepage(context):
   context.driver = uc.Chrome()
   context.driver.get("https://www.google.com")
   
@when('I search for "{search_text}"')
def step_search_google(context, search_text):
    search_box = context.driver.find_element(By.NAME, "q")
    search_box.send_keys(search_text)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

@then('I should see results containing "{expected_text}"')
def step_verify_results(context, expected_text):
    page_source = context.driver.page_source
    assert expected_text.lower() in page_source.lower(), f"'{expected_text}' not found in search results"
    context.driver.quit()
