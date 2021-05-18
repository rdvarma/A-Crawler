from selenium import webdriver
import re
import urllib.request

##### WEB CRAWLER CLASS For ALL Operations ######
# class WebCrawler():

def crawl(driver,url_to_crawl,idx):
	##### FINDING BASIC INFO & GENERAL SPECS OF MOBILE ######
	# Product Name,Avg Rating,No of Ratings,No of Reviews,MRP,Store Price,Discount
	driver.get(url_to_crawl)
	elems1 = driver.find_elements_by_xpath('''//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]''')
	# We cannot seperate the detils from here....so need to extract seperately!!

	prod_name = driver.find_elements_by_xpath('''//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span ''')[0].text
	avg_rating = driver.find_elements_by_class_name('''_3LWZlK''')[0].text
	no_of_ratings = driver.find_elements_by_xpath('''//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]/span/span[1] ''')[0].text
	no_of_reviews = driver.find_elements_by_xpath('''//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]/span/span[3] ''')[0].text
	mrp = driver.find_elements_by_xpath('''//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1] ''')[0].text
	store_price = driver.find_elements_by_xpath('''//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[2] ''')[0].text
	discount = driver.find_elements_by_xpath('''//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[3]/span ''')[0].text


	basic_info = dict()

	basic_info['Product Name'] = prod_name
	basic_info['Average Rating'] = avg_rating
	basic_info['No of Ratings'] = ''.join(no_of_ratings.strip().split(' ')[0])
	basic_info['No of Reviews'] = ''.join(no_of_reviews.strip().split(' ')[0])
	basic_info['MRP'] = mrp[1:]+'/-'
	basic_info['Store Price'] = store_price[1:]+'/-'
	basic_info['Discount'] = ''.join(discount.strip().split(' ')[0])

	# print(basic_info)	

	elems2 =  driver.find_elements_by_class_name("_14cfVK")

	l = [] # Maintaining a list to store all the scraped data and futthur operate on it

	for i in elems2:
		l.append(i.text)

	# print(l)

	general_specs = l[0].split("\n") # As, all required specs are there in l[0] with '\n' as seperator
	# print(general_specs) 

	keys = []
	values = []

	for i in range(len(general_specs)):
		if i%2==0:
			# print(general_specs[i],end=" : ") 
			keys.append(general_specs[i])
		else:
			# print(general_specs[i])
			values.append(general_specs[i])

	g_specs = dict() # Dictionary to store the specs as Key-Value pairs
	for i in range(len(keys)):
		g_specs[keys[i]] = values[i]

	# print(d)

	with open('specs.txt', 'a') as fw:
		fw.write('\n####### PRODUCT' + str (idx)+ ' ######\n')
		fw.write('\n\n####### BASIC INFO ######\n')
		for k,v in basic_info.items():
			fw.write(k+' : '+v+'\n')
		fw.write('\n####### GENERAL SPECS ######\n')
		for k,v in g_specs.items():
			fw.write(k+' : '+v+'\n')


	####### EXTRACT & SAVE SINGLE IMAGE OF PRODUCT #######

	img = driver.find_element_by_xpath('''//*[@id="container"]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/img''')

	src_url = img.get_attribute('src')
	print(src_url)
	urllib.request.urlretrieve(src_url, filename="./product-img"+str(idx)+".png")

	####### EXTRACT & SAVE ALL IMGS OF PRODUCT #######
	# ...