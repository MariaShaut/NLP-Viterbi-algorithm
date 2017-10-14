words1 = "pa’Daq ghah taH tera’ngan ’e".replace("’","'").split()
tags1 = "Start N PRO V N PRO".split()

words2 = "ja’chuqmeH rojHom neH tera’ngan".replace("’","'").split()
tags2 = "V N V N".split()

words3 = "tera’ngan qIp puq ’eg puq qIp tera’ngan".replace("’","'").split()
tags3 = "N V N CONJ N V N".split()

for tag in tags2:
    tags1.append(tag)
#print(tags1)
for tag in tags3:
    tags1.append(tag)
#tags1[0] = 'Start'
#print(tags1)

Matrix = [[0 for x in range(4)] for y in range(5)]

for i in range(5):
    for k in range(4):
        Matrix[i][k] = 0.1

index = 0
rowNames = ['Start', 'N', 'V', 'CONJ', 'PRO']
colNames = ['N', 'V', 'CONJ', 'PRO']

while index < len(tags1) - 1:
    word1 = tags1[index]
    word2 = tags1[index + 1]
    #print(word1, word2)
    
    ind1 = rowNames.index(word1)
    ind2 = colNames.index(word2)
        
    Matrix[ind1][ind2] =  Matrix[ind1][ind2] +1
    
    index = index +1
print(Matrix)
