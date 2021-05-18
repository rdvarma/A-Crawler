from selenium import webdriver
import time

def extract_links(driver, url, category):
    driver.get(url)
    popup_close_btn = driver.find_element_by_class_name('''_2doB4z''')
    popup_close_btn.click()

    search_bar = driver.find_element_by_class_name("_3704LK")
    search_bar.send_keys(category + "\n")
    search_icon = driver.find_element_by_class_name("L0Z3Pu")
    search_icon.click()

    time.sleep(5)
    
    limit = 100
    cnt = 1

    product_links = list()

    while cnt <= limit:

        try:
            links = driver.find_elements_by_class_name("_1fQZEK")
            urls = []
            for link in links: 
                if link not in product_links:
                    product_links.append(link.get_attribute("href"))
        except:
            next = driver.find_element_by_class_name("_1LKTO3")
            next.click()

        cnt += 1

    return product_links


    