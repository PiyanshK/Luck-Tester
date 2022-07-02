import luck


# Create 100 classes
groups = []
for i in range(100):
    groups.append(luck.get_group(100))

# print data
# for i in groups:
#     print("new class #{}".format(groups.index(i)))
#     for person in i:
#         print(person)

# analyze data
best_totals = []
best_skills = []
best_lucks = []

for group in groups:
    best_total = luck.top_total(group, 10)
    best_totals.append(best_total)
    best_skill = luck.top_skill(group, 10)
    best_skills.append(best_skill)
    best_luck = luck.top_luck(group, 10)
    best_lucks.append(best_luck)
