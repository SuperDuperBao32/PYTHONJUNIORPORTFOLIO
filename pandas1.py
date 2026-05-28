#Gongbao Lin

import pandas as pd

data = pd.read_csv("gamedev.csv")

level = data['Level'].tolist()

time = data['Time'].tolist()

rating = data['Rating'].tolist()

summary = data['Summary'].tolist()

feedback = data['Feedback'].tolist()

filter = []

#print(data.loc[0])

#print a list of rows

#print(data.loc[[0,1,5,7]])

#print a range of rows

#print(data.loc[0 : 25])

#Challenge 1

def problems(score):
    for i in range(len(rating)):
        if score >= rating[i]:
            print(data.loc[i])



def highest():
    print("this is the highest time")
    print(data.loc[77])

def secret():
    print("This is the secret passage")
    print(level[66])
    print(time[66])
    print(summary[66])


problems(3)

highest()

secret()
