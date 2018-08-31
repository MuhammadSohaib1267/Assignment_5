def remove_adjacent(num):
    s=set(num)
    return s

def linear_merge(list1,list2):
    list1.sort()
    list2.sort()
    z=len(list2)
    for i in range(z):
        list1.append(list2[i])
    return list1    