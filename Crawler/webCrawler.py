from selenium import webdriver
import re
import urllib.request
from flask import jsonify, json
import sys


def getProductName(driver):
	return driver.find_elements_by_class_name('''B_NuCI''')[0].text

def getAverageRating(driver):
	return driver.find_elements_by_class_name('''_3LWZlK''')[0].text

def getTotalRatings(driver):
	TotalRatings = driver.find_elements_by_xpath('''//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]/span/span[1]''')[0].text
	return ''.join(TotalRatings.strip().split(' ')[0])

def getTotalReviews(driver):
	TotalReviews = driver.find_elements_by_xpath('''//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]/span/span[3]''')[0].text
	return ''.join(TotalReviews.strip().split(' ')[0])

def getMaxRetailPrice(driver):
	try:
		MaxRetailPrice = driver.find_elements_by_xpath('''//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]''')[0].text
	except:
		MaxRetailPrice = driver.find_elements_by_xpath('''//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div''')[0].text
	return MaxRetailPrice[1:]+'/-'

def getStorePrice(driver):
	try:
		StorePrice = driver.find_elements_by_class_name('''_3I9_wc''')[0].text
	except:
		StorePrice = driver.find_elements_by_class_name('''_19_Y9G''')[0].text
	return StorePrice[1:]+'/-'

def getDiscount(driver):
	Discount = driver.find_elements_by_xpath('''//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[3]/span''')[0].text
	return ''.join(Discount.strip().split(' ')[0])

def crawler(driver,url_to_crawl,prod_cnt):

	driver.get(url_to_crawl)	

	print( {
		"Product Name" : getProductName(driver),
		"Average Rating" : getAverageRating(driver),
		"TotalRatings" : getTotalRatings(driver),
		"TotalReviews" : getTotalReviews(driver),
		"MaxRetailPrice" : getMaxRetailPrice(driver),
		"StorePrice" : getStorePrice(driver),
		"Discount" : getDiscount(driver) }
	, file=sys.stderr)

	# return jsonify({
	# 	"Product Name" : getProductName(driver),
	# 	"Average Rating" : getAverageRating(driver),
	# 	"TotalRatings" : getTotalRatings(driver),
	# 	"TotalReviews" : getTotalReviews(driver),
	# 	"MaxRetailPrice" : getMaxRetailPrice(driver),
	# 	"StorePrice" : getStorePrice(driver),
	# 	"Discount" : getDiscount(driver) })

	# print(getProductName(driver),file=sys.stderr)




	
