import random
import heapq

class Person:
    def __init__(self, id):

        self.id = id
        self.luck = random.randint(0, 50)/10
        self.skill = random.randint(800, 950)/10
        self. total = self.luck + self.skill

    
    def __str__(self):
        return "Person: {}, Luck: {}, Skill: {}, Total: {}".format(self.id, self.luck, self.skill, self.total)

def get_class(size):
    class_list = []
    for i in range(size):
        class_list.append(Person(i))
    return class_list


def print_class(class_list):
    for i in class_list:
        print(i)

def top_total(class_list):
    totals = []
    for i in class_list:
        totals.append(i.total)
    highest_totals = (heapq.nlargest(10, totals))
    final_list = []
    for total in highest_totals:
        for i in class_list:
            if i.total == total:
                final_list.append(i)
    return final_list
                

def top_skill(class_list):
    skills = []
    for i in class_list:
        skills.append(i.skill)
    highest_skill = (heapq.nlargest(10, skills))
    final_list = []
    for skill in highest_skill:
        for i in class_list:
            if i.skill == skill:
                final_list.append(i)
    return final_list

class_list = get_class(100)

print_class(class_list)
print("\n")

top_totals = top_total(class_list)
top_skills = top_skill(class_list)

print("People with the highest total (skill + luck)")
for i in top_totals:
    print(i)

print("\n")


print("People with the highest skill")
for i in top_skills:
    print(i)

