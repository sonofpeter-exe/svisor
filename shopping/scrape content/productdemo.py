class Product():
    name = models.CharField(max_val=30)
    price = models.DecimalField(max_val=x)
    promo = models.CharField(max_val=x)
    desc = models.TextField()
    department = models.CharField(max_val=30)
    img = models.CharField(max_val=x)


    def __init__(self, name, price, desc, department, img):
        self.name = name
        self.price = price
        self.desc = desc
        self.department = department
        self.img = img
    
    def __repr__(self):
        return f'{self.name}\n{self.price}\n{self.desc}\n{self.department}\n{img}'



# scrape to json
# populate table from json
# create a store profile
# - store inventory
# - loc/com status
# - location
# - inventory key
# - vendor-product table
# display store from db


# scrape to json

product = {
    name : ['pro 1', 'pro 2', 'pro 3', 'pro 4', 'pro 5'],
    price : ['price 1', 'price 2', 'price 3', 'price 4', 'price 5'],
    department : ['dep 1', 'dep 2', 'dep 3', 'dep 4', 'dep 5'],
    desc : ['desc 1', 'desc 2', 'desc 3', 'desc 4', 'desc 5'],
    img : ['img 1', 'img 2', 'img 3', 'img 4', 'img 5']
}


# departments = {}
# for i in inventory:
#     departments[i.department] += i

# populate from json

for i in range(len(name)):
    globals()[f'{name[i]}'] = Product(name[i], price[i], desc[i], department[i], img[i])
    name.save()

# users define local/commercial status -
# SV validates if comercial or not (verification badge)

# HOME FILTER
# display by most visited?
# - search how to filter/arrange default/home page to optimise visits & sales
# check com & loc stores
# com/loc tab (based on location):
# - most visited -> popular product (repeat for x number of stores and/or products)


# product carriers (peeks from main inv)
# user: product, qty
# or
# product: user, qty
# or 
# user-product: qty

# vendor table/properties:
# loc/com status
# location
# inventory key
# - vendor-product table


# vendor inventory
# user.inventory
# dep: dairy, 
# name: clover milk
# price: R###
# desc: described
# img: image




for i in range(len(name)):
    print(globals()[f'{name[i]}'])
    print()


# relationship between department + its inventory



























