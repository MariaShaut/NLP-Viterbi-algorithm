import pandas as pd


# initialization
tags = ['Start', 'Noun', 'Verb', 'Conj', 'Pro']
words = ['terangan', 'legh', 'yaS']

tags_1 = pd.Series({'Noun': 4.1, 'Verb': 0.1, 'Conj': 0.1, 'Pro': 0.1})
tags_2 = pd.Series({'Noun': 0.1, 'Verb': 0.1, 'Conj': 0.1, 'Pro': 0.1})
tags_3 = pd.Series({'Noun': 0.1, 'Verb': 0.1, 'Conj': 0.1, 'Pro': 0.1})
emission = pd.DataFrame([tags_1, tags_2, tags_3], index = ['terangan', 'legh', 'yaS'])

tags_1 = pd.Series({'Noun': 1.1, 'Verb': 0.1, 'Conj': 0.1, 'Pro': 0.1})
tags_2 = pd.Series({'Noun': 1.1, 'Verb': 3.1, 'Conj': 1.1, 'Pro': 2.1})
tags_3 = pd.Series({'Noun': 5.1, 'Verb': 0.1, 'Conj': 0.1, 'Pro': 0.1})
tags_4 = pd.Series({'Noun': 1.1, 'Verb': 0.1, 'Conj': 0.1, 'Pro': 0.1})
tags_5 = pd.Series({'Noun': 0.1, 'Verb': 2.1, 'Conj': 0.1, 'Pro': 0.1})
 
transition = pd.DataFrame([tags_1, tags_2, tags_3, tags_4, tags_5], index = tags)
 
tags_1 = pd.Series({words[0]: None, words[1]: None, words[2]: None}) 

result = pd.DataFrame([tags_1, tags_1, tags_1, tags_1], index = tags[1:])


# algorithm
start_probab = 1.0

for i in tags[1:]:
    result.loc[i]['terangan'] = start_probab * emission.loc['terangan'][i] * transition.loc['Start'][i]         
        
        
def findMax(word, tag):
    max_value = 0
    for i in tags[1:]:
        index = words.index(word, )
        prev = words[index - 1]
        temp = result.loc[i][prev] * transition.loc[tag][i]
        if temp > max_value:
            max_value = temp
    return max_value

for i in words[1:]:
    for j in tags[1:]:
        result.loc[j][i] = emission.loc[i][j] * findMax(i, j)
        
        
for i in words[0:]:
    res = tags[1]
    for j in tags[2:]:
        if result.loc[j][i] > result.loc[res][i]:
            res = j
    print('The word ', i, ' is ', res)

  

