from bs4 import BeautifulSoup as bs

class Product():
    def __init__(self, name, price, desc, department, img):
        self.name = name
        self.price = price
        self.desc = desc
        self.department = department
        self.img = img
    
    def __repr__(self):
        return f'{self.name}\n{self.price}\n{self.desc}\n{self.department}\n{img}'


name, price, desc, department, img = [], [], [], [], []
#department + super directory
# directory -> department 
# {department : inventory()}
# {super-department : department}
# super-department == header carousel   

# for i in super-dep:
#     for j in dep:
#         with open(j) as pnp:
#             scrape n populate
#             associate store with available inventory using foreign key 


def classify(txt):
    txt = txt.replace('&', 'and')
    txt = txt.replace('-', ' ')
    txt = txt.replace('Ã©', 'e')
    txt = txt.lower().replace(',', '').split()
    return '_'.join(txt)

with open('C:/Users/Rinkie/Documents/Coding/Web/shopping/shoprite/fruit.html') as srite:
    source = bs(srite, 'lxml')

dirs = source.find('ul', class_='sub-navigation-list')
# for li in dirs.find_all('li')[1:]:
#     pass# print(li.text.strip())   

def traverse(src):
    pg = src.find('p', class_='total-number-of-results').text.split()[0]
    pages = int(pg)//20

    for idx in range(1, pages+1):
        for pagi in source.find('ul', class_='pagination').find_all('a')[:-1]:
            curr = f'{pagi["href"][:-1]}{idx}'
            print(curr)
            # for card in curr.find_all('div', class_='item-product'):
            #     print(card.find('h3', class_='item-product__name').text.strip()) #name
            #     print(card.find('div', class_='js-item-product-price').text.strip()) #price
            #     print() #...
            # print(pagi['href'][:-1])

# traverse(source)

def trav(src):
    try:
        for li in src.find_all('li')[1:3]:
            col = source.find('div', class_=f'{li["id"]}')
            print(li.text.strip())
            if col and not col.li:
                print('yes') # traverse(col)
            else:
                trav(col)
        print()
    except AttributeError:
        pass

trav(dirs)


# col1 = dirs.find('div', class_='food')

# try:
#     # '''col 1'''
#     # dirs = source.find('div', class_='sub__navigation')
#     for li in dirs.find_all('li')[1:2]:
#         col2 = source.find('div', class_=f'{li["id"]}')
#     # '''col 2'''
#         for i in col2.find_all('li')[1:2]:
#             print(i.text.upper().strip()) 
#             col3 = source.find('div', class_=f'{i["id"]}')
#             if not col3.li:
#                traverse(col3)
#                 print('yes')
                
#     # '''col 3'''
#             for j in col3.find_all('li')[1:2]:
#                 print(' ', j.text.strip())
#     # '''col 4'''
#                 col4 = source.find('div', class_=f'{j["id"]}')
#                 # print(col4['sup-cat'])
#                 # co = source.find('div', class_=f'{classify(j.text.strip())}')
#                 # print(co['class'][-1])
#                 # if not col4.text.isalpha():
#                 #     # print('     no 4')
#                 #     print('     ###########################')
#                     # print('     No colum 4')
#                     # print('     ###########################')
#                 for k in col4.find_all('li')[1:2]:
#                     for l in range(pages)
#                     curr = k.a['href']
#                     for card in source.find_all('div', class_='item-product'):
#                         print(card.find('h3', class_='item-product__name').text.strip())
#                         print(card.find('div', class_='js-item-product-price').text.strip())
#                         print()

#                     # print('     ', k.a['href'], '---')
#                 print()
                
#             # print()
#         # print()
#     # print()
# except:
#     print('try again')

# shoprite = 20 items p.p
# page = innermost_page

# col3 = source.find('div', class_='red')
# print(col3)



# for card in source.find_all('div', class_='item-product'):
#     print(card.find('h3', class_='item-product__name').text.strip())
#     print(card.find('div', class_='js-item-product-price').text.strip())
#     print()


# image = card.find('div', class_='item-product__image').img
# name = card.find('h3', class_='item-product__name').text
# price = card.find('div', class_='js-item-product-price').text
# promo
# desc 



# page = web traversal > curr page = page > get pg > loop products > curr page = next pg



# use try statements to find inner most child