'''
Напишите функцию single_root_words, которая принимает одно обязательное слово
в параметр root_word, а далее неограниченную последовательность в параметр *other_words.
Функция должна составить новый список same_words только из тех слов списка other_words,
которые содержат root_word или наоборот root_word содержит одно из этих слов.
После вернуть список same_words в качестве результата своей работы.
'''

# Решение задачи «Однокоренные»

def single_root_words(root_word, *other_words):
    same_words = []
    for tmp_word in other_words:
        if (tmp_word.lower() in root_word.lower()) or (root_word.lower() in tmp_word.lower()):
            same_words.append(tmp_word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
