# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв а в слове
word = 'Архангельск'
print(len(word))

# Вывести количество гласных букв в слове
word = 'Архангельск'
wovels = list('аеёиоуыэюя')
letters = list(word.lower())
print(len([l for l in letters if l in wovels]), end=', ')

count = 0
for letter in word.lower():
    if letter in wovels:
        count += 1

print(count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for wrd in sentence.split():
    print (wrd[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words = sentence.split()
print(sum([len(wrd) for wrd in words]) / len(words))
