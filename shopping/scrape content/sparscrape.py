from bs4 import BeautifulSoup as bs
import requests

lnk = requests.get('https://www.shoprite.co.za/c-66/All-Departments/Food/Fresh-Food/Fresh-Fruit', verify=False)
# l = bs(lnk, 'lxml')

# source = l
# dirs = source.find('ul', class_='sub-navigation-list')
# dep, tmp, ln, num = [], [], '', 0



# traverse(dirs)

# sp = get('https://queenswood.spar.co.za/collections/groceries').text

# with open('C:/Users/Rinkie/Documents/Coding/Web/shopping/spar/GrROCERIES.html', encoding='utf8') as spar:
#     source = bs(spar, 'lxml')

# print(source.prettify())
# nav = source.find('ul', id='AccessibleNav')
# for i in nav:
#     print(i.text)

# def traverse(src):
#     for i in src.find_all('div')[:5] + src.find_all('div')[-1:]:
#         if i:
#             col = i.find('li')
#             print('TITLE:', col.text.upper().strip())
#             if col:
#                 for j in i.find_all('a')[2:]:
#                     print(' -', j['href'])
#                     link = bs(j['href'])
#                     # scrape(link)
#         print()
