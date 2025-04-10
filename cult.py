'''
shivani yashodhara manikandan
shivani.y.manikandan@vanderbilt.edu
last edited april 8, 2025
classics 1010: introduction to mediterraenan studies

cult.py

this cult class has been created by me, and me only, in order to utilize to put the moving parts of the simulation class as well as handle the user input (either manual or through text processing and text files) in order to run the simulation any n number of times
'''

import people as pers
import simulation as sim

def generator(num):
    people = []
    existing_names = set()
    
    for _ in range(num):
        while True:
            name = input("Enter a name: ").upper()
            if name in existing_names:
                print("This name is already taken. Please enter a different name.")
            else:
                existing_names.add(name)
                obj = pers.Person(name)
                people.append(obj)
                break  

    return people

def generatorfile(infile):
   people = []
   existing_names = set()
   
   with open(infile, 'r') as f:
    for line in f:
        name = line.strip().upper()
        if name not in existing_names:
            existing_names.add(name)
            obj = pers.Person(name)
            people.append(obj)
           
    return people


def main():
    print("the cult festival includes masked dances with low inhibitions, as well as various rituals and other practiceis. research suggests that this may be a result of the need for self expression, maybe because of low alcoholic content and not as much need for sexual desire (ainsworth)")

    if ( input("welcome to my modeling of the dinoysus cult. this was a mysterious cult and even today, not much is known about it. this is a way to simulate / provide some of the knowledge on the rituals. please note that this model includes themes of cannabilism, sex-based topics and rituals, and more. \n \nto start the simulation, please hit any key except 'e'. if you would like to input your own people list manually / by file, please it the 'e' key \n").upper() == 'E'):
        if (input("do you want to input manually? type y if yes, anything else for no: ").upper() == 'Y'):
            people = generator(int(input("\nenter number of current members: ")))
            sim.party(people)
        else:
            people = generatorfile(input("enter txt file name: "))
            sim.party(people)
    else:
        people = generatorfile("default.txt")
        sim.party(people)