import re

def odd_words(sentence):
    split_sentence = sentence.split(" ")
    list_words = []
    for i in split_sentence:
        passed_words = re.sub("[.!?]", "", i)
        list_words.append(passed_words)
    ordered_words = {}
    for word in list_words:
        if len(word) in ordered_words: 
            ordered_words[len(word)] = ordered_words[len(word)] + [word]
        else:
            ordered_words[len(word)]=[word]
    odd_words_dictionary = {}
    for word in ordered_words:
        for odd_words in ordered_words[word]:
            if len(odd_words) % 2 == 1:
                odd_words_dictionary[word] = ordered_words[word]
        else:
            continue
    return odd_words_dictionary




# Tests
assert(odd_words("This is a sentence. And yet another one!") == {1: ['a'], 3: ['And', 'yet', 'one'], 7: ['another']})
assert(odd_words("Miscollated alphabetic superimposition") == {11: ['Miscollated'], 15: ['superimposition']})
print(odd_words("a a a a bb bb bb ccc ccc") == {1: ['a', 'a', 'a', 'a'], 3: ['ccc', 'ccc']})