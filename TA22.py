from random import randint

def linSearch(n):
    a = [randint(1, 99) for item in range(n)]
    print(a)
    k = int(input('Ввидете нужный элемент '))
    for i in range(n):
        if k == a[i]:
            return i
    return 'Элемента нет в массиве'

def binSearch(n):
    a = [randint(1, 99) for item in range(n)]
    print(a.sort())
    k = int(input('Ввидете нужный элемент '))
    left = 0
    right = int(len(a)-1)
    while left <= right:
        mid = int(len(a) // 2)
        if a[mid] == k:
            return mid
        elif a[mid]<k:
            left = mid+1
        else:
            right=mid-1
    return 'Искомого элементма нет в массиве'


def sellect(n):
    a = [randint(1, 99) for item in range(n)]
    print(a)
    # цикл перебирает элементы массива
    for i in range(n - 1):
        # цикл перебирает элементы неосортированной части массива
        for j in range(i + 1, n):
            # если выбранный элемент отсортированной части массива больше неотсортированной
            # то в переменной b запоминается выбранный элемент отсортированной части
            # на место выбранного элемента отсортированной части ставится элемент неотсортированной
            # на место неотсортированной части ставится отсортированный
            if a[i] > a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
    print('-----------------------------------')
    print(a)
    return


def insertion(n):
    a = [randint(1, 99) for item in range(n)]
    print(a)
    # берем элемент массива
    for i in range(n):
        # берем предыдущий индекс массива
        j = i - 1
        # во временной переменной записываем выбранный элемент массива
        tmp = a[i]
        # если предыдущий элемент массива больше выбранного и не конец отсортированной части
        while a[j] > tmp and j >= 0:
            # выбрранный элемент становится предыдущим
            a[j + 1] = a[j]
            j -= 1
        # на место последнего помененого элемента записывается выбранный элемент
        a[j + 1] = tmp
    print('-----------------------------------')
    print(a)
    return a


def bubl(n):
    a = [randint(1, 99) for item in range(n)]
    print(a)
    # берем элемент массива
    for i in range(n - 1):
        # берем следующий элемент
        for j in range(i + 1, n):
            # если предыдущий элемент больше следующиего то меняем их местами
            # и продвигаемся дальше по массиву пока наибольший элемент не всплывет
            if a[j - 1] > a[j]:
                tmp = a[j - 1]
                a[j - 1] = a[j]
                a[j] = tmp
    print('-----------------------------------')
    print(a)
    return a


def fastSort(n):
    a = [randint(1, 99) for item in range(n)]
    print(a)
    def quickSort(arr):
    # проверяем что массив состоит больше чем из 1 элемента
        if len(arr) <= 1:
            return arr
        else:
    # выбираем элемент по середине
            tmp = arr[len(arr) // 2]
    # создаем массивы куда сохранятся левая и правая часть
            left = []
            right = []
            middle = []
    # перебираем элементы
            for i in range(len(arr)):
    # если выбранный элемент меньше элементра по середине то записываем его в левую часть
    # если больше в правую а если он равен то посередине
                if tmp > arr[i]:
                    left.append(arr[i])
                elif tmp < arr[i]:
                    right.append(arr[i])
                else:
                    middle.append(arr[i])
    # рекурсивно применяем функцию для обоих групп и соединяем вместе
        return quickSort(left) + middle + quickSort(right)
    a = quickSort(a)
    print('-----------------------------------')
    print(a)

print('Функция линейного поиска - 1 ')
print('Функция бинарного поиска - 2 ')
print('Функция сортировки выбором - 3 ')
print('Функция сортировки включением - 4 ')
print('Функция сортировки пузырьком - 5 ')
print('Функция быстрой сортировки - 6 ')
f = int(input('Введите нужную функцию '))
n = int(input('Введите размер массива '))

if f == 1:
    print(linSearch(n))
elif f == 2:
    print(binSearch(n))
elif f == 3:
    sellect(n)
elif f == 4:
    insertion(n)
elif f == 5:
    bubl(n)
elif f == 6:
    fastSort(n)

input('Нажмите Enter для выхода\n')
#
#
#
#
#
