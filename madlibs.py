#Gongbao Lin

#enter funny verbs and adverbs and nouns and it will make a cool story

#story



import random


def madlib():

    print(" you will be able to enter your own words to make a story out of it")


    VerbBank = ["Advance", "Bolt", "Explode" , "Hurry" , "Slouch" , "Dance" , "Crash" , "Rush"]

    CountryBank = ["Zimbabwe" , "China" , "Vietnam" , "Thailand", " Venezuela" , "Germany", "India" , "Georgia" , "Lithuania"]

    PlaceBank = ["A School" , "The White House" , "The River" , "Chipotle" , "The Beach" , "A Temple" , "The Mountains" , " A library" , "A Daycare"]

    AdjectiveBank = ["awesome", "super", "amazing" , "sublime" , "tricky" , "disasterous" , "crazy"]

    NameBank = ["Bill Gates" , "Albert Einstein" , "Drake ", "Dwayne Johnson" , "Elvis Presley" , "Michael Jordan" , "Justin Bieber", "Abraham Lincoln", "Martin Luther King Jr"]




    decision1 = input("would you like to randomize the country you go to?  : ").lower()

    if decision1 == "yes":
        country = random.choice(CountryBank)


    if decision1 == "no":
        country = input("name any country : ")


    decision2 = input("would you like to randomize somebody who goes with you on this adventure?  : ").lower()

    if decision2 == "yes":
        name = random.choice(NameBank)

    if decision2 == "no":
        name = input("bring somebody with you : ")


    decision3 = input("would you like to randomize a place you go to? : ").lower()

    if decision3 == "yes":
        Place1 = random.choice(PlaceBank)

    if decision3 == "no":
        Place1 = input("put any place : ")


    decision4 = input("would you like to randomize another place you go to? : ").lower()

    if decision4 == "yes":
        Place2 = random.choice(PlaceBank)

    if decision4 == "no":
        Place2 = input("put a second place : ")


    decision5 = input("would you like to randomize the last place you go to? : ").lower()
    if decision5 == "yes":
        Place3 = random.choice(PlaceBank)


    if decision5 == "no":
        Place3 = input("put a third place : ")


    decision6 = input("would you like to randomize your adjectives? : ").lower()
    if decision6 == "yes":
        adjective1 = random.choice(AdjectiveBank).lower()

    if decision6 == "no":
        adjective1 = input("put an adjective : ")

    decision7 = input("would you like to randomize your adjectives? : ").lower()

    if decision7 == "yes":
        adjective2 = random.choice(AdjectiveBank).lower()

    if decision7 == "no":
        adjective2 = input("put a second adjective : ").lower()

    decision8 = input("would you like to randomize your action? : ").lower()

    if decision8 == "yes":
        verb1 = random.choice(VerbBank).lower()

    if decision8 == "no":
        verb1 = input("put a verb : ").lower()

    print(f""" I decided to traverse the Jungle in {country} with my best buddy {name}.
    We plan to first roam around {Place1} and have a {adjective1} time. After that we {verb1}
    to the most beautiful resort,{Place2}. By the time we are finished, we will be {adjective2}
    and rest at {Place3}.
    """)



#Main

madlib()
