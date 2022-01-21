from bs4 import BeautifulSoup as bs
from requests import get

with open('C:/Users/Rinkie/Documents/Coding/Web/shopping/shoprite/fruit.html') as srite:
    source = bs(srite, 'lxml')

dirs = source.find('ul', class_='sub-navigation-list')

dep = []
tmp = []
num = 0

def traverse(src):
    global dep, tmp, num
    try:
        for li in src.find_all('li')[1:3]:
            col = source.find('div', class_=f'{li["id"]}')
            if col and col.li:
                # print(li.text.strip(), int(col['col'])-1)
                dep += [li.text.strip(), int(col['col'])-1]

                if int(col['col'])-1 > num:
                    num = int(col['col'])-1
                elif int(col['col'])-1 <= num:
                    num = int(col['col'])-1
                    tmp = tmp[:num-1]
                
                if int(col['col'])-1 == 1:
                    tmp = [li.text.strip()]
                else:
                    tmp += [li.text.strip()]
                
                print(tmp)
                traverse(col)
            else:
                # print(li.a['href']) 
                # link = get(li.a['href']).text
                link = li.a['href']
                # ns = bs(link, 'lxml')
                # dep += [li.text]
                # scrape(link)
            
        print()

    except AttributeError:
        pass

trav(dirs)