from flask import Flask
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select

from Crawler.webCrawler import crawl

app = Flask(__name__)

@app.route('/')
def crawl_the_url():
	driver_path = r"C:\\Users\\Others\\WebDriver\\geckodriver.exe"

	driver = webdriver.Firefox(executable_path=driver_path)

	urls = ["https://www.flipkart.com/mi-10i-atlantic-blue-128-gb/p/itm780df69dfa0fe?pid=MOBFZ4RNZMVZDZVH&lid=LSTMOBFZ4RNZMVZDZVHOXI1B4&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_13&otracker=nmenu_sub_Electronics_0_Mi&fm=organic&iid=4fa65a0a-ff92-43cf-b1d5-e13da40db41f.MOBFZ4RNZMVZDZVH.SEARCH&ppt=pp&ppn=pp&ssid=8iqgraj0ds0000001621320690265",
	"https://www.flipkart.com/infinix-smart-5-morandi-green-32-gb/p/itm8d968c7fe7d88?pid=MOBFZX3H2ARU2GHY&lid=LSTMOBFZX3H2ARU2GHY5J5UTT&marketplace=FLIPKART"]

	# wc = webCrawler()
	idx = 0
	for url_to_crawl in urls:
		idx+=1
		crawl(driver,url_to_crawl,idx)

	driver.close()

	return


	 