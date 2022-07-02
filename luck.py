import random
import heapq


class Person:
    def __init__(self, id):

        self.id = id
        self.luck = random.randint(0, 500)/10
        self.skill = random.randint(8000, 9500)/10
        self. total = self.luck + self.skill

    def __str__(self):
        return "Person: {}, Luck: {}, Skill: {}, Total: {}".format(self.id, self.luck, self.skill, self.total)


def get_group(size):
    group = []
    for i in range(size):
        group.append(Person(i))
    return group


def print_group(group):
    for i in group:
        print(i)


def top_total(group, top):
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


def top_skill(group, top):
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


def top_luck(group, top):
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

group = get_group(100)

print_group(group)
print("\n")

top_totals = top_total(group, 10)
top_skills = top_skill(group, 10)
top_lucks = top_luck(group, 10)

print("People with the highest total (skill + luck)")
for i in top_totals:
    print(i)

print("\n")


print("People with the highest skill")
for i in top_skills:
    print(i)

print("\n")

print("People with the highest luck")
for i in top_lucks:
    print(i)