from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def chrome_webdriver():
    chromedriver_path = '/Users/mymac/data/chromedrv/chromedriver'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                'Chrome/123.0.0.0 Safari/537.36'
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--headless')
    options.add_argument(f'user-agent={user_agent}')
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

url = 'https://www.etoro.com/api/sts/oauth/v3/auth'
driver = chrome_webdriver()
driver.request("POST", url, data = """{
  "loginIdentifier": "",
  "password": "",
  "requestedScopes": [],
  "isTemporalDevice": false,
  "deviceTokens": []
}""")
driver.implicitly_wait(10)
print(driver.page_source)
