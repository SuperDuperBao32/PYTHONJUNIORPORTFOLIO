

#initialize

#Happiness
#Hunger
#Mood


happiness = 50
hunger = 50
energy = 50




#you’ll be receiving cash from your job because you’re a retired military veteran
money = 100


# for holding future foods that you’ll get from the grocery shop
inventory = []

day = 1

#items from market
items = ["milk","chocolate","dogfood","a5wagyu","peanutbutter","eggs"]

#storyline: Your the owner of a Shiba Inu named Bruford, take care of him at all cost or else.. DEATH!

#Function


#feeding bruford
def feed(item):
    global hunger, happiness, energy, inventory

    for food in inventory:
        if food == item:
            inventory.remove(food)

            if item == "milk":
                print("Bruford drinks the milk")
                hunger += 10
                happiness += 5

            elif item == "dogfood":
                print("Bruford eats the dogfood")
                hunger += 20
                happiness -= 5

            elif item == "a5wagyu":
                print("Bruford loves it")
                hunger += 30
                happiness += 20

            elif item == "peanutbutter":
                print("Bruford loves peanut butter")
                hunger += 15
                happiness += 15

            elif item == "eggs":
                print("Bruford eats the eggs")
                hunger += 12
                energy += 5

            elif item == "chocolate":
                print("Bruford dies")
                hunger = 0
                happiness = 0
                energy = 0

            return hunger, happiness, energy

    print("That item is not in your inventory")
    return hunger, happiness, energy
def game():
    global happiness, hunger, energy, money, inventory, day
    print('Welcome to Take Care Of Bruford')
    print('This game is made to entertain for my create project')
    print("You're goal is to make it to day 30 without having Bruford die, but for this demo, it'll be 10 days to minimize the time of the game")
    print("Be careful of each move, each move costs a day, and everyday Bruford's stats lower")
    while True:

        print("Bruford's current stats")
        print(f"{happiness}, happiness")
        print(f"{hunger}, hunger")
        print(f"{energy}, energy")



    #took design inspiration from https://www.youtube.com/watch?v=21-CwgU68V0
    #when creating menu and added 'print' to print the list of things that you can do for the menu
    #added custom menu design with ......menu.......

        print('.........................menu.........................')
        print(f'It is day {day} of taking care of Bruford')
        print('1.Feed')
        print('2.Sleep')
        print('3.Play with')
        print('4.Shop')
        print('5.Show your money')
        print('......................................................')


    #Debugging help and coding tutorial from https://docs.python.org/3/tutorial/errors.html
    #Learned how to use "Value Error" and try and except in order to fix typing errors, lists asking for 'integer' but breaking
    #when entering a letter rather than an integer
        try:
            choice = int(input('enter:'))

        except ValueError:
            print('enter a valid answer')
            continue

        #choice implement feeding system

        if choice == 1:

            if len(inventory)== 0 : #checks for food if you dont have food tells you to buy some food
                print('You have no food, buy some at the market')

            else:
                print(inventory)
                item = input('which would you like to feed Bruford? : ')

                if item in inventory:
                    feed(item)

                else:
                    print('item is not in inventory')


        if choice == 2: #takes away hunger but gives energy
            print('Bruford sleeps and gains 20 energy points, but loses 10 hunger')
            energy += 20
            hunger -= 10

        if choice == 3: #takes away hunger and energy but gives big happiness

            print("Bruford's happiness has increased by 20, but his energy has lowered by 15")
            happiness += 15
            energy -= 15

        #shopping system using the money
        if choice ==4:
            print('what would you like to buy? ')

            print('1.milk 2.50$')
            print('2.chocolate #do not feed this to your dog 100$')
            print('3.dogfood 1.50$')
            print('4.a5wagyu 50$')
            print('5.peanutbutter 10$')
            print('6.eggs 5$')


    #Debugging help and coding tutorial from https://docs.python.org/3/tutorial/errors.html
    #Learned how to use "Value Error" and try and except in order to fix typing errors, lists asking for 'integer' but breaking
    #when entering a letter rather than an integer
            try:
                choice2 = int(input('what would you like to buy? : '))

            except ValueError:
                print("error try again")
                continue

            if choice2 == 1:
                money = money-2.50
                inventory.append(items[0])
                print(f"you have bought {items[0]}")

            elif choice2 == 2:
                money = money-100
                inventory.append(items[1])
                print(f"you have bought {items[1]}")

            elif choice2 == 3:
                money = money - 1.50
                inventory.append(items[2])
                print(f"you have bought {items[2]}")

            elif choice2 == 4:
                money = money - 50
                inventory.append(items[3])
                print(f"you have bought {items[3]}")


            elif choice2 == 5:
                money = money - 10
                inventory.append(items[4])
                print(f"you have bought {items[4]}")

            elif choice2 == 6:
                money = money-5
                inventory.append(items[5])
                print(f"you have bought {items[5]}")

            else:
                print('please type a number or a valid response')

        if choice == 5:
            print(f'{money} dollars')


        #payout5

        if day % 5 ==0:
            money += 25
            print('You get paid 25 dollars from retirement')


        #daily bruford feed

        hunger -=5
        happiness-=3
        energy -=3


        #death of bruford
        if hunger <= 0 or happiness <= 0 or energy <= 0:
            print("Bruford has died")
            break

        if day >= 10:
            print('you have beat the game')
            break


        day += 1

#main
game()
