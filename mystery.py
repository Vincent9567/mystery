import re

def odd_words(sentence):
    split_sentence = sentence.split(" ")
    list_words = []
    for i in split_sentence:
        passed_words = re.sub("[.!?]", "", i)
        list_words.append(passed_words)
    return list_words

def ordered_words_dict(list):
    ordered_words = {}
    for word in list:
        if len(word) in ordered_words: 
            ordered_words[len(word)] = ordered_words[len(word)] + [word]
        else:
            ordered_words[len(word)]=[word]
    return ordered_words
     
def odd_words_dict(ordered_words_list):
    odd_words_dictionary = {}
    for word in ordered_words_list:
        for odd_words in ordered_words_list[word]:
            if len(odd_words) % 2 == 1:
                odd_words_dictionary[word] = ordered_words_list[word]
        else:
            continue
    return odd_words_dictionary

def create_odd_words_dict(string):
   return odd_words_dict(ordered_words_dict(odd_words(string)))





# Tests
assert(create_odd_words_dict("This is a sentence. And yet another one!") == {1: ['a'], 3: ['And', 'yet', 'one'], 7: ['another']})
assert(create_odd_words_dict("Miscollated alphabetic superimposition") == {11: ['Miscollated'], 15: ['superimposition']})
print(create_odd_words_dict("a a a a bb bb bb ccc ccc") == {1: ['a', 'a', 'a', 'a'], 3: ['ccc', 'ccc']})