from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
driver.get("https://github.com")
driver.save_screenshot("/sdcard/download/screenshot.png")
driver.quit()