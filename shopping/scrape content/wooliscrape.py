from bs4 import BeautifulSoup as bs


with open('C:/Users/Rinkie/Documents/Coding/Web/shopping/woolworths/Buy Fresh Salads, Fruit And Vegetables Online _ Woolworths.co.za.html') as wooli:
    source = bs(wooli, 'lxml')

d1 = source.find('nav', id='main-nav').ul
food = d1.find_all('li', class_='main-nav__list-item--primary')[1]
ul = food.find('ul', class_='main-nav__list--secondary')
def traverse(src):
    out = False
    for li in ul.find_all('li'):
        if out == True:
            break
        co = li.find('ul', class_='list--silent')
        if co:
            for i in co:
                print(i.find('a').text)
                if i.find('a').text.strip() == 'Food Cupboard':
                    b = i.find('ul')
                    for j in b:
                        print(j.text)
                if i.find('a').text.strip() == 'Beverages & Juices':
                    out = True
                    break
            print()


def scrape(src):
    global inventory
    # GET PAGINATION
    items = src.find('label', class_='product-records__count').text.split()[0]
    pages = int(items)//60

    # TRAVERSE PAGES
    # for idx in range(1): # pages+1
    #     # GENERATE NEXT PAGE LINK
    #     for pg in source.find('ul', class_='pagination').find_all('a')[:-1]:
    #         curr = bs(f'{pg["href"][:-1]}{idx}', 'lxml')
            # SCRAPE CONTENT ON EACH PAGE
    cnt = 0
    for card in src.find_all('article', class_='product-card'):
        # print('found')
        try:
            name = card.find('a', class_='range--title').text.strip()
            # print(name)
            price = card.find('div', class_='product__price').text.strip()
            # desc = card.find('div', class_='description').text
            # if not desc:
            #     desc = ''
            promo = card.find('div', class_='product--promotions').text.strip()
            if not promo:
                promo = '-'
            img = card.find('div', class_='product--image').img['alt']
            if not img:
                img = 'default img'
            # print('done')
            print(name, price, promo, img, sep='\n')
            
            id_ = name
            name = {'name' : name,
                    'price' : price,
                    'img' : img,
                    }
                    # 'desc' : desc,
                    # 'promo' : promo,
                    # 'dep' : dep}
            # SAVE ITEM IN INVENTORY
            inventory[id_] = name
            # print(name)
            print() #...
        except AttributeError:
            pass

inventory = {}

scrape(source)


# with open('inventory.json', 'w') as f:
#     json.dump(inventory, f)


