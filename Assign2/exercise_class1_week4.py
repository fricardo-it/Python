## Exercise Class 1 Week 4 ##
products = []
total_bill = 0
total_quantity = 0

while True:
    product_name = input("Enter product name (or '0' to exit): ")
    
    if product_name == '0':
        break

    price = float(input("Enter price: "))
    quantity = float(input("Enter quantity: "))

    total_price = price * quantity

    total_bill += total_price
    total_quantity += quantity
    
    product_info = {"Name": product_name, "Price": price, "Quantity": quantity, "Total Price": total_price}
    products.append(product_info)

lowest_price_index = 0
highest_price_index = 0

for i in range(1, len(products)):
    if products[i]["Price"] < products[lowest_price_index]["Price"]:
        lowest_price_index = i
    if products[i]["Price"] > products[highest_price_index]["Price"]:
        highest_price_index = i

lowest_product = products[lowest_price_index]
highest_product = products[highest_price_index]

print("\nLowest Product:")
print("Name: {}, Price: {:.2f}".format(lowest_product["Name"], lowest_product["Price"]))

print("\nMost Expensive Product:")
print("Name: {}, Price: {:.2f}".format(highest_product["Name"], highest_product["Price"]))

average_price = total_price / total_quantity

print("\nAverage Price: {:.2f}".format(average_price))

print("\nList of Products:")
for product in products:
    print("Name: {p_name}, Price: {p_price}, Quantity: {p_qty}, Total Price: {t_price}".format(p_name=product["Name"],p_price=product["Price"],p_qty=product["Quantity"],t_price=product["Total Price"]))

print("\nTotal Amount Paid: {:.2f}".format(total_price))

