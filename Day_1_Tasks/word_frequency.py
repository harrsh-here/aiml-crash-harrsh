# To count frequency of letter in a sentence using normal function and collections.Counter

from collections import Counter
sentence = "Harsh is Awesome"
def count_char(sentence):
    done = {}
    for c in sentence:
        if c not in done:
            done[c] = 1
        else:
            done[c] += 1
    return sorted(done.items(), key = lambda x : x[1], reverse = True)       
print(count_char(sentence))

print(Counter(sentence))