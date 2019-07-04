# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import random
import re
file=open('cifer.txt', 'w')

cifer=''
for _ in range(2500):
    cifer=cifer+str(random.randint(0,9))
#cifer=cifer+'444444444'
file.write(cifer)
file.close()
file=open('cifer.txt', 'r')
cif=(re.findall(r'[0]+|[1]+|[2]+|[3]+|[4]+|[5]+|[6]+|[7]+|[8]+|[9]+', file.read()))  #line2=(re.findall(r'[a-z]+', line))
idxmax=0
maxlen=0
for idx, i1 in enumerate(cif):
    if maxlen<len(i1):
        maxlen=len(i1)
        idxmax=idx
print(cif)
print('максимальная последовательность:', cif[idxmax])
