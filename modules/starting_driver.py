from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def start_driver():
    chrome_settings = Options()
    arguments = ['--lang=pl', '--window-size=1000, 1300','--incognito']
    for argument in arguments:
        chrome_settings.add_argument(argument)
    chrome_settings.add_experimental_option('prefs',{
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options= chrome_settings)
    return driver