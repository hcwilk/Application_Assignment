import math
import pandas as pd

#moved the file into the same directory in order to avoid the path stuff here
df = pd.read_csv("data.csv")

#gets the distance from origin to circular part of arc
def radius(x,y):
    return math.sqrt(x**2 + y**2)

#determines what location the shot was taken from
def location(x,y):
    if (abs(x)>22.0 and abs(y)<7.8):
        return 1
    elif radius(x,y)>23.75:
        return 2
    else:
        return 0

Team_A_2A, Team_A_2M, Team_A_C3A, Team_A_C3M, Team_A_3A, Team_A_3M = 0,0,0,0,0,0
Team_B_2A, Team_B_2M, Team_B_C3A, Team_B_C3M, Team_B_3A, Team_B_3M = 0,0,0,0,0,0

for index, row in df.iterrows():
    x = float(row['x'])
    y = float(row['y'])
    m = int(row['fgmade'])
    if row['team']=='Team A':
        if location(x,y)==1:
            if m==1:
                Team_A_C3M+=1
            Team_A_C3A+=1
        elif location(x,y)==2:
            if m==1:
                Team_A_3M+=1
            Team_A_3A+=1
        else:
            if m==1:
                Team_A_2M+=1
            Team_A_2A+=1
    else:
        if location(x,y)==1:
            if m==1:
                Team_B_C3M+=1
            Team_B_C3A+=1
        elif location(x,y)==2:
            if m==1:
                Team_B_3M+=1
            Team_B_3A+=1
        else:
            if m==1:
                Team_B_2M+=1
            Team_B_2A+=1


def E(a,m,th):
    return (m +(.5*th))/a

a = [Team_A_2A, Team_A_2M, Team_A_C3A, Team_A_C3M, Team_A_3A, Team_A_3M]
b = [Team_B_2A, Team_B_2M, Team_B_C3A, Team_B_C3M, Team_B_3A, Team_B_3M]
total_A = Team_A_2A+Team_A_3A+Team_A_C3A
total_B = Team_B_2A+Team_B_3A+Team_B_C3A


#just to cut down on formatting
stri = ["2PT","C3", "NC3"]

for i in range(3):
    print("The % of shots taken in the "+ stri[i]+" zone for Team A is " + str((a[2*i]/total_A))+"%")
    print("The % of shots taken in the "+ stri[i]+" zone for Team B is " + str((b[2 * i] / total_B)) + "%")


print("The effective field goal percentage for Team A with 2PT shots is "+ str(E(Team_A_2A,Team_A_2M,0)) + "%")
print("The effective field goal percentage for Team A with 3PT Corner shots is "+ str(E(Team_A_C3A,Team_A_C3M,Team_A_C3M)) + "%")
print("The effective field goal percentage for Team A with 3PT non-corner is "+ str(E(Team_A_3A,Team_A_3M,Team_A_3M)) + "%")

print("The effective field goal percentage for Team B with 2PT shots is "+ str(E(Team_B_2A,Team_B_2M,0)) + "%")
print("The effective field goal percentage for Team B with 3PT Corner shots is "+ str(E(Team_B_C3A,Team_B_C3M,Team_B_C3M)) + "%")
print("The effective field goal percentage for Team B with 3PT non-corner is "+ str(E(Team_B_3A,Team_B_3M,Team_B_3M)) + "%")
