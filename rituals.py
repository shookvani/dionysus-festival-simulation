'''
shivani yashodhara manikandan
shivani.y.manikandan@vanderbilt.edu
last edited april 8, 2025
classics 1010: introduction to mediterraenan studies

rituals.py

this rituals class has been created by me, and me only, in order to compartamentalize various initation and other rites completed by the dionysus cult both in public and during the private parties. this version of the rituals class provides descriptions of the rituals based on the research, and assumed chagnes to the person that completes them dependending on the context. 
'''

import people as pers
import random as rd

def initation(p,people):
    print(f"{p} is not a member of the cult. we are starting the initiation ritual for them.\n\n")
    obj = pers.Person(p)
    people.append(obj)
    randomtask(obj)  

    return people

def bacchantwomenritual(obj):
    print(obj.name+"...parttakes in this ritual invovles dancing in the mountains during the winter. this dance was done to the rythm of aulos and tympanmom (double pipe and hand drum) (brittanica). they would also parttake in the tearing apart and consumption of the raw flesh and blood of animals. this last part is referred to as omophagia (ainsworth, rice & stambaugh). it is told that they would yell the ritual cry \"euoi\" whilst forming thyosi (holy bands) and thyrosi (wands of fennel that are bound with grapevine and them dipped in ivy). they also believed during the ritual that they would be awakened by certain powers (self-freedom / exspression). there is significant debate put out there by scholars about the validity of this ritual and to what extent, especially with the involvment of omophagia and sparagmos. this is especially true when invovling cannabilism.")
    obj.devotion += 4
    obj.action +=1

def sparagmos(obj):
    print(obj.name+"...parttakes in this ritual invovles sacrifice by dismemberment (ainsworth). there is significant debate put out there by scholars about the validity of the involvment of omophagia and sparagmos, especially when it comes to cannabilism.")
    obj.devotion += 2
    obj.action +=1

def wine(obj):
    print(obj.name+"...has a glass of wine/alcohol. dionysus was the god of wine, and this was likely a common practice during all types of festivals")
    obj.wines += 1
    obj.happiness += round(rd.uniform(1.00, 3.99), 2)
    obj.tipsiness += round(rd.uniform(1.00, 1.99), 2)
    obj.ecstasy += 0.1
    obj.devotion += 0.5
    obj.action +=1

def dance(obj):
    print(obj.name+"...conducts a dance or theatrical performance")
    obj.happiness += round(rd.uniform(4.00, 6.99), 2)
    obj.ecstasy += 0.02
    obj.interactions += 2
    obj.devotion += 1
    obj.action +=1

def sacrifice(obj):
    print(obj.name+"...conducts a sacrifice. this is common when worshipping any god in the ancient world.")
    obj.happiness += round(rd.uniform(2.00, 3.99), 2)
    obj.interactions += 1
    obj.devotion += 2
    obj.action +=1

def randomtask(obj):
    obj.ecstasy = 0.0
    counter = rd.randint(1, 5)
    tasks = ["sacrifice", "drink wine", "the bacchant women ritual", "sparagmos"]

    while counter > 0:
        task = tasks[rd.randint(0, len(tasks) - 1)]
        obj.happiness -= round(rd.uniform(0.01, 2.99), 2)
        obj.interactions +=1

        if task == "drink wine":
            wine(obj)
            wine(obj)
            wine(obj)
        elif (task == "the bacchant women ritual"):
            bacchantwomenritual(obj)
        elif (task == "sparagmos"):
            sparagmos(obj)
        elif (task == "sacrifice"):
            sacrifice(obj)

        counter -= 1


def hermaphroditusprank(obj):
    print(obj.name+"...is victim to a prank. statues of the god hermaphroditus were used to play a prank on members. brady-garnand writes, \"The host would boast about their newly acquired marble, ... the group would see the statue from behind, and find the slender figure and ample curves...woman enticing...they would be met with the shocking realization that they had been tricked into lusting after a man...Everyone would have a good laugh, and then return to their festivities.\" this is specifically interesting because hermaphroditus is an important person, and also greek sex culture was very complicated in different ways. you also have roman emperor hadrian who took a same-sex partner named antinous. but here, in this cult, it is simply made all to be a joke — a cult that worships the god of fertility, and where a lot of sex likely happened.")

    obj.happiness += round(rd.uniform(0.01, .99), 2)
    obj.interactions +=3
    obj.action +=1

def hermaphroditusboost(people):
    print("...the god hermaphroditus was very welcome at the dionysus cult \"parties\" as they were nonbinary, and thus is considered the god of effimacy. a devotion boost is applied to all members.")
    for person in people:
        person.happiness += round(rd.uniform(0.01, .99), 2)
        person.ecstasy += 0.05
        person.devotion +=2

def fertility(a,b):
    print(a.name+" and "+b.name+"...have sex. dionysus was the god of fertility, and this was likely a common practice during both the public and private festivals, espcially during the private, mysterious ones")
    a.happiness += round(rd.uniform(5.00, 9.99), 2)
    a.ecstasy += 0.2
    a.interactions += 1
    a.action +=1

    b.happiness += round(rd.uniform(5.00, 9.99), 2)
    b.ecstasy += 0.2
    b.interactions += 1
    b.action +=1
