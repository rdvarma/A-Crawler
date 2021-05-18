from flask import Flask, Response, json
from selenium import webdriver
import sys

from Crawler.webCrawler import crawler
# from Crawler.productDetails import getProductURLS
from Crawler.linkExtractor import extract_links

app = Flask(__name__)

@app.route('/')
def crawl_the_url():

	driver_path = r"C:\\Users\\Others\\WebDriver\\geckodriver.exe"

	driver = webdriver.Firefox(executable_path=driver_path)
	
	site_url = "https://www.flipkart.com"
	category = "mobiles"
	product_urls = extract_links(driver, site_url, category)

	for prod_cnt, url_to_crawl in enumerate(product_urls,1):
		data = crawler(driver,url_to_crawl,prod_cnt)	
		

	driver.close()

	return Response("test",status=200,mimetype="text/html")


	 