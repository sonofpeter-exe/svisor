from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('C:/Users/Rinkie/Documents/Coding/Web/shopping/spar/GROCERIES.html')

# select & traverse categories
cat = driver.find_element_by_tag_name('select')
li = cat.find_elements_by_tag_name('option')

for i in li:
    print(i.text)
# cards = driver.find_elements_by_class_name('product-grid-block')
# for i in cards:
#     name = i.find_element_by_class_name('prod_card_title')
#     p = list(i.find_element_by_class_name('product-item--price').text.split('\n')[0].strip())
#     p.insert(-2, '.')
#     p = ''.join(p)
#     # img = i.find_element_by_tag_name('img')
#     ig = i

#     print(name.text)
#     print(p)
#     print(img)
#     print()

# print(help(By))

# lis = driver.find_elements_by_tag_name('ul')
# for i in lis:
#     try:
#         if i.By.LINK_TEXT == 'Browse Products':
#             li = i.find_elements_by_tag_name('li')
#             print(li.text)
#         # i.find_element_by_class_name('sub-navigation-list')
#         # print(i.text)
#     except:
#         pass
# driver.find_elements_by_class_name('sub-navigation-list')
# print(len(lis))
# li = lis.find_elements_by_tag_name('li')
# for i in li:
#     print(i.text)


driver.quit()
# lis = driver.find_element_by_tag_name('ul').find_element_by_class_name('sub-navigation-list')
# ('ul', class_='sub-navigation-list')
# print(lis)
# driver.close()