from collections import Counter
def finding(list1, list2):
    sol_arr = []
    for item in list1:
        if item in list2:
            sol_arr.append(item)
    sum_dict = {}
    for item in sol_arr:
        add = list1.index(item) + list2.index(item)
        if add not in sum_dict.keys():
            sum_dict[add] = [item]
        else:
            sum_dict[add].append(item)
    mini = min(list(sum_dict.keys()))
    return sum_dict[mini]
print(finding(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Shogun","Burger King"]))
