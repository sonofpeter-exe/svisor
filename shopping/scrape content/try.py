from neo4j import GraphDatabase
import os
from bs4 import BeautifulSoup as bs
import requests

# with open('C:/Users/Rinkie/Documents/Coding/Web/shopping/shoprite/fruit.html') as srite:
#     source = bs(srite, 'lxml')

# pic = source.find_all('img', attrs={'alt': 'Golden Apples Pack 1kg'})[0]['src']
# res = requests.get(pic)
# print(res.status_code)

# path = os.path.abspath('C:\\Users\\Rinkie\\Documents\\Coding\\Web\\shopping\\shoprite\\Apples & Pears _ Fresh Fruit _ Fresh Food _ Food _ Shoprite ZA_files')
# os.chdir('C:\\Users\\Rinkie\\Documents\\Coding\\Web\\shopping\\shoprite\\Apples & Pears _ Fresh Fruit _ Fresh Food _ Food _ Shoprite ZA_files')
# print(path)

root = os.path.abspath('C:\\Users\\Rinkie\\Documents\\Coding\\Web\\test\\django_project\\explore\\static\\explore')
os.chdir(root)

tmp = ['a', 'b', 'c']

path = '\\'.join(tmp)
root = 'tmp'


# if not os.path.isdir(path):
#     os.makedirs(path)
#     os.chdir(os.path.join(root, path))
#     # Populate
# elif os.path.isdir(path):
#     os.chdir(os.path.join(root, path))
#     # Populate



# path = os.path.abspath(p)
print(os.path.join(root, path))
# print(os.getcwd())
exit()

graphdb = GraphDatabase.driver(uri = 'neo4j://localhost:7687', auth=('neo4j', 'MSoulZA01#'))
session = graphdb.session()




def deputise(i):

    # i = str(i)
    i = i.replace(',', '')
    i = i.replace('&', 'And')
    i = i.replace(' ', '')
    # print(i)
    return i

def rope(o):
    return [list(i.values())[:] for i in o]
# view = clip(child)
# for idx in view:
#     path_finder(parent, name, promo, idx)

def path_finder(parent, child, name, promo, idx):
    if child == 'Health Range':
        nchild = deputise('Health Range')
        link(nchild, name, promo)
    elif 'Frozen' in child:
        pass
    elif parent == 'Convenience Meals':
        if child == 'Deli & Party Snacks & Dips':
            nchild = deputise('COOKED MEATS, SANDWICH FILLERS & DELI')
            session.run(f"MATCH (dep:{nchild}) MREGE (m:Meta {{name: '{nchild}Meta'}}) MERGE (mn:MetaNode {{name:'Deli & Party Snacks & Dips'}}) MERGE (dep)-[:Link]->(m)->[:Link]->(mn) ")
            link(nchild, name, promo)
        elif child == 'Desserts':
            nchild = deputise('FRESH & CHILLED DESSERTS')
            link(nchild, name, promo)
        else:
            nchild = deputise('READY MEALS')
            link(nchild, name, promo)
    else:
        if len(deps:= rope(session.run(f"MATCH (dep) where dep.department CONTAINS '{idx}' RETURN dep.department ").data())) > 1:
            nchild = rope(session.run(f"MATCH (dep:{deputise(parent)})-[:Link]->(d) where d.department CONTAINS '{idx}' RETURN d.department ").data())[0]
            link(nchild,name,promo)
        elif len(deps) == 1:
            link(deps[0], name, promo)

