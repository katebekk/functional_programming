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

def make_text(text, start, end):
    if(end >= len(text)):
        return []
    else:
        if(text[end] == "."):
            d = {}
            b = []
            d = dict([(text[start:(end+1)], count_words(text[start:(end+1)],0,0))])
            d.update(make_text(text, end + 1, end + 2))
            return d
        else:
            if(text[end] != "."):
                return make_text(text, start, end + 1)


print(make_text(this_text,0,0))
