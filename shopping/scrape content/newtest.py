from bs4 import BeautifulSoup as bs
from requests import get
import json
from neo4j import GraphDatabase
import re
import os


name, price, desc, department, img = [], [], [], [], []
#department + super directory
# directory -> department 
# {department : inventory()}
# {super-department : department}
# super-department == header carousel   

graphdb = GraphDatabase.driver(uri = 'neo4j://localhost:7687', auth=('neo4j', 'MSoulZA01#'))
session = graphdb.session()


# with open('C:/Users/Rinkie/Documents/Coding/Web/shopping/shoprite/fruit.html') as srite:
#     source = bs(srite, 'lxml')
def page(src):
    lnk = get(src, verify=False).text
    l = bs(lnk, 'lxml')
    return l

source = page('https://www.shoprite.co.za/c-66/All-Departments/Food/Fresh-Food/Fresh-Fruit')

dirs = source.find('ul', class_='sub-navigation-list')

dep, tmp, ln = [], [], ''
num = 0


def traverse(src):
    global dep, tmp, num, ln
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
                    ln = li.a['href']
                    # print(ln)
                
                # print(tmp)
                traverse(col)
            else:
                if len(tmp) > 0:
                    print(tmp, '-', li.text)
                    print('site:', ln)
                pg = page(f'https://www.shoprite.co.za{ln}')
                populate(tmp, pg)
                # scrape(source)
                exit()
                # print(li.a['href']) 
                # link = get(li.a['href']).text
                link = li.a['href']
                # ns = bs(link, 'lxml')
                # dep += [li.text]
                # scrape(link) 
        print('restart')           
        print()

    except AttributeError:
        pass

# pg = source.find('ul', class_='pagination').find_all('a')[:-1][0]['href']
# print(pg)

def clear(i):

    # i = str(i)
    i = i.replace(',', '')
    i = i.replace('&', 'And')
    i = i.replace(' ', '')
    # print(i)
    return i
        

def populate(tmp, pg):
    
    # q1 = 'MATCH (x) return x'
    # nodes = session.run(q1)
    # for node in nodes:
    #     print(node)
    

    for i in tmp:
        a = clear(i)
        dep = f'MERGE (cat:{a} {{department: "{a}" }})'
        session.run(dep)
    # i,j,k = tmp
    # d,e,f = clear(i), clear(j), clear(k)
    for i in range(len(tmp)):
        tmp[i] = clear(tmp[i])
    
    lnk = ''
    if len(tmp) == 3:
        lnk = 'MATCH (a:{}), (b:{}), (c:{}) MERGE (a)-[:Link]->(b) MERGE (b)-[:Link]->(c)'.format(*tmp)
    elif len(tmp) == 2:
        lnk = 'MATCH (a:{}), (b:{}) MERGE (a)-[:Link]->(b)'.format(*tmp)
    # elif len(tmp) == 1:
    #     lnk = 'MATCH (a:{0}), (b:{1}) CREATE (a)-[:Link]->(b)'.format(*tmp)


    session.run(lnk)
    # tmp1 = [d,e,f]
    # tmp.clear()
    source = pg
    print('made it:', tmp[-1])
    scrape(source, tmp)
    print('CAME BACK OUT')

    # q1 = 'MATCH (x) return x'
    # nodes = session.run(q1)

    # for node in nodes:
    #     print(node)
        
    # for i,j,k in deps:
    #     match (a:i.stirp()), (b:j.strip()), (c:k.strip()) create (a)-[:Link]->(b), (b)-[:Link]->(c)
    # last_link = lnk
    # dep_name = k
    # for i in lnk:
    #     match (a:i.strip()), (b:k.strip()) create (a)-[:Link]->(b)


