from math import *
import numpy as np
import matplotlib.pyplot as plt

# ВВЕДИТЕ ПОДЫНТЕГРАЛЬНУЮ ФУНКЦИЮ
def f(x):
    return (pow(x, 2) + 7*x + 12) * cos(x)

# ВВЕДИТЕ ТОЧНОЕ ЗНАЧЕНИЕ ИНТЕГРАЛА
I_prec =  7 - 2 * sin(4) + cos(4)


##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################

# Функция нахождения погрешности, где I_approx - вычисленная нами приближенная точность
def errorRate(I_approx):
    return abs(I_prec - I_approx)

# Метод левых прямоугольников
def methLeftRectangle(x_array):
    k, total = 0, 0.0
    for i in range(len(x_array)):
        if(k < len(x_array)-1):
            total += f(x_array[i]) * (x_array[i+1] - x_array[i])
            k += 1
    
    return (total)

# Метод правых прямоугольников
def methRightRectangle(x_array):
    k, total = 0, 0.0
    for i in range(len(x_array)):
        if(k < len(x_array)-1):
            total += f(x_array[i+1]) * (x_array[i+1] - x_array[i])
            k += 1
    return (total)

# Метод средних прямоугольников
def methMiddleRectangle(x_array):
    k, total = 0, 0.0
    for i in range(len(x_array)):
        if(k < len(x_array)-1):
            total += f( (x_array[i+1] + x_array[i]) /2 ) * (x_array[i+1] - x_array[i])
            k += 1
    return (total)

# Метод трапеций
def methTrapeze(x_array):
    k, total = 0, 0.0
    for i in range(len(x_array)):
        if(k < len(x_array)-1):
            total += ( (f(x_array[i]) + f(x_array[i+1])) /2 ) * (x_array[i+1] - x_array[i])
            k += 1
    return (total)

# Метод парабол
def methParabola(x_array):
    k, total = 0, 0.0
    for i in range(len(x_array)):
        if(k < len(x_array)-1):
            total += ( f(x_array[i]) + 4*f( (x_array[i+1] + x_array[i])/2) + f(x_array[i+1])) * (x_array[i+1] - x_array[i])
            k += 1
    total *= 1/6
    return (total)

a, b = int(input("Введите левую границу предела интегрирования: ")), int(input("Введите правую границу предела интегрирования: "))
# Для шага разбиения отрезка интегрирования
N_len = int(input("Введите кол-во чисел разбиения: "))

# Список сохранения чисел разбиения
N_list = []
# Списки сохранения для погрешностей каждых из пяти методов
errRate_MethLeftRectangle = []
errRate_MethRightRectangle = []
errRate_MethMiddleRectangle = []
errRate_MethTrapeze = []
errRate_MethParabola = []
# Список сохранения шагов разбиения
step_list = []

for i in range(N_len):
    numb = int(input((f"Введите число разбиений (number{i+1}):")))
    N_list.append(numb)

print("\nМассив чисел разбиений: ", end = " ")
for i in range(len(N_list)):
    print(N_list[i], end = " ")
print("\n")
print("Точное значение: ", I_prec, "\n")

for i in range(len(N_list)):
    # linspace используется для создания массива чисел с равномерно распределенными значениями.
    lim_integr = np.linspace(a, b, N_list[i])
    
    print(f"===РАЗБИЕНИЕ {N_list[i]}")

    print(f"Шаг разбиений: {lim_integr[1] - lim_integr[0]}")
    step_list.append(lim_integr[1] - lim_integr[0])    

    print("Наш массив: ")
    for i in range(len(lim_integr)):
        print(lim_integr[i], end = "  ")
    print("\n")

    print("\t", "===ДЕМОНСТРАЦИЯ МЕТОДОВ", "\n", "\t" ,"Метод прямоугольников:", sep = "")
    print(f"Вызван метод левых прямоугольникoв(приближенное значение): {methLeftRectangle(lim_integr)}", "|" ,end = " ")
    print(f"Погрешность: {errorRate(methLeftRectangle(lim_integr))}")
    errRate_MethLeftRectangle.append(errorRate(methLeftRectangle(lim_integr)))

    print(f"Вызван метод правых прямоугольникoв(приближенное значение): {methRightRectangle(lim_integr)}", "|" ,end = " ")
    print(f"Погрешность: {errorRate(methRightRectangle(lim_integr))}")
    errRate_MethRightRectangle.append(errorRate(methRightRectangle(lim_integr)))

    print(f"Вызван метод средних прямоугольникoв(приближенное значение): {methMiddleRectangle(lim_integr)}", "|" ,end = " ")
    print(f"Погрешность: {errorRate(methMiddleRectangle(lim_integr))}")
    errRate_MethMiddleRectangle.append(errorRate(methMiddleRectangle(lim_integr)))

    print("\n", "\t" ,"Метод трапеций и парабол:", sep = "")

    print(f"Вызван метод трапеций(приближенное значение): {methTrapeze(lim_integr)}", "|" ,end = " ")
    print(f"Погрешность: {errorRate(methTrapeze(lim_integr))}")
    errRate_MethTrapeze.append(errorRate(methTrapeze(lim_integr)))

    print(f"Вызван метод парабол(приближенное значение): {methParabola(lim_integr)}", "|" ,end = " ")
    print(f"Погрешность: {errorRate(methParabola(lim_integr))}")
    errRate_MethParabola.append(errorRate(methParabola(lim_integr)))
    print("\n\n")

    
print("Таблица погрешностей каждых из методов относительно шагов разбиения: ")
# N - разбиения,  ,mLR - methLeftRectangle, mRR - methRightRectangle, ...
print("  N \t\t Step \t\t mLR \t\t mRR \t\t mMR \t\t mT \t\t mP")
for i in range (len(errRate_MethLeftRectangle)):
    print(f"{N_list[i]: .5f}\t{step_list[i]: 5f}\t{errRate_MethLeftRectangle[i]: 5f}\t{errRate_MethRightRectangle[i]: 5f}\t{errRate_MethMiddleRectangle[i]: 5f}\t{errRate_MethTrapeze[i]: 5f}\t{errRate_MethParabola[i]: 5f}")   
   
plt.figure(figsize=(10, 6))
plt.plot(step_list, errRate_MethLeftRectangle, marker = 'o', linestyle = '-', label = 'Левый прямоугольник (mLR)')
plt.plot(step_list, errRate_MethRightRectangle, marker = 's', linestyle = '--', label = 'Правые прямоугольник (mRR)')
plt.plot(step_list, errRate_MethMiddleRectangle, marker='^', linestyle='-.', label='Средние прямоугольники (mMR)')
plt.plot(step_list, errRate_MethTrapeze, marker='d', linestyle=':', label='Трапеции (mT)')
plt.plot(step_list, errRate_MethParabola, marker='v', linestyle='-', label='Параболы (mP)')

plt.xlabel('Шаг разбиения h')
plt.ylabel('Погрешность ∆')
plt.title('Зависимость погрешности методов от шага разбиения')
plt.grid(True)
plt.legend()
plt.show()