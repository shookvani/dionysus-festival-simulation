'''
shivani yashodhara manikandan
shivani.y.manikandan@vanderbilt.edu
last edited april 8, 2025
classics 1010: introduction to mediterraenan studies

simulation.py

this simulation class has been created by me, and me only, in order to utilize to put the moving parts of a single person or multiple people in a given cult. this allows them to randomly complete tasks/rite, get checked on the guest list, and start the initation process if necessary. there is also a way to see average attributes per person per simulation trial and per person across all trials.
'''

import rituals as rit
import random as rd

def guestlist(people):
    for person in people:
        person.printer()

def checklist(people_list):
    p = input("\nThe Dionysus cult is a mysterious cult. Please enter the name that you would like to check the membership of: ").upper()
    
    for person in people_list:
        if person.name == p:
            print("this person is a member, continuing with party")
            return True
    
    return p

def statistics(li,total):
    happy = 0
    wine = 0
    ecstasy = 0
    interactions = 0
    action = 0
    devotion = 0
    counter = 0
    
    for person in li:
        happy += person.happiness
        wine += person.wines
        ecstasy += person.ecstasy
        interactions += person.interactions
        action += person.action
        devotion += person.devotion
        counter += 1

    print(f"""
        \n\nAverage Results (per simulation, adjusted by total participants):
        - Happiness: {round(happy / counter, 2) / total}
        - Interactions: {round(interactions / counter, 2) / total}
        - Actions: {round(action / counter, 2) / total}
        - Devotion: {round(devotion / counter, 2) / total}
        - Wine: {round(wine / counter, 2) / total}
        - ecstasy: {round(ecstasy / counter, 2) / total}
    """)

    print(f"""
        \nAverage Results (per participant):
        - Happiness: {round(happy / counter, 2)}
        - Interactions: {round(interactions / counter, 2)}
        - Actions: {round(action / counter, 2)}
        - Devotion: {round(devotion / counter, 2)}
        - Wine: {round(wine / counter, 2)}
        - ecstasy: {round(ecstasy / counter, 2)}
    """)
    
def simulate(z, li):
    for i in range(z): 
        r = rd.randint(0,5)
        if (r==0):
            rit.dance(li[rd.randint(0, len(li) - 1)])
        elif (r==1):
            rit.wine(li[rd.randint(0, len(li) - 1)])
        elif (r==2):
            rit.sacrifice(li[rd.randint(0, len(li) - 1)])
        elif (r==3):
            rit.hermaphroditusboost(li)
        elif (r==4):
            rit.hermaphroditusprank(li[rd.randint(0, len(li) - 1)])
        elif (r==5):
            a = li[rd.randint(0, len(li) - 1)]
            b = li[rd.randint(0, len(li) - 1)]
            if (a!= b):
                rit.fertility(a,b)

def party(people):
    li = people
    guestlist(li)
    inprog = True
    switcher = False
    simulationcount = 0

    while inprog:
        if (input("type y if you need to check a membership: ").upper() == 'Y'):
            x = checklist(li)
            if (x != True):
                name = input("confirm the name of the person to initiate: ").upper()
                confirm = False
                while(confirm == False):
                    if (name != x):
                        name = input("confirm the name of the person to initiate: ").upper()
                    elif (name == x):
                        li = rit.initation(name, li)
                        confirm = True
        
        if switcher:
            choice = input("Do you want to automate 1000 simulations? If so, type 'y': ").upper()
            
            if choice == 'Y':
                simulate(1000, li)
                simulationcount += 1000
            else:
                z = rd.randint(4, 10)
                simulate(z, li)
                simulationcount += z

            if input("\nDo you want to end the party? (y for yes, anything else to continue) ").upper() == 'Y':
                inprog = False

        switcher = True

    print("\n\n\n")
    guestlist(li)
    statistics(li, simulationcount)
    print("\nTotal simulations: " + str(simulationcount))
