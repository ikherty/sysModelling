#f(x)=1/x^2 x:1..a
from math import *
k=2500 #число элементов
r=0#кол-во интервалов
p=0#теоретическая вероятность попадания в каждый интервал
array=[] #массив псевдослучайных чисел
newarray=[]#новый массив
VerU=[]
l_aper=0 #длина апериодичности
l_per=0 #длина периода
p_i =[] #количество попаданий в каждый интервал
X2=0 #хи-вквадрат

def fraction(x):
    # функция для расчета дробной части
    return x - int(x)

def fillArray():
    # функция для заполнения массива
    y0=0.45864863#float(input("Введите гамма-нулевое: "))
    accrs=8#int(input("Введите количество знаков после запятой: "))
    for i in range(k):
        array.append(y0)
        y0=(10 ** -accrs)*int((10 ** accrs)*fraction(float(((1-y0) ** 3)*(10 ** accrs)))) #метод середины квадратов
    print("Массив заполнен псевдослучайными числами.")
    for i in range(k):
        #по новой формуле заполняем массив
        newarray.append(array[i]**0.1)

def periodLength():
    global l_aper, l_per
    print("Определение длины периода и апериодичности.")
    flag=True #пока в последовательности будут одинаковые элементы
    for i in range(k):
        for j in range(i+1, k):
            if(abs(newarray[i]-newarray[j])<0.00000001):#сравниваем
                print("Cовпадение в ", i, "-ом и ", j, "-ом элементах: ", newarray[i], " и ", newarray[j])
                l_aper = j
                l_per = j-i
                flag=False
            if not flag:
                break
        if flag:
            #если нет одинаковых элементов, длина апериодичности = длине последовательности
            l_aper=k
            l_per=0
        if not flag:
            break

def calc_pi():
    print("Рассчет количества попаданий в каждый интервал.")
    global newarray, r, p
    r = int((1 + 3.3 * log10(k)))
    p = float((1 / r))
    print("Число интервалов", r)
    for i in range(r):
        #обнуляем p_i
        p_i.append(0)
    print("Распределение по интервалам:")
    for i in range(k):
        for j in range(k):
            if (newarray[j]>(i*p) and newarray[j]<((i+1)*p)):
                p_i[i]+=1
    for i in range(r):
        print(p_i[i], end = ', ')

def calc_X2():
    print("Рассчет Х2.")
    X2 = 0
    tver=[]
    for i in range(r):
        tver.append((((i+1)/r)**10)-(i/r)**10)
    for i in range(r):
        X2+=((p_i[i]-(k*tver[i])) ** 2)/(k*tver[i])
    print("X2 = ", X2)

def show():
    n=int(input("Вывести последовательность до: "))
    if n>k:
        n=k
    for i in range(n):
        print(newarray[i], end = ', ')

fillArray()
periodLength()
calc_pi()
calc_X2()
show()