def link(nchild, name, promo):
    
    if nchild == 'Health Range':
        session.run(f"MATCH (d:FreshFood) MERGE (dp:{nchild} {{department:'Health Range'}}) MERGE (p:Stock {{name:'{name}', promo:'{promo}'}}) MERGE (d)-[:Link]->(dp)-[:Link]->(p) ")
        return
    if meta:= rope(session.run(f"MATCH (dep:{nchild})-[:Link]->(m:Meta)-[:Link]->(o) where toLower('{name}') CONTAINS o.name return o.name").data()):
        prod = []
        for j in meta:
            prod += rope(session.run(f"MATCH (dep:{nchild})-[:Link]->(p:Stock) where toLower(p.name) CONTAINS '{j}' return p.name "))
        prod = set(prod)
        if relation(prod, name)[1] == 100:
            pass
        else:
            session.run(f"MATCH (d:{nchild}) MERGE (p:Stock {{name:'{name}', promo:'{promo}'}}) MERGE (d)-[:Link]->(p) ")
    else:
        if dep:= rope(session.run(f"MATCH (d)-[:Link]->(dep)-[:Link]->(m:Meta)-[:Link]->(o) where toLower('{name}') CONTAINS o.name return d.department, dep.department").data()):
            for i in dep:
                parent, child = i[0], i[1]
                for idx in clip(i[1]):
                    path_finder(parent, child, name, promo, idx)
            # session.run(f"MATCH (d:{dep[0]}) MERGE (p:Stock {{name:'{name}', promo:'{promo}'}}) MERGE (d)-[:Link]->(p) ")
        else:
            pass
            # session.run(f"MATCH (d:{nchild}) MERGE (p:Stock {{name:'{name}', promo:'{promo}'}}) MERGE (d)-[:Link]->(p) ")

# print(dep:= rope(session.run(f"MATCH (d)-[:Link]->(dep)-[:Link]->(m:Meta)-[:Link]->(o) where toLower('PnP Golden Delicious Apples 1.5kg') CONTAINS o.name return d.department, dep.department").data())[:])




# if parent != 'xxx':
#                         # narrow search, find parent dep linked to child, return child dep
#                         nchild = session.run(f"MATCH (dep:{clip(parent)})-[:Link]->(d) where d.department CONTAINS '{idx}' RETURN d.department ").data()
#                         # validate child - prod relationship
#                         # if meta knows about the prod and prod not in dep, add
#                         if meta:= rope(session.run(f"MATCH (dep:{nchild})-[:Link]->(m:Meta)-[:Link]->(o) where toLower({name}) CONTAINS o.name return o.name").data()):
#                             prod = []
#                             for j in meta:
#                                 prod += rope(session.run(f"MATCH (dep:{nchild})-[:Link]->(p:Stock) where toLower(p.name) CONTAINS '{j}' return p.name "))
#                             prod = set(prod)
#                             if relation(prod, name) == 100:
#                                 pass
#                             else:
#                                 session.run(f"MATCH (d:{nchild}) MERGE (p:Stock {{name:'{name}', desc:'{desc}'}}) MERGE (d)-[:Link]->(p) ")


# if len(deps:= rope(session.run(f"MATCH (dep) where dep.department CONTAINS 'Fruit' RETURN dep.department ").data())) > 1:
#     if parent != 'Convenience Meals':
#         nchild = session.run(f"MATCH (dep:{deputise(parent)})-[:Link]->(d) where d.department CONTAINS 'Fruit' RETURN d.department ").data()
#         if meta:= rope(session.run(f"MATCH (dep:{nchild})-[:Link]->(m:Meta)-[:Link]->(o) where toLower({name}) CONTAINS o.name return o.name").data()):
#             prod = []
#             for j in meta:
#                 prod += rope(session.run(f"MATCH (dep:{nchild})-[:Link]->(p:Stock) where toLower(p.name) CONTAINS '{j}' return p.name "))
#             prod = set(prod)
#             if relation(prod, name) == 100:
#                 pass
#             else:
#                 session.run(f"MATCH (d:{nchild}) MERGE (p:Stock {{name:'{name}', desc:'{desc}'}}) MERGE (d)-[:Link]->(p) ")


# deps = session.run(f"MATCH (n:MetaNode) return n.name").data()

# if num:= 4:
#     print(num)
# for i in deps:
# print([list(i.values())[0] for i in deps])
# print(help(values()))



# print(len(deps))


# for i in li:
#     print([j for i,j in i.items()][0])