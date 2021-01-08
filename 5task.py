# Про каждое блюдо известен набор продуктов, требуемый для его изготовления, и количество каждого продукта.
# Задан список продуктов, имеющихся в наличие: какой продукт, сколько.
# Написать функции, формирующие возможное меню. Учитывать, что суммарное количество одного и того же продукта 
# в меню не может превышать имеющееся количество продукта.

dishes = [["Борщ", [["Картофель", 2],["Капуста", 1],["Свекла", 1],["Морковь", 1],["Фасоль", 1]]],
["Плов", [["Рис", 100],["Морковь", 1],["Чеснок", 1],["Грибы", 100]]],
["Ризотто",[["Рис", 100],["Сливки", 100],["Чеснок", 1],["Грибы", 100]]],
["Пицца", [["Помидор", 2],["Тесто", 200],["Сыр", 100]]],
["Щи", [["Картофель", 2],["Капуста", 1],["Свекла", 1],["Морковь", 1]]]]

inStock = [["Картофель", 10],["Капуста", 5],["Свекла", 6],["Морковь", 7],["Фасоль", 3],["Рис", 200],["Сливки", 100],["Чеснок", 1],["Грибы", 200]]

# Написать функции, формирующие возможное меню. Учитывать, что суммарное количество одного и того же продукта 
# в меню не может превышать имеющееся количество продукта.

def findProdact(prodact, inSt):
    for st in inSt:
        if(prodact[0] == st[0]):
            return inSt.index(st)
def delProd(prodact, inSt):
    ind = findProdact(prodact, inSt)
    if(inSt[ind][1] > prodact[1]):
        inSt[ind][1] = inSt[ind][1] - prodact[1]
    else: inSt.remove(inSt[ind])
    
def makeMenu(Stock):
    St = Stock
    menu = []
    for d in dishes:
        isAll = 0
        for prod in d[1]:
            if(findProdact(prod , St) != None):
                isAll = isAll + 1
                delProd(prod, St)
        if(isAll == len(d[1])):
            menu.append(d[0])
    
    return menu        
            
            
print(makeMenu(inStock))

