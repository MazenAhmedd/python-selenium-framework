import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browserType = "chrome"
if "chrome" in browserType:
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif "firefox" in browserType:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())

wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# creating an object of the ActionChains class to perform the mouse/ keyboard actions
action = ActionChains(driver)
menu = driver.find_element(By.ID, "mousehover")
action.move_to_element(menu).perform()  # perform method is always mandatory to perform all the chained actions
childMenu = driver.find_element(By.LINK_TEXT, "Top")
action.move_to_element(childMenu).click().perform()
############################################################################
# Context Click - Right click
driver.get("https://the-internet.herokuapp.com/context_menu")
action.move_to_element(driver.find_element(By.ID, "hot-spot")).context_click().perform()
alert = driver.switch_to.alert
assert "You selected a context menu" in alert.text
time.sleep(3)
#######################################################
# action.double_click(driver.find_element(By.ID, "Whatever")).perform()
