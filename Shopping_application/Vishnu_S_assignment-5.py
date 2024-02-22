inventory = {}

def load_inventory():
    try:
        with open('inventory.text','r')as file:
            for line in file:
                product_id,product_name,category,price,quantity = list.strip().split(',')
                inventory[product_id] ={
                    'name':product_name,
                    'category':category,
                    'price':float(price),
                    'quantity':int(quantity)
                }
        print("Inventory loaded successfully")
    except:
        print("No inventory file found")


def display_menu():
    print("\nMenu")
    print("1. Add Product")
    print("2.Update Product Information")
    print("3. Display Inventory")
    print("4. Exit")

def add_product():
    product_id = input("Enter Product ID:")
    if product_id in inventory:
        print("Product ID already exists. Please enter a unique ID.")
        return
    
    product_name = input("Enter Product Name:")
    category = input("Enter Category:")
    price = input("Enter Price:")
    quantity = input("Enter Quantity:")
    
    inventory[product_id] ={
        'name':product_name,
        'category':category,
        'price':price,
        'quantity':quantity
    }
    print("Product added successfully")

def save_inventory():
    with open('inventory.txt', 'w') as file:
        for product_id, product in inventory.items():
            file.write(f"{product_id},{product['name']},{product['category']},{product['price']},{product['quantity']}\n")
    print("Inventory saved successfully.")

def update_product():
    product_id = input("Enter Product ID to update:")
    if product_id in inventory:
        print("1. Update Product Name")
        print("2. Update Category")
        print("3. Update Price")
        print("4. Update Quantity")
        choice = input("Enter your choice:")
        if choice == '1':
            inventory[product_id]['name'] = input("Enter new Product Name:")
        elif choice == '2':
            inventory[product_id]['category'] = input("Enter new Category:")
        elif choice == '3':
            inventory[product_id]['price'] = input("Enter new Price:")
        elif choice == '4':
            inventory[product_id]['quantity'] = input("Enter new Quantity:")
        else:
            print("Invalid Choice")
        print("Product updated successfully")
    else:
        print("Product not found")

def display_inventory():
    print("\nInventory:")
    print("Product ID\tProduct Name\tCategory\tPrice\tQuantity")
    for product_id,product in inventory.items():
        print(f"{product_id}\t\t{product['name']}\t\t{product['category']}\t\t{product['price']}\t\t{product['quantity']}")


def main():
    load_inventory()
    while True:
        display_menu()
        choice = input("Enter your choice:")
        if choice == '1':
            add_product()
        if choice == '2':
            update_product()
        if choice == '3':
            display_inventory()
        if choice == '4':
            save_inventory()
            print("Exiting.")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()