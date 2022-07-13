import luck

# analyze data

def get_averages(group : int):
    return [luck.average_totals(group), luck.average_skills(group), luck.average_lucks(group)]

# def print_top_averages(group):
#     print("\n")
#     print("Average total: {}".format(luck.average_totals(group)))
#     print("Average skill: {}".format(luck.average_skills(group)))
#     print("Average luck: {}".format(luck.average_lucks(group)))
#     print("\n")


def groups_with_statistics(numgroups: int, groupsize: int, top: int):
    groups = []
    for i in range(numgroups):
        groups.append(luck.get_group(groupsize))
    best_totals = []
    best_skills = []
    best_lucks = []
    for group in groups:
        best_total = luck.top_total(group, top)
        best_totals.append(best_total)
        best_skill = luck.top_skill(group, top)
        best_skills.append(best_skill)
        best_luck = luck.top_luck(group, top)
        best_lucks.append(best_luck)
    
    statistics = []
    for (group, best_skill, best_luck, best_total) in zip(groups, best_skills, best_lucks, best_totals):
        statistics.append([(group, get_averages(group)), (best_total, get_averages(best_total)), (best_skill, get_averages(best_skill)), (best_luck, get_averages(best_luck))])
        
    # for (best_skill, best_total, best_luck) in zip(best_skills, best_totals, best_lucks):
    #     group = groups[best_skills.index(best_skill)]
    #     print("class #{}".format(str(int(groups.index(group)) + 1)))
    #     print("\n")

    #     luck.print_group(group)
    #     print("\n")

    #     print("best total:")
    #     print("\n")
    #     luck.print_group(best_total)
    #     print("\n")
    #     # averages from group with best totals
    #     print_top_averages(best_total)

    #     print("best skill:")
    #     print("\n")
    #     luck.print_group(best_skill)
    #     print("\n")
    #     # averages from group with best skills
    #     print_top_averages(best_skill)

    #     print("best luck:")
    #     print("\n")
    #     luck.print_group(best_luck)
    #     print("\n")
    #     # averages from group with best luck
    #     print_top_averages(best_luck)

groups_with_statistics(2, 20, 5)