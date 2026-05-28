#Gongbao Lin
#Grocery store

items = [
    "Milk", "Eggs", "Bread", "Butter", "Cheese",
    "Chicken Breast", "Ground Beef", "Pork Chops", "Bacon", "Sausage",
    "Pasta", "Rice", "Quinoa", "Cereal", "Oatmeal",
    "Apples", "Bananas", "Oranges", "Strawberries", "Blueberries",
    "Grapes", "Pineapple", "Mangoes", "Lemons", "Limes",
    "Potatoes", "Onions", "Garlic", "Carrots", "Broccoli",
    "Cauliflower", "Spinach", "Kale", "Lettuce", "Bell Peppers",
    "Tomatoes", "Cucumbers", "Zucchini", "Mushrooms", "Avocados",
    "Olive Oil", "Vegetable Oil", "Cooking Spray", "Salt", "Pepper",
    "Sugar", "Brown Sugar", "Flour", "Baking Powder", "Baking Soda",
    "Peanut Butter", "Jelly", "Honey", "Maple Syrup", "Nutella",
    "Coffee", "Tea", "Hot Chocolate", "Creamer", "Sugar Packets",
    "Orange Juice", "Apple Juice", "Soda", "Sparkling Water", "Sports Drink",
    "Chips", "Crackers", "Pretzels", "Popcorn", "Cookies",
    "Ice Cream", "Frozen Pizza", "Frozen Vegetables", "Frozen Chicken Nuggets", "Frozen Waffles",
    "Canned Soup", "Canned Beans", "Canned Corn", "Canned Tomatoes", "Canned Tuna",
    "Ketchup", "Mustard", "Mayonnaise", "BBQ Sauce", "Hot Sauce",
    "Paper Towels", "Toilet Paper", "Facial Tissues", "Dish Soap", "Laundry Detergent"
]



prices = [
    3.49, 2.99, 2.79, 3.99, 4.59,
    7.99, 6.49, 5.99, 4.99, 4.49,
    1.79, 4.29, 5.99, 3.99, 3.49,
    4.49, 1.39, 3.99, 4.99, 5.49,
    5.49, 3.49, 4.99, 1.79, 1.79,
    3.99, 2.49, 1.29, 2.29, 2.99,
    3.49, 3.49, 3.99, 2.49, 3.49,
    2.99, 1.79, 2.49, 2.99, 1.99,
    7.99, 5.49, 3.99, 1.29, 2.49,
    2.49, 2.99, 3.49, 2.49, 1.99,
    3.99, 3.29, 4.99, 6.99, 5.49,
    9.99, 4.49, 3.99, 2.49, 1.99,
    4.29, 3.99, 1.99, 2.49, 2.99,
    3.99, 3.49, 2.99, 2.49, 4.99,
    5.99, 6.49, 2.99, 7.49, 4.99,
    2.79, 1.49, 1.29, 1.79, 2.49,
    2.99, 2.49, 4.49, 3.49, 3.99,
    8.99, 12.99, 3.99, 2.99, 11.99
]



def pricing():

    item = input("what would you like to buy :  ")
    if item in items:

        #find the location of the item then set it find the location of the item equal to the price number by using index?
        #Now we have found price
        #Problem prices.lens isn't working

        prices1 = (items.index(item))

        cost = prices[prices1]

        x = round(cost,2)

        print(f"you're {item} costs {x}")


def discount():

    item = input("what would you like to buy :  ")


    if item in items:

        #find the location of the item then set it find the location of the item equal to the price number by using index?
        #Now we have found price
        #Problem prices.lens isn't working

        prices1 = (items.index(item))

        cost = prices[prices1]

        x = round(cost,2)

        print(f"you're {item} costs {x}")
            #Challenge 2
        #Taking the prices and discounting by 20%
        print("you're lucky, today there is a 20% discount for everything!")
        x = x-(x*.20)

        x = round(x,2)

        print (f"Your {item} is now {x}")


def list():

    money = int(input("how much could you get for "))

    if money >









#Check if the item for price is even in the list

#Challenge 1 : Locating Prices Based off Names
pricing()




#Challenge 2
#Taking the prices and discounting by 20%
discount()

#Challenge 3
#Checking if the given amount has enough for # of items that can be bought for that amount

list()

# money = int(input("what can you buy with ")




