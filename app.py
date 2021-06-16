from selenium import webdriver

start_node = 'https://www.youtube.com/watch?v=6TEwVDNA7bI'

driver = webdriver.PhantomJS()
driver.get(start_node)
tags = driver.find_element_by_class_name('iv-click-target')
print(tags)
