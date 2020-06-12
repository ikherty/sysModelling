from math import *
k=2500 #число элементов
r=0#кол-во интервалов
p=0#теоретическая вероятность попадания в каждый интервал
array=[] #массив псевдослучайных чисел
newarray=[]#новый массив
secarray=[]
l_aper=0 #длина апериодичности
l_per=0 #длина периода
p_i =[] #количество попаданий в каждый интервал
X2=0 #хи-вквадрат

def fraction(x):
    # функция для расчета дробной части
    return x - int(x)

def fillArray():
    print(k)
    # функция для заполнения массива
    y0=0.1234#float(input("Введите гамма-нулевое: "))
    accrs=4#int(input("Введите количество знаков после запятой: "))
    for i in range(k):
        array.append(y0)
        y0=(10 ** -accrs)*int((10 ** accrs)*fraction(float(((1-y0) ** 3)*(10 ** accrs)))) #метод середины квадратов
    print("Массив заполнен псевдослучайными числами.")
    for i in range (k):
        newarray.append((2*array[i])**(1/3))#новый массив для первого интеграла
    for i in range (k):
        secarray.append(2*array[i])#новый массив для второго интеграла

def calc_pi():
    print("Рассчет количества попаданий в каждый интервал.")
    global r, p
    r = int((1 + 3.3 * log10(k)))
    p = float((1 / r))
    print("Число интервалов", r)
    for i in range(r):
        #обнуляем p_i
        p_i.append(0)
    #print("Распределение по интервалам:")
    for i in range(k):
        for j in range(k):
            if (array[j]>(i*p) and array[j]<((i+1)*p)):
                p_i[i]+=1
    #for i in range(r):
    #    print(p_i[i], end = ', ')

def calcI1():
    I1=0#вычисление интеграла по плотности x^2
    for i in range (k):
        I1+=newarray[i]**2
    I1=I1*2/(3*k)#M1
    print("I1=", I1)
    D1=0#дисперсия 1
    d=0
    for i in range (k):
        d+=newarray[i]**4
    D1=d*4/(9*k)-I1**2
    print("D1=", D1)
    E1=3 * ((D1 / k) ** 0.5)
    print("E1=", E1)

def calcI2():
    I2=0#вычисление интеграла по плотности 1/2
    for i in range (k):
        I2+=secarray[i]**4
    I2=I2*2/k#M2
    print("I2=", I2)
    D2=0#дисперсия 2
    d=0
    for i in range (k):
        d+=secarray[i]**8
    D2=d*4/k-I2**2
    print("D2=", D2)
    E2=3 * ((D2 / k) ** 0.5)
    print("E2=", E2)

def show():
    n=30#int(input("Вывести последовательность до: "))
    if n>k:
        n=k
    for i in range(n):
        print(array[i], end = ', ')

fillArray()
calc_pi()
calcI1()
calcI2()
#show()
