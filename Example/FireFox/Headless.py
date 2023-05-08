from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)
driver.get("https://github.com")
driver.save_screenshot("/sdcard/download/screenshot.png")

driver.quit()