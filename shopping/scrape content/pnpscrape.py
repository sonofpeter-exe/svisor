from bs4 import BeautifulSoup as bs
from requests import get
from neo4j import GraphDatabase
from fuzzywuzzy import process
import re
import json

graphdb = GraphDatabase.driver(uri = 'neo4j://localhost:7687', auth=('neo4j', 'MSoulZA01#'))
session = graphdb.session()
with open('C:/Users/Rinkie/Documents/Coding/Web/shopping/pnp/fruit.html') as pnp:
    source = bs(pnp, 'lxml')

dirs = source.find('ul', class_='item-container')

def traverse(src):
    for i in src.find_all('div')[:5] + src.find_all('div')[-1:]:
        if i:
            col = i.find('li')
            parent = col.text.upper().strip()
            print('TITLE:', parent)
            if col:
                for j in i.find_all('a')[2:]:
                    child = clean(j.text)
                    print(' -', child)
                    # link = bs(j['href'])
                    # scrape(link)
        print()

def scrape(parent, child, src, idx=0):
    items = src.find('div', class_='totalResults').text.strip().split()[-1]
    pages = int(items)//18

    # CHECK IF PAGES > 1
    if src.find('ul', class_='pagination').find_all('a')[:-1][0]['href']:
        pg = src.find('ul', class_='pagination').find_all('a')[:-1][0]['href'][:-1]

    # SCRAPE
    if idx <= pages:
        for card in source.find_all('div', class_='product-card-grid'):
            print(name:=card.find('div', class_='item-name').text) # assign name
            print(price:=f"{source.find('div', class_='currentPrice').text.strip()[:-2]}.{source.find('div', class_='currentPrice').text.strip()[-2:]}") #assign price
            promo = None
            if card.find('div', class_='promotionContainer').a: #assign promo
                print(promo:=card.find('div', class_='promotionContainer').text.strip())
                promo = None
#             desc = None #assign desc
            img = card.find('div', class_='thumb').img['alt'] #assign image
            print('img -', img)
            print('#######################')

            # 1) match child dep
            view = clip(child)
            for idx in view:
                if path_finder(child, parent, name, promo, idx):
                    print('was true')
                    break
# traverse(dirs)

def clean(txt):
    txt = txt.replace('Ã«', 'E')
    txt = txt.replace('Ã‰', 'E')
    txt = txt.replace('Â®', '')
    return txt

def deputise(i):
    i = i.replace(',', '')
    i = i.replace('&', 'And')
    i = i.replace(' ', '')
    return i

def clip(x):
    return re.split(', |& ', x)

def rope(o):
    return [list(i.values())[0] for i in o]

def relation(lis, prod):
    if lis:
        return process.extractOne(prod, lis)
    return 0

def path_finder(child, parent, name, promo, idx):
    if child == 'Health Range':
        nchild = deputise('Health Range')
        if link(nchild, name, promo):
            return True
    elif 'Frozen' in child:
        pass
    elif parent == 'Convenience Meals':
        if child == 'Deli & Party Snacks & Dips':
            nchild = deputise('COOKED MEATS, SANDWICH FILLERS & DELI')
            session.run(f"MATCH (dep:{nchild}) MREGE (m:Meta {{name: '{nchild}Meta'}}) MERGE (mn:MetaNode {{name:'Deli & Party Snacks & Dips'}}) MERGE (dep)-[:Link]->(m)->[:Link]->(mn) ")
            if link(nchild, name, promo):
                return True
        elif child == 'Desserts':
            nchild = deputise('FRESH & CHILLED DESSERTS')
            if link(nchild, name, promo):
                return True
        else:
            nchild = deputise('READY MEALS')
            if link(nchild, name, promo):
                return True
    elif child.split()[-1] == 'Shop':
        if name in session.run(f"MATCH (d:Snacks)-[:Link]->(p:Stock) RETURN p.name ").data():
            # pend prod to child, child to parent
        # if prod in snacks, link shop to prod else create prod
            pass
    else:
        if len(deps:= rope(session.run(f"MATCH (dep) where dep.department CONTAINS '{idx}' RETURN dep.department ").data())) > 1:
            nchild = rope(session.run(f"MATCH (dep:{deputise(parent)})-[:Link]->(d) where d.department CONTAINS '{idx}' RETURN d.department ").data())[0]
            if link(nchild, name, promo):
                return True
        elif len(deps) == 1:
            if link(deps[0], name, promo):
                return True

def link(nchild, name, promo):
    
    if nchild == 'Health Range':
        session.run(f"MATCH (d:FreshFood) MERGE (dp:{nchild} {{department:'Health Range'}}) MERGE (p:Stock {{name:'{name}', promo:'{promo}'}}) MERGE (d)-[:Link]->(dp)-[:Link]->(p) ")
        return True
    if meta:= rope(session.run(f"MATCH (dep:{nchild})-[:Link]->(m:Meta)-[:Link]->(o) where toLower('{name}') CONTAINS o.name return o.name").data()):
        prod = []
        for j in meta:
            prod += rope(session.run(f"MATCH (dep:{nchild})-[:Link]->(p:Stock) where toLower(p.name) CONTAINS '{j}' return p.name "))
        prod = set(prod)
        if relation(prod, name)[1] == 100:
            print('found')
            pass
        else:
            # session.run(f"MATCH (d:{nchild}) MERGE (p:Stock {{name:'{name}', promo:'{promo}'}}) MERGE (d)-[:Link]->(p) ")
            print(f"({nchild})-[:Link]-({name})")
            return True
    else:
        if dep:= rope(session.run(f"MATCH (d)-[:Link]->(dep)-[:Link]->(m:Meta)-[:Link]->(o) where toLower('{name}') CONTAINS o.name return d.department, dep.department").data()):
            for i in dep:
                parent, child = i[0], i[1]
                view = clip(child)
                for idx in view:
                    if path_finder(child, parent, name, promo, idx):
                        return True
            # session.run(f"MATCH (d:{dep[0]}) MERGE (p:Stock {{name:'{name}', promo:'{promo}'}}) MERGE (d)-[:Link]->(p) ")
        else:
            # print(f"({nchild})-[:Link]-({name})")
            print('failed')
            pass
            # session.run(f"MATCH (dep:{parent}) MERGE (d:{child}) MERGE (p:Stock {{name:'{name}', promo:'{promo}'}}) MERGE (dep)-[:Link]->(d)-[:Link]->(p) ")

scrape('Fresh Food', 'Fruit', source)