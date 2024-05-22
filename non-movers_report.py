import csv
with open("sales_data.csv", errors="ignore", newline='') as sales_csv, open("product-export.csv", errors="ignore", newline='') as products_csv:

    
    sales_reader = csv.DictReader(sales_csv)
    products_reader = csv.DictReader(products_csv)
    
    #parse products csv
    products_sku_list = list()
    for product in products_reader:
        products_sku_list.append(product["sku"])
    
    #parse sales csv
    sales_sku_list = list()
    for product in sales_reader:
        sales_sku_list.append(product["SKU"])

    non_movers_sku_list = [sku for sku in products_sku_list if sku not in sales_sku_list]

with open("product-export.csv", errors="ignore", newline='') as products_csv, open("non_movers.csv", "w", newline='') as non_movers_csv:
    products_reader = csv.DictReader(products_csv)
    field_names = products_reader.fieldnames
    non_movers_writer = csv.DictWriter(non_movers_csv, fieldnames=field_names)
    non_movers_writer.writeheader()

    for product in products_reader:
        if product["sku"] in non_movers_sku_list:
            non_movers_writer.writerow(product)