def scrape(src, tmp, idx=0):
    global inventory, source
    # GET PAGINATION
    items = src.find('p', class_='total-number-of-results').text.split()[0]
    pages = int(items)//20 +1

    # CHECK IF PAGES > 1
    if src.find('ul', class_='pagination').find_all('a')[:-1][0]['href']:
        pg = src.find('ul', class_='pagination').find_all('a')[:-1][0]['href'][:-1]

    print('page', idx)

    # SCRAPE
    # if idx < pages:
    for card in src.find_all('div', class_='item-product'):
        try:
            name = card.find('h3', class_='item-product__name').text.strip()
            # print(name)
            price = card.find('div', class_='js-item-product-price').text.strip()[1:]

            # desc = card.find('div', class_='description').text
            # if not desc:
            #     desc = ''
            # promo = card.find('div', class_='promo').text
            # if not promo:
            #     promo = ''
            # src = img, alt = name
            alt = card.find('div', class_='item-product__image').img['alt']
            src = card.find('div', class_='item-product__image').img['src']
            if not src:
                src = 'default img'
            # print('done')
            
            id_ = name
            # tmp = clear(tmp)
            root = os.path.abspath('C:\\Users\\Rinkie\\Documents\\Coding\\Web\\test\\django_project\\products\\static\\products\\inventory')
            os.chdir(root)
            #create img path & save img
            dir_path = '\\'.join(tmp)
            # path = os.path.join(file_path, f'{name}')

            if not os.path.isdir(dir_path):
                os.makedirs(dir_path)
                os.chdir(os.path.join(root, dir_path))
            elif os.path.isdir(dir_path):
                os.chdir(os.path.join(root, dir_path))

            # with open(f'{alt}.png', 'wb') as f:
            #     f.write(f'{alt}')
            # img_path = os.path.join(os.getcwd(), f'{alt}.png')
            session.run(f'MATCH (a:{tmp[-1]}) CREATE (b:Stock {{name: "{name}", img: "{dir_path}"}}), (a)-[:Link]->(b)')
            print(name, price, '', sep='\n')
            name = {'name' : name,
                    'price' : price,
                    'img' : dir_path,
                    }
                    # 'desc' : desc,
                    # 'promo' : promo,
                    # 'dep' : dep}
            # SAVE ITEM IN INVENTORY
            inventory[id_] = name
            # print(name)
            # print() #...
        except AttributeError:
            pass
    idx += 1
    print('page', idx)
    print(pages)
    if idx < pages:
        # np = get().text
        source = page(f'https://www.shoprite.co.za{pg}{idx}')
        scrape(source, tmp, idx)


inventory = {}

# scrape(source)
# session.run('MATCH (x) DETACH DELETE x')
traverse(dirs)


# with open('inventory.json', 'w') as f:
#     json.dump(inventory, f)




# Fruit = ['apple', 'pear', 'banana']
# vegies = ['carrots', ]
# prefixes = ['pnp']

# # create (n.Stock {name=xxx, parent=xxx})

# dep, prod 

# prod_meta = re.split(', |& ', idx)

# deps = re.split(', |& ', prod.dep)

# create meta

# search for department where
# product contains meta name
# 1) split dep & prod 
# 2) for-loop compare search
# 3) 

# for depa in deps:
#     if depa.query is not null:
#         match prod w/meta
#     if match db.depa size(db.department) > 0:
#         for 
#         match n.stock where n.name =




# for i in prod_meta:
#     if i not in prefixes and i in deps-meta  (n.Stock):
#         f'MATCH (n.Stock) where n.parent = dep merge (n)-[:link]->(i)'
#         break
#     if i == (n.dep):
#         f'(n)-[:Link]->(i)'
#         break
#     f'MERGE (n:dep {{dep= {dep}}}) MERGE (nn:Stock {{name={i}}}) MERGE (n)-[:Link]->(nn)'


def clip(x):
    return re.split(', |& ', x)


def sift(dep, prod):

    departments = clip(dep)
    departments2 = clip(dep)
    product = clip(prod)

    linked = False

    '''
    1) look at incoming department, if dep = preped meat, look @ synonym
    2) if match returns > 1 result,
        - look at parent dep
        - if dep = conve, look at synonym
    3) validate incoming dep - product pairing
        - if valid
            > create population path
            > sniff redundance, send items to db:
        - if invalid
            > search meta partial_prod match
            > create new population path
            > sniff redundance, send items to db
    '''
    exclusion = ['fresh', 'frozen']
    departments = clear(departments)

    col2 = clip(departments2)
    col = clip(departments)

    if col2[0] not in exclusion:
        if col2[0] == 'Prepared':
            pass
        else:
            for idx in col2:
                if len(list(session.run(f"MATCH (dep) where dep.department CONTAINS '{idx}' RETURN dep "))) > 1:
                    if col[0] == 'Convenience':
                        pass
                    elif list(session.run(f"MATCH (d:{clear(departments)}), (dep) where dep.department CONTAINS '{idx}' RETURN dep IS NOT NULL ")):
                        dep = session.run(f"MATCH (d:{clear(departments)}), (dep) where dep.department CONTAINS '{idx}', (d)-[:Link]->(dep) RETURN dep.department ") #return department link
                        for i in dep:
                            if list(session.run(f"MATCH (d:{dep}), (d)-[:Link]->(m:Meta)->(o) where {i.name} CONTAINS o.name RETURN m IS NOT NULL")):
                                #sniff redundancy
                                session.run(f"MATCH (d:{dep}) MERGE (p:Stock {{name: '{i.name}'}}) MERGE (d)-[:Link]->(p) ")
                        popu(departments, idx)
                        session.run(f"MATCH (d:{clear(departments)}), (dep) where dep.department CONTAINS '{idx}' ")

