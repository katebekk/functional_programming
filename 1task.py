# Задан текст, состоящий из символов. Текст содержит предложения. Признаком конца предложения является точка.
# Построить список предложений. Для каждого предложения посчитать количество слов (слова отделяются пробелом). 
# Найти предложение, число слов в котором наибольшее. 
# Найти в каждом предложении слово максимальной длины и построить список таких слов.

this_text = "Привет меня зовут Катя.Я живу во Владивостоке.Слушаю музыку.Слушаю музыку.Люблю смотреть сериалы."
# Построить список предложений.(возвращает список предложений)
def split_text(txt):
    sentences = txt.split('.')
    
    return sentences

# Для каждого предложения посчитать количество слов (слова отделяются пробелом).(возвращает  список списков состоящих из предложения и количества слов в нем)
def words_num(sentences):
    numbers = [] 
    for k in sentences:
        i = k.split(' ')
        j = len(i)
        if(i[j-1] != ''):
            numbers.append([j,k])
    return numbers

# Найти предложение, число слов в котором наибольшее.(возвращает пару: предложение и число слов в нем)
def max_sent(numbers):
    num = 0
    main_sent = []
    for k in numbers:
        if(k[0] > num):
            num = k[0]
            main_sent = k
    return main_sent

# Найти в каждом предложении слово максимальной длины и построить список таких слов.(возвращает список слов)
def max_word(sentences):
    max_words = []
    for k in sentences:
        i = k.split(' ')
        word = ''
        l = 0
        for el in i:
            if(len(el) > l):
                l = len(el)
                word = el
        max_words.append(word)
    return max_words

def main(text):
    sentences = split_text(text)
    print ("список предложений ", sentences)
    wn = words_num(sentences)
    print ("список предложений и количества слов каждого предложения ", wn)
    ms = max_sent(wn)
    print ("самое длинное предложение ", ms)
    mw = max_word(sentences)
    print ("список самых длинных слов ", mw)
    

main(this_text)