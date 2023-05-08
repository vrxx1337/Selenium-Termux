from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1920, 1080))
display.start()

options = webdriver.FirefoxOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Firefox(options=options)
driver.get("https://github.com")
driver.save_screenshot("/sdcard/download/screenshot.png")

driver.quit()
display.stop()