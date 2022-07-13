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


def get_group(size: int):
    group = []
    for i in range(size):
        group.append(Person(i))
    return group


def print_group(group: list):
    for i in group:
        print(i)


def top_total(group: list, top: int):
    totals = []
    for i in group:
        totals.append(i.total)
    highest_totals = (heapq.nlargest(top, totals))
    final_list = []
    for total in highest_totals:
        for i in group:
            if i.total == total:
                final_list.append(i)
    return final_list


def top_skill(group: list, top: int):
    skills = []
    for i in group:
        skills.append(i.skill)
    highest_skill = (heapq.nlargest(top, skills))
    final_list = []
    for skill in highest_skill:
        for i in group:
            if i.skill == skill:
                final_list.append(i)
    return final_list


def top_luck(group: list, top: int):
    lucks = []
    for i in group:
        lucks.append(i.luck)
    highest_luck = (heapq.nlargest(top, lucks))
    final_list = []
    for luck in highest_luck:
        for i in group:
            if i.luck == luck:
                final_list.append(i)
    return final_list


def average_totals(group: list):
    totals = []
    for i in group:
        totals.append(i.total)
    return sum(totals)/len(totals)


def average_skills(group: list):
    skills = []
    for i in group:
        skills.append(i.skill)
    return sum(skills)/len(skills)


def average_lucks(group: list):
    lucks = []
    for i in group:
        lucks.append(i.luck)
    return sum(lucks)/len(lucks)

# group = get_group(100)

# print_group(group)
# print("\n")

# top_totals = top_total(group, 10)
# top_skills = top_skill(group, 10)
# top_lucks = top_luck(group, 10)

# print("People with the highest total (skill + luck)")
# print_group(top_totals)

# print("\n")


# print("People with the highest skill")
# print_group(top_skills)

# print("\n")

# print("People with the highest luck")
# print_group(top_lucks)
