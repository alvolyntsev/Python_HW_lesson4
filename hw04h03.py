# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
import random
res='YES'
ex=0
while res=='YES' and ex<10000: #тут можно поиграть с возможностью случайно подобрать значение ex- кол-во итераций случайного подбора
    x1=random.randint(0,7)
    y1=random.randint(0,7)
    x2=random.randint(0,7)
    y2=random.randint(0,7)
    x3=random.randint(0,7)
    y3=random.randint(0,7)
    x4=random.randint(0,7)
    y4=random.randint(0,7)
    x5=random.randint(0,7)
    y5=random.randint(0,7)
    x6=random.randint(0,7)
    y6=random.randint(0,7)
    x7=random.randint(0,7)
    y7=random.randint(0,7)
    x8=random.randint(0,7)
    y8=random.randint(0,7)
    figures=[[x1,y1],[x2,y2],[x3,y3],[x4,y4],[x5,y5],[x6,y6],[x7,y7],[x8,y8]]
    board=[[0,0,0,0,0,0,0,0] for _ in range(8)]
    #print(figures)
    #print(figures[1])
    figures_rotate = list(map(list, (zip(*figures))))
    #print(len(figures_rotate))
    #print(len(figures_rotate[1]))
    res='NO'
    sumdiag=[]
    difdiag=[]
    for x in range(0, (len(figures_rotate))):
    #    print(x)
        for y, fig in enumerate(figures_rotate[x]):
            for z in range(y+1, len(figures_rotate[x])): #ищем повторы по оси х и по оси y, это покажет пересечения по вертикали либо горизонтали
                if fig==figures_rotate[x][z]: res='YES' #and print('par')
                # ищем пересечения на диагоналях как суммы и разности x и y
    for idx, x in enumerate(figures):
        sumdiag.append(figures[idx][0]+figures[idx][1])
        difdiag.append(figures[idx][0]-figures[idx][1])
    #print(sumdiag, difdiag)
    for idx, diag in enumerate(sumdiag):
        for z in range(idx+1, len(sumdiag)):
            if diag == sumdiag[z]: res = 'YES' #and print('sum')
    for idx, diag in enumerate(difdiag):
        for z in range(idx+1, len(difdiag)):
            if diag == difdiag[z]: res = 'YES' #and print('dif')
    ex+=1


print(res)

for figur in figures:
    #    print(figur[0], figur[1])
    board[figur[0]][figur[1]]=1

for bo in board:
    print(bo)