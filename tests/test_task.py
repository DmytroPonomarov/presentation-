from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def page_loaded_successfully_test(chrome_browser):
    chrome_browser.get('https://github.com/django/django')
    chrome_browser.maximize_window()

    WebDriverWait(chrome_browser, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.commit-tease-sha'))
    )
    commit_id = len(chrome_browser.find_elements_by_css_selector('.commit-tease-sha'))

    assert commit_id == 1


def last_commit_displaying_successfully_test(chrome_browser):
    commit_id_in_repo = chrome_browser.find_element_by_css_selector(
        '.commit-tease-sha'
    ).get_attribute('innerText')

    commits_page = chrome_browser.find_element_by_css_selector('.commits')
    commits_page.click()
    WebDriverWait(chrome_browser, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.commit-group'))
    )

    latest_commit_id = chrome_browser.find_element_by_css_selector(
        '.commit:first-child .sha'
    ).get_attribute('innerText')

    assert commit_id_in_repo == latest_commit_id

