import json
all_products = {}


def retrieve_all_products():
    with open(r"C:\Users\user\Desktop\DI\week11\products.json", mode='r') as f:
        all_products = json.load(f)
        print(all_products)
        return all_products


def retrieve_requested_product(product):
    all_products = retrieve_all_products()
    for pro in all_products:
        if product == pro["ProductId"]:
            requested_product = product
            print(requested_product)
            return requested_product


retrieve_all_products()
retrieve_requested_product("HT-1000")