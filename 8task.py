# 15 вариант
# Реализовать набор предикатов работы с множествами.
# Каждый предикат должен вычислять сложность(число шагов необходимых для вычисления) для самого себя.
# 1) Добавление заданных элементов
# 2) Удаление заданных элементов
# 3) Проверка на принадлежность
# 4) Объеденение 3х множеств
# 5) Пересечение 3х множеств
# 6) Вывод на экран элементов множества в порядке возрастания

list = []

def find(el, L):
    for l in L:
        if(l == el):
            return L.index(l)

# 1) Добавление заданных элементов
def addToList(L, new_el):
    for el in new_el:
        L.append(el)
    return L

# 2)Удаление заданных элементов
def delInList(L, del_el):
    for el in del_el:
        if(find(el, L) != None):
            L.remove(el)
    return L

# 3) Проверка на принадлежность
def isInList(L, els):
    isHere = true
    for el in els:
        if(find(el, L) == None):
            isHere = false
    return isHere

# 4) Объеденение 3х множеств
def union(L1, L2, L3):
    L = []
    for el in L1:
        if(find(el, L) == None):
            L.append(el)
    for el in L2:
        if(find(el, L) == None):
            L.append(el)
    for el in L3:
        if(find(el, L) == None):
            L.append(el)
    return L
    
print(union([1,2,4],[2,5,17],[12,1,0]))

# 5) Пересечение 3х множеств
def cross(L1, L2, L3):
    L = L1
    for el in L:
        if(find(el, L2) == None):
            L.remove(el)
    for el in L:
        if(find(el, L3) == None):
            L.remove(el)

    return L


print(cross([1,2,4],[2,5,17,1],[12,1,0,2]))

# 6) Вывод на экран элементов множества в порядке возрастания
def sort(List):
    L = List
    N = len(List)
    for i in range(N-1):
        for j in range(N-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L
    
print(sort([90,2,1,34,65,22,12]))



    






















