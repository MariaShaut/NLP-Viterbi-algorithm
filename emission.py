import sys
import re
import os
words1 = "pa’Daq ghah taH tera’ngan ’e".replace("’","'").split()
tags1 = "N PRO V N PRO".split()

words2 = "ja’chuqmeH rojHom neH tera’ngan".replace("’","'").split()
tags2 = "V N V N".split()

words3 = "tera’ngan qIp puq ’eg puq qIp tera’ngan".replace("’","'").split()
tags3 = "N V N CONJ N V N".split()

train = []
train.append(zip(words1, tags1))
train.append(zip(words2, tags2))
train.append(zip(words3, tags3))

from collections import defaultdict
new_dict = defaultdict(list)
#print(new_dict)
for sent in train:
    
    for word, tag in sent:
        new_dict[word].append(tag)
    #print(new_dict)

for word, tags in sorted(new_dict.items()):
    row = []
    row.append(word)

    #print(row)

    for tag in ["N", "V", "CONJ", "PRO"]:
        row.append(tags.count(tag)+0.1)

    print(row)