def popu(dep, prod):
    if departments == 'Prepared':
        pass
    if departmets2 == 'Convenience':
        pass
    if len(list(session.run(f"MATCH (dep) where dep.department CONTAINS '{departments}' RETURN dep "))) > 1:
        dep = session.run(f"MATCH (dep) where dep.department CONTAINS '{departments2}' RETURN dep.department ")
        session.run(f"MATCH (dep:{dep})-[:Link]->(n), merge (n)-[:Link]->(prod) ")
    elif len(list(session.run(f"MATCH (dep) where dep.department CONTAINS '{departments}' RETURN dep "))) == 1:
        dep = session.run(f"MATCH (dep) where dep.department CONTAINS '{departments}' MERGE (n:Stock {{name:'{prod}'}}) MERGE (dep)-[:Link]->(n) ")


    departments = clear(departments)
    departments2 = clear(departments2)



    
    # for idx in product:
    #     if list(session.run(f"MATCH (m:Meta)-[:Link]->(o) where o.name CONTAINS '{idx}', (dep)-[:link]->(m), (p:Stock) where p.name CONTAINS '{idx}', (dep)-[:Link]->(p) "))



















    # 1st match closest depa
    # 2nd match depa w/prod_partial_match
    linked = False
    for depa in departments:
        if list(session.run(f'MATCH (n:{depa}) RETURN n IS NOT NULL')):
            for idx in product:
                if list(session.run(f'MATCH (n:{depa})-[:Link]->(m:Meta), (m)-[:Link]->(o) where toLower(o.name) CONTAINS "{idx.strip()}" return o.name is not null ')):
                    if list(session.run(f"MATCH (dep:{depa}) RETURN dep IS NOT NULL ")):


                        session.run(f"MATCH (prod:Stock) where prod.name CONTAINS '{prod.strip()}', (dep)-[:Link]->(prod) RETURN dep ")
                        print(prod)
                        linked = True
                        break
        if linked == True:
            linked = False
            return
    linked = alt()

    if not linked:
        for i in depa:
            if not null:
                session.run(f'MATCH (dep:"{i}"), create (p:Stock {{name: "{prod}"}}), (dep)-[:Link]->(p) ')
                break
    
def alt(deps):
    
    for i in prod:
        session.run(f'MATCH (dep)-[:Link]->(nn:Meta)-[:Link]->(o) where toLower("{prod}") CONTAINS o RETURN dep ')

        if list(q):
            # return the metas, if meta in partial_prod -> prod -> depa
            session.run(f'MATCH (nn:Meta), (dep)-[:Link]->(nn)-[:Link]->(o) where toLower("{prod}") CONTAINS o.name, CREATE (p:Stock {{name:"{prod}"}}), (dep)-[:Link]->(p) RETURN dep')
            return True
    return False




# sift('FreshFruit', 'apple, & rice, grapple')    

    #     if match n.depa is not null:
    #         match depa->meta
    #         find depa meta
    #         for i in prod: ["Delicious", "Standard", "Gold", "Apples", "1.5kg"]
    #             if meta contains partial_prod:
    #                 append
    #                 linked = True
    #                 break
    #     if linked == True:
    #         linked = False
    #         break
    # if linked == False:
    #     match depa w/prod_partial_match
    #     sift 

    





# print(inventory)


# issues:
# - stationery & newsagent conflicting w/ second column
# - n trigering exception
# - trigerring exception
#   - vitamin 50+ 
#   - nappies double underscore
#   - apostrophies
# - spaces between empty column 4s


# use try statements to find inner most child