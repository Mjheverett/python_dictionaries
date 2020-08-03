menu = {
    "Brunch" : {
        "Steak and Eggs": 16.99, 
        "Three Egg Breakfast": 8.99, 
        "Egg Benedict": 11.99, 
        "Biscuits and Gravy": 7.99, 
        "Chicken Fingers": 10.99, 
        "Chicken Wrap": 8.99, 
        "Steak Salad" : 1.99
    },
    "Drinks": {
        "Soft Drink": 1.99, 
        "Coffee": 1.99, 
        "Orange Juice": 0.99, 
        "Milk": 0.55, 
        "Water": 0.00
    } 
}

# 1. Fix the price of the steak salad. It should be 15.99
menu["Brunch"]["Steak Salad"] = 15.99
#print(menu)
# 2. Add a specials menu that includes: Soup of the Day (8.99), Catch of the Day (14.99), Chef Special (15.99) 
menu["Specials"] = {
    "Soup of the Day": 8.99,
    "Catch of the Day": 14.99,
    "Chef Special": 15.99
}
#print(menu)
# 3. Change "Three Egg Breakfast" to have the options of: Without Bacon (8.99) and With Bacon (9.99)
menu["Brunch"]["Three Egg Breakfast"] = {
    "Without Bacon": 8.99,
    "With Bacon": 9.99
}
# print(menu)

# For each table you will need to print a reciept for the requested items 
# Assume all tables will have one payer
# On the 'receipt' you will need to:
#   print out each menu item order and the price of the item calculate the total for their bill
#   calculate the sales tax (7%)
#   print out suggested tips (25%, 20%, 15%)
#   calculate total bill with sales tax included 
# TABLE 1:
#   Guest 1: Egg Benedict, Coffee
#   Guest 2: Biscuit and Gravy, Coffee 
#   Guest 3: Steak and Eggs, Soft Drink
# TABLE 2:
#   Guest 1: Steak Salad, Soft Drink
#   Guest 2: Soup of the Day, Chicken Wrap, Water 
#   Guest 3: Chicken Fingers, Soft Drink
#   For the Table: Chef Special

#Table_1 = (menu["Brunch"]["Egg Benedict"],menu["Drinks"]["Coffee"],menu["Brunch"]["Biscuits and Gravy"],menu["Drinks"]["Coffee"],menu["Brunch"]["Steak and Eggs"],menu["Drinks"]["Soft Drink"])
Table_1 = (
    "Egg Benedict",
    "Coffee",
    "Biscuits and Gravy",
    "Coffee",
    "Steak and Eggs",
    "Soft Drink"
)

# Table_2 = (menu["Brunch"]["Steak Salad"],menu["Drinks"]["Soft Drink"],menu["Specials"]["Soup of the Day"],menu["Brunch"]["Chicken Wrap"],menu["Drinks"]["Water"],menu["Brunch"]["Chicken Fingers"],menu["Drinks"]["Soft Drink"],menu["Specials"]["Chef Special"])
Table_2 = {
    "Guest1": {
        "Steak Salad",
        "Soft Drink"
    },
    "Guest2": {
        "Soup of the Day",
        "Chicken Wrap",
        "Water"
    },
    "Guest3": {
        "Chicken Fingers",
        "Soft Drink"
    },
    "FortheTable": {
        "Chef Special"
    }
}
price_table_1 = 0
price_table_2 = 0

for items in Table_1:
    if items in menu["Brunch"]:
        print(items)
        price_table_1 += menu["Brunch"][items]
    elif items in menu["Drinks"]:
        print(items)
        price_table_1 += menu["Drinks"][items]
    elif items in menu["Specials"]:
        print(items)
        price_table_1 += menu["Specials"][items]

taxes_table_1 = price_table_1 * 0.08
total_table_1 = price_table_1 + taxes_table_1

for items in Table_2:
    if items in menu["Brunch"]:
        print(items)
        price_table_2 += menu["Brunch"][items]
    elif items in menu["Drinks"]:
        print(items)
        price_table_2 += menu["Drinks"][items]
    elif items in menu["Specials"]:
        print(items)
        price_table_2 += menu["Specials"][items]

taxes_table_2 = price_table_2 * 0.08
total_table_2 = price_table_2 + taxes_table_2
# print("%.2f %.2f %.2f %.2f %.2f %.2f" % (price_table_1, taxes_table_1, total_table_1, price_table_1 * .25, price_table_1 * .20, price_table_1 * .15))
# print("%.2f %.2f %.2f %.2f %.2f %.2f" % (price_table_2, taxes_table_2, total_table_2, price_table_2 * .25, price_table_2 * .20, price_table_2 * .15))

# for items in Table_1:
#     print("%s " % (items))

# testing out that wakatime is actually working by pretending to do some good ole coding.