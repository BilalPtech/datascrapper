from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def get_article_hrefs(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(url)
    time.sleep(5)

    all_hrefs = set()

    while True:
        soup = BeautifulSoup(driver.page_source, 'lxml')
        
        content_area = soup.find('div', class_='content-area')
        if not content_area:
            break
        
        articles = content_area.find_all('article')
        for article in articles:
            article_header = article.find('header',{'class':'entry-header'})
            article_h2 = article_header.find('h2',{'class':'entry-title'})
            a = article_h2.find('a')
            href = a.get('href')
            if href:
                all_hrefs.add(href)

        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1.2);")
            time.sleep(2)
            older_posts_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@class="content-area"]//main[@class="site-main"]//div[@id="infinite-handle"]//button[text()="Older posts"]'))
            )
            older_posts_button.click()
            print('OlderPost Btn Clicked')
            time.sleep(5)

        except TimeoutException:
            print('No more Older posts button')
            break

    driver.quit()

    return list(all_hrefs)