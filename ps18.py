#gongbao lin
#problem set 18


import random

finish = 50


tortoise_w = 0

hare_w = 0

snail_w = 0

#challenge 2

for i in range(100000):

    tortoise = 0

    hare = 0

    snail = 0

    #the race
    while tortoise < finish and hare < finish and snail < finish:
        #constant move (turtle)


        tortoise_p = random.randint(1,3)

        tortoise += tortoise_p

        #sleeps 30% chance to sleep
        #challenge 3 should replace the chances --- > 0.6925 or 69.25% chance for the hare to sleep in order for tortoise to win 95% or above
        #extra credit what rate should it be
        #random.random function from https://docs.python.org/3/library/random.html : taught me that random.random goes through values up to 1.0 which I
        #use to emulate percentages by using decimals

        #hare
        if random.random() < 0.30:
            #hare sleeps
            pass

        else:
            hare_p = random.randint(1,5)
            hare += hare_p





        #every 10% snail section
        if random.random() < 0.10:
            #snail hitches a ride code

            snail = hare

        else:
            snail += 2

        #got rid of tracking steps to declutter amounts of messages for challenge 2: 100,000 loops
        #print (f"Tortoise : {tortoise}, Hare: {hare}")

#keeps track of victories
    if tortoise >= finish:
        print("Tortoise wins")
        tortoise_w += 1

    elif snail >= finish:
        print("Snail wins")
        snail_w += 1

    else:
        print("Hare wins")

        hare_w += 1

    print (f'Tortoise {tortoise_w}')
    print (f'Hare {hare_w}')
    print (f'Snail {snail_w}')

#challenge 2 results : slow and steady does NOT win all, tortoise : 22k times won hare : 78 k won
