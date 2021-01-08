# Задан текст, состоящий из символов. Текст содержит предложения. Признаком конца предложения является точка.
# Построить список предложений. Для каждого предложения посчитать количество слов (слова отделяются пробелом). 
# Найти предложение, число слов в котором наибольшее. 
# Найти в каждом предложении слово максимальной длины и построить список таких слов.

this_text = "Привет меня зовут Катя.Я живу во Владивостоке.Слушаю музыку.Слушаю музыку.Люблю смотреть сериалы."
text = "Привет меня зовут."

# считает слова в предложение
def count_words(text,count = 0,i = 0):
    if(text[i] == "."):
        count = count + 1
    else:
        if(text[i] == " "):
            count = count_words(text, count + 1, i + 1)
        else:
            count = count_words(text, count, i + 1)
    return count
    
print(count_words(text, 0, 0))

# Построить список предложений. Для каждого предложения посчитать количество слов (слова отделяются пробелом). 
def make_text(text, start, end, d):
    if(end >= len(text)):
        return []
    elif(text[end] == "."):
        d.append([text[start:(end+1)], count_words(text[start:(end+1)],0,0)])
        make_text(text, end + 1, end + 2, d)

    elif(text[end] != "."):
        return make_text(text, start, end + 1,d)


d = []
make_text(this_text,0,0,d)

txt = d.copy()
txt.pop(1)
print(d)

# Найти предложение, число слов в котором наибольшее.
def max_list(text):
    if(len(text) == 1):
        return text[0]
    elif(text[0][1] < text[1][1]):
        return(max_list(text[1:])) 
    elif(text[0][1] >= text[1][1]):
        if(len(text) == 2):
            return text[0]
        else:
            txt = text.copy()
            txt.pop(1)
            return(max_list(txt)) 
print(max_list(d))

# Найти в каждом предложении слово максимальной длины и построить список таких слов.
def len_word(string,start,end,d):
    if(len(string) <= end):
        return None
    elif((string[end] == " ") or (string[end] == ".")):
        d.append([string[start:(end)], end-start])
        len_word(string,end+1,end+2,d)
    elif(string[end] != " "):
        return len_word(string,start,end+1,d)  

def max_word(text):
    if(len(text) == 1):
        return text[0]
    elif(text[0][1] < text[1][1]):
        return(max_word(text[1:])) 
    elif(text[0][1] >= text[1][1]):
        if(len(text) == 2):
            return text[0]
        else:
            txt = text.copy()
            txt.pop(1)
            return(max_word(txt)) 
        
w=[]        
len_word(this_text,0,0,w)
print(max_word(w))    


