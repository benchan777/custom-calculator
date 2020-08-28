print("Tera plate crafting and price calculator")
while True:
    item_type = input("Would you like to craft a siglo or plate? ")
    if item_type == "siglo":
        break
    elif item_type == "plate":
        break
    else:
        print("Please enter siglo or plate.")
while True:
    try:
        amount_of_item = int(input(f"Enter number of {item_type}s you would like to craft: "))
        break
    except ValueError:
        print("Please enter a number.")
base_item_price = input("Enter the price of each silver talent: ")


