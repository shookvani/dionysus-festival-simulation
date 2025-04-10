'''
shivani yashodhara manikandan
shivani.y.manikandan@vanderbilt.edu
last edited april 6, 2025
classics 1010: introduction to mediterraenan studies

people.py

this person class has been created by me, and me only, in ordr to utilize a person object type to manipulate when completing rituals. the person has various attributes.
'''
import random as rd

class Person:
    def __init__(self, name):
        self.name = name
        self.happiness = round(rd.uniform(0.01, 99.99), 2)
        self.tipsiness = 0
        self.wines = 0
        self.devotion = 3
        self.interactions = 0
        self.ecstasy = 0.0
        self.action = 0

        if self.happiness >= 80.0:
            self.ecstasy = round(rd.uniform(1.0, 10.0), 2)

    def printer(self):
        self.data()
        print(f"{self.name} has made {self.interactions} interaction(s), "
              f"completed {self.action} action(s), "
              f"and specifically drunk {self.wines} glass(es) of wine. Their tipsiness score is {self.tipsiness}. "
              f"Their resulting happiness score is {self.happiness} and ecstasy score is {self.ecstasy}.")
        
    def data(self):
        self.happiness = round(self.happiness, 2)
        self.ecstasy = round(self.ecstasy, 2)
        self.tipsiness = round(self.tipsiness, 2)