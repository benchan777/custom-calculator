print("Tera plate crafting and price calculator")
#This while loop checks if the user has entered one of the two options. If not, the user is prompted to enter only siglo or plate.
while True:
    item_type = input("Would you like to craft a siglo or plate? ")
    if item_type == "siglo":
        break
    elif item_type == "plate":
        break
    else:
        print("Please enter siglo or plate.")
#This while loop checks to see if the user entered a number. If not, the user is prompted to enter a number.
while True:
    try:
        amount_of_item = int(input(f"Enter number of {item_type}s you would like to craft: ")) #convert the number which was converted into a string by input() back into an integer
        break
    except ValueError: #asks user to enter a number if they enter something that is unable to be converted into an integer
        print("Please enter a number.")
#This while loop checks to see if the user entered a number. If not, the user is prompted to enter a number.
while True:
    try:
        base_item_price = int(input("Enter the price of each silver talent: ")) #convert the number which was converted into a string by input() back into an integer
        break
    except ValueError:
        print("Please enter a number.") #asks user to enter a number if they enter something that is unable to be converted into an integer
siglo_craft_count = (amount_of_item / 3)
number_of_kits = (siglo_craft_count * 60)
plate_craft_count = (amount_of_item / 3)
if item_type == "siglo":
    number_of_talents = (siglo_craft_count * 5)
    total_cost = (number_of_talents * base_item_price + number_of_kits)
    print(f"You will need {round(number_of_talents)} talents and {number_of_kits} kits. It will cost you {round(total_cost)} gold.")
elif item_type == "plate":
    siglo_craft_count_1 = (siglo_craft_count * 5)
    siglo_craft_count_2 = (siglo_craft_count_1 / 3)
    number_of_talents = (siglo_craft_count_2 * 5)
    number_of_plate_kits = (plate_craft_count * 240)
    talent_cost = (base_item_price * number_of_talents)
    kit_cost = (number_of_plate_kits + number_of_kits)
    total_cost = (talent_cost + kit_cost)
    print(f"You will need {round(number_of_talents)} talents and {number_of_plate_kits + number_of_kits} kits. It will cost you {round(total_cost)} gold.")
else:
    print("what")