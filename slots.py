#Gongbao Lin and David

#Assignment: Build a 3-Slot Machine in Python



def main_game():


    import random

    bank_account = 0

    while True:


        print(f"your account has {bank_account} credits")

        print("1.) You may deposit money into your account")
        print("2.) You may spend your money on spins")
        print("3.) you may cash out")

        select = input("select 1,2,3 : ")

        if select == '1':
            print("you may only insert 20,50,100 currency")

            addition = int(input("how much money would you like to add? :  "))

            if addition == 20:

                bank_account = bank_account+addition

            elif addition == 50:
                bank_account = bank_account+addition

            elif addition == 100:
                bank_account = bank_account+addition

            else:
                print("please deposit a valid ammount")



        if select == '2':

            if bank_account < 10:
                        print("you don't have enough credits to play")

            if bank_account >= 10:

                        bank_account = bank_account - 10


                        print(f"you now have {bank_account} credits ")


                        #the placeholder is for when I do the wheel[1] for some reason it didnt work until I added the placeholder and didn't let me get a jackpot which kind of ruins the point
                        symbols = ['placeholder','♥', '♦', '♠','7']

                        #gives the chances to get different winnings

                        weights= [0,30,30,25,10]



                        wheel = random.choices(symbols, weights=weights, k=3)

                        #bogus wheel winnings to make me hella money


                        print(f"you have rolled {wheel[0]}, {wheel[1]}, {wheel[2]}")

                        if wheel[0] == wheel[1] == wheel[2]:

                            print(f"you have rolled {wheel[0]}, {wheel[1]}, {wheel[2]}")

                            print("you have won")

                            if wheel[0] == '♥' and wheel [1] == '♥' and wheel [2] == '♥':
                                bank_account = bank_account+25

                                print("you have won 25 credits")


                            if wheel[0] == '♦' and wheel [1] == '♦' and wheel [2] == '♦':
                                bank_account = bank_account+50

                                print("you have won 50 credits")



                            if wheel[0] == '♠' and wheel [1] == '♠' and wheel [2] == '♠':
                                bank_account = bank_account+300
                                print("you have won 300 credits")

                            if wheel[0] == '7' and wheel [1] == '7'  and wheel [2] == '7':
                                bank_account = bank_account+500
                                print("jackpot! you hav won 500 credits")

                        else:
                            print("you have lost")



            else:
                print("please enter a valid response")


            if select == '3':
                    print(f"You have cashed out {bank_account}")
                    break


def testing():

    #1,000*10(the cost of one game) that means this account needs to have 10,000 to spin 1,000 times
    import random

    bank_account = 10000

    house = 0

    print(f"your account has {bank_account} credits")


#my new code: problem is i don't know how to code for net profit

    for i in range(1000):

        print(f"the net profit for the house is {house} ")

        if bank_account < 10:
                    print("you don't have enough credits to play")

        if bank_account >= 10:

                    bank_account = bank_account - 10
                    house = house + 10

                    print(f"you now have {bank_account} credits ")


                    #the placeholder is for when I do the wheel[1] for some reason it didnt work until I added the placeholder and didn't let me get a jackpot which kind of ruins the point
                    symbols = ['placeholder','♥', '♦', '♠','7']

                    #gives the chances to get different winnings

                    weights= [0,30,30,25,10]



                    wheel = random.choices(symbols, weights=weights, k=3)

                    #bogus wheel winnings to make me hella money

                    print(f"you have rolled {wheel[0]}, {wheel[1]}, {wheel[2]}")


                    if wheel[0] == wheel[1] == wheel[2]:

                        print("you have won")

                        if wheel[0] == '♥' and wheel [1] == '♥' and wheel [2] == '♥':
                            bank_account = bank_account+25
                            house = house-15
                            print("you have won 25 credits")


                        if wheel[0] == '♦' and wheel [1] == '♦' and wheel [2] == '♦':
                            bank_account = bank_account+50
                            house = house-40
                            print("you have won 50 credits")



                        if wheel[0] == '♠' and wheel [1] == '♠' and wheel [2] == '♠':
                            bank_account = bank_account+300
                            print("you have won 300 credits")

                            house = house-290

                        if wheel[0] == '7' and wheel [1] == '7'  and wheel [2] == '7':
                            bank_account = bank_account+500
                            print("jackpot! you hav won 500 credits")

                            house = house-490

                    else:
                        print("you have lost")





                #early code


                  # print(f"you have rolled {select} , {select2} , {select3}")



                  # if select == '7' and select2 == '7' and select3 == '7':
                       #print("you have hit jackpot and received 300 credits")
                       #bank_account = bank_account+300



                  # elif select == select2 and select == select3:
                       #print("you have won 100 credits")
                       #bank_account = bank_account+100


                   #else:
                       #print('you have lost')









#main

#main_game()

testing()
