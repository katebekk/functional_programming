# 15 вариант
# Реализовать набор предикатов работы с множествами.
# Каждый предикат должен вычислять сложность(число шагов необходимых для вычисления) для самого себя.
# 1) Добавление заданных элементов
# 2) Удаление заданных элементов
# 3) Проверка на принадлежность
# 4) Объеденение 3х множеств
# 5) Пересечение 3х множеств
# 6) Вывод на экран элементов множества в порядке возрастания

list1 = [6,1,1,2,3,11,6,1]
list2 = [8,9,1]
# 1) Добавление заданных элементов
def add(list1,list2):
    list3 = list1.copy()
    return list3+list2
print(add(list1,list2))

# 2) Удаление заданных элементов
def del_numb(list1, num):
    if(len(list1) == 1):
      if(list1.count(num) > 0):
            list1.remove(num) 
            return list1
    else:
        if(list1.count(num) > 0):
            ind = list1.index(num) 
            list1.remove(num)
            return del_numb(list1,num)

def del_list(list1,list2):
    if(len(list2) == 1):
        if(list1.count(list2[0]) > 0):
            del_numb(list1,list2[0])
            return list1
    else:
        if(list1.count(list2[0]) > 0):
            del_numb(list1,list2[0])
        return del_list(list1,list2[1:])
print(del_list(list1,list2))
del_numb(list1,1)

# 3) Проверка на принадлежность
def inList(list1, list2):
    print(list2)
    b = True
    if(len(list2) == 1):
        if(list1.count(list2[0]) == 0):
            b = False
            return b
    else:
        if(list1.count(list2[0]) == 0):
            b = False
        b = inList(list1, list2[1:])
    return b
    
l1 = [3,4,5,11,2]
l2 = [2,3]
print(inList(l1,l2))

# 4) Объеденение 3х множеств
def union2(list1,list2):
    if(len(list2) == 1):
       if(list1.count(list2[0]) == 0): 
           list1.append(list2[0])
           return list1
    else:
        if(list1.count(list2[0]) == 0):
           list1.append(list2[0])
        union2(list1, list2[1:])
    return list1
    
def union3(list1,list2,list3):
    return union2(union2(list1,list2),list3)
    
L1 = [3,4,5,11,2]
L2 = [2,6]
L3 = [2,3,8,9]
print("объединение :", union3(L1, L2,L3))

# 5) Пересечение 3х множеств
def cross(l1,l2,l3):
    if(len(l2) == 1):
        if(l1.count(l2[0]) != 0): 
            l3.append(l2[0])
            return l3
    else:
        if(l1.count(l2[0]) != 0):
            l3.append(l2[0])
        cross(l1,l2[1:],l3)
    return l3

ll = []
def cross3(l1,l2,l3):
    ll = []
    l = cross(l1,l2, ll)
    ll =[]
    return cross(l,l3,ll)
    
L1 = [3,4,5,11,2,6]
L2 = [2,6,8]
L3 = [2,3,8,9,6]

print("пересечение :", cross3(L1, L2,L3))

# 6) Вывод на экран элементов множества в порядке возрастания
def sort(list,cur,pr):
    if(cur == len(list)-1):
        pr = pr + 1
    elif(list[cur] > list[cur+1]):
        list[cur],list[cur+1] = list[cur+1],list[cur]
        sort(list,cur+1,pr)
    elif(list[cur] <= list[cur+1]):
        sort(list,cur+1,pr)
    if(pr < len(list)-1):
        sort(list,pr+1,pr+1)
    return list

L3 = [2,3,8,9,6]
print(sort(L3,0,0))

