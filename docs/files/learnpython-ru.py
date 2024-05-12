
# Однострочные комментарии начинаются с символа решётки.

""" Многострочный текст может быть
    записан, используя 3 знака " и обычно используется
    в качестве встроенной документации
"""

####################################################
## 1. Примитивные типы данных и операторы
####################################################

# У вас есть числа
3  # => 3

# Математика работает вполне ожидаемо
1 + 1   # => 2
8 - 1   # => 7
10 * 2  # => 20
35 / 5  # => 7.0

# Результат целочисленного деления округляется в меньшую сторону
# как для положительных, так и для отрицательных чисел.
5 // 3       # => 1
-5 // 3      # => -2
5.0 // 3.0   # => 1.0  # работает и для чисел с плавающей запятой
-5.0 // 3.0  # => -2.0

# Результат деления возвращает число с плавающей запятой
10.0 / 3  # => 3.3333333333333335

# Остаток от деления
7 % 3  # => 1

# Возведение в степень
2**3  # => 8

# Приоритет операций указывается скобками
1 + 3 * 2    # => 7
(1 + 3) * 2  # => 8

# Булевы значения - примитивы (Обратите внимание на заглавную букву)
True   # => True
False  # => False

# Для отрицания используется ключевое слово not
not True   # => False
not False  # => True

# Булевы операторы
# Обратите внимание: ключевые слова "and" и "or" чувствительны к регистру букв
True and False  # => False
False or True   # => True

# True и False на самом деле 1 и 0, но с разными ключевыми словами
True + True  # => 2
True * 8     # => 8
False - 5    # => -5

# Операторы сравнения обращают внимание на числовое значение True и False
0 == False   # => True
1 == True    # => True
2 == True    # => False
-5 != False  # => True

# Использование булевых логических операторов на типах int превращает их в булевы значения, но возвращаются оригинальные значения
# Не путайте с bool(ints) и bitwise and/or (&,|)
bool(0)   # => False
bool(4)   # => True
bool(-6)  # => True
0 and 2   # => 0
-5 or 0   # => -5

# Равенство — это ==
1 == 1  # => True
2 == 1  # => False

# Неравенство — это !=
1 != 1  # => False
2 != 1  # => True

# Ещё немного сравнений
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Проверка, находится ли значение в диапазоне
1 < 2 and 2 < 3  # => True
2 < 3 and 3 < 2  # => False

# Сравнения могут быть записаны цепочкой
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# (is vs. ==) ключевое слово is проверяет, относятся ли две переменные к одному и тому же объекту, но == проверяет если указанные объекты имеют одинаковые значения.
a = [1, 2, 3, 4]  # a указывает на новый список, [1, 2, 3, 4]
b = a             # b указывает на то, что указывает a
b is a            # => True, a и b относятся к одному и тому же объекту
b == a            # => True, Объекты a и b равны
b = [1, 2, 3, 4]  # b указывает на новый список, [1, 2, 3, 4]
b is a            # => False, a и b не относятся к одному и тому же объекту
b == a            # => True, Объекты a и b равны

# Строки определяются символом " или '
"Это строка."
'Это тоже строка.'

# И строки тоже могут складываться!
"Привет " + "мир!"  # => "Привет мир!"

# Строки (но не переменные) могут быть объединены без использования '+'
"Привет " "мир!"  # => "Привет мир!"

# Со строкой можно работать, как со списком символов
"Привет мир!"[0]  # => 'П'

# Вы можете найти длину строки
len("Это строка")  # => 10

# Вы также можете форматировать, используя f-строки (в Python 3.6+)
name = "Рейко"
f"Она сказала, что ее зовут {name}."  # => "Она сказала, что ее зовут Рейко"
# Вы можете поместить любой оператор Python в фигурные скобки, и он будет выведен в строке.
f"{name} состоит из {len(name)} символов."  # => "Рэйко состоит из 5 символов."


# None является объектом
None  # => None

# Не используйте оператор равенства "==" для сравнения
# объектов с None. Используйте для этого "is"
"etc" is None  # => False
None is None   # => True

# None, 0 и пустые строки/списки/словари/кортежи приводятся к False.
# Все остальные значения равны True
bool(0)   # => False
bool("")  # => False
bool([])  # => False
bool({})  # => False
bool(())  # => False


####################################################
## 2. Переменные и Коллекции
####################################################

# В Python есть функция Print
print("Я Python. Приятно познакомиться!")  # => Я Python. Приятно познакомиться!

# По умолчанию, функция print() также выводит новую строку в конце.
# Используйте необязательный аргумент end, чтобы изменить конец последней строки.
print("Привет мир", end="!")  # => Привет мир!

# Простой способ получить входные данные из консоли
input_string_var = input("Введите данные: ")  # Возвращает данные в виде строки
# Примечание: в более ранних версиях Python метод input() назывался raw_input()

# Объявлять переменные перед инициализацией не нужно.
# По соглашению используется нижний_регистр_с_подчёркиваниями
some_var = 5
some_var  # => 5

# При попытке доступа к неинициализированной переменной выбрасывается исключение.
# Об исключениях см. раздел "Поток управления и итерируемые объекты".
some_unknown_var  # Выбрасывает ошибку NameError

# if можно использовать как выражение
# Эквивалент тернарного оператора '?:' в C
"да!" if 0 > 1 else "нет!"  # => "нет!"

# Списки хранят последовательности
li = []
# Можно сразу начать с заполненного списка
other_li = [4, 5, 6]

# Объекты добавляются в конец списка методом append()
li.append(1)  # [1]
li.append(2)  # [1, 2]
li.append(4)  # [1, 2, 4]
li.append(3)  # [1, 2, 4, 3]
# И удаляются с конца методом pop()
li.pop()      # => возвращает 3 и li становится равен [1, 2, 4]
# Положим элемент обратно
li.append(3)  # [1, 2, 4, 3].

# Обращайтесь со списком, как с обычным массивом
li[0]  # => 1

# Обратимся к последнему элементу
li[-1]  # => 3

# Попытка выйти за границы массива приведёт к ошибке индекса
li[4]  # Выбрасывает ошибку IndexError

# Можно обращаться к диапазону, используя так называемые срезы
# (Для тех, кто любит математику, это называется замкнуто-открытый интервал).
li[1:3]   # Вернуть список из индекса с 1 по 3 => [2, 4]
li[2:]    # Вернуть список, начиная с индекса 2 => [4, 3]
li[:3]    # Вернуть список с начала до индекса 3  => [1, 2, 4]
li[::2]   # Вернуть список, выбирая каждую вторую запись => [1, 4]
li[::-1]  # Вернуть список в обратном порядке => [3, 4, 2, 1]
# Используйте сочетания всего вышеназванного для выделения более сложных срезов
# li[начало:конец:шаг]

# Сделать однослойную глубокую копию, используя срезы
li2 = li[:]  # => li2 = [1, 2, 4, 3], но (li2 is li) вернет False.

# Удаляем произвольные элементы из списка оператором del
del li[2]  # [1, 2, 3]

# Удалить первое вхождение значения
li.remove(2)  # [1, 3]
li.remove(2)  # Выбрасывает ошибку ValueError поскольку 2 нет в списке

# Вставить элемент по определенному индексу
li.insert(1, 2)  # [1, 2, 3]

# Получить индекс первого найденного элемента, соответствующего аргументу
li.index(2)  # => 1
li.index(4)  # Выбрасывает ошибку ValueError поскольку 4 нет в списке

# Вы можете складывать, или, как ещё говорят, конкатенировать списки
# Обратите внимание: значения li и other_li при этом не изменились.
li + other_li  # => [1, 2, 3, 4, 5, 6]

# Объединять списки можно методом extend()
li.extend(other_li)  # Теперь li содержит [1, 2, 3, 4, 5, 6]

# Проверить элемент на наличие в списке можно оператором in
1 in li  # => True

# Длина списка вычисляется функцией len
len(li)  # => 6


# Кортежи похожи на списки, только неизменяемые
tup = (1, 2, 3)
tup[0]  # => 1
tup[0] = 3  # Выбрасывает ошибку TypeError

# Обратите внимание, что кортеж длины 1 должен иметь запятую после последнего элемента, но кортежи другой длины, даже 0, не должны.
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>

# Всё то же самое можно делать и с кортежами
len(tup)         # => 3
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tup[:2]          # => (1, 2)
2 in tup         # => True

# Вы можете распаковывать кортежи (или списки) в переменные
a, b, c = (1, 2, 3)  # a == 1, b == 2 и c == 3
# Вы также можете сделать расширенную распаковку
a, *b, c = (1, 2, 3, 4)  # a теперь 1, b теперь [2, 3] и c теперь 4
# Кортежи создаются по умолчанию, если опущены скобки
d, e, f = 4, 5, 6  # кортеж 4, 5, 6 распаковывается в переменные d, e и f
# соответственно, d = 4, e = 5 и f = 6
# Обратите внимание, как легко поменять местами значения двух переменных
e, d = d, e  # теперь d == 5, а e == 4


# Словари содержат ассоциативные массивы
empty_dict = {}
# Вот так описывается предзаполненный словарь
filled_dict = {"one": 1, "two": 2, "three": 3}

# Обратите внимание, что ключи для словарей должны быть неизменяемыми типами. Это
# сделано для того, чтобы ключ мог быть преобразован в хеш для быстрого поиска.
# Неизменяемые типы включают целые числа, числа с плавающей запятой, строки, 
# кортежи.
invalid_dict = {[1,2,3]: "123"}  # => Выбрасывает ошибку TypeError: unhashable type: 'list'
valid_dict = {(1,2,3):[1,2,3]}   # Однако значения могут быть любого типа.

# Поиск значений с помощью []
filled_dict["one"]  # => 1

# Все ключи в виде списка получаются с помощью метода keys(). Его вызов нужно
# обернуть в list(), так как обратно мы получаем итерируемый объект, о которых
# поговорим позднее. Примечание - для Python версии <3.7, порядок словарных
# ключей не гарантируется. Ваши результаты могут не точно соответствовать
# приведенному ниже примеру. Однако, начиная с Python 3.7 элементы в словаре
# сохраняют порядок, в котором они вставляются в словарь.
list(filled_dict.keys())  # => ["three", "two", "one"] в Python <3.7
list(filled_dict.keys())  # => ["one", "two", "three"] в Python 3.7+


# Все значения в виде списка можно получить с помощью values().
# И снова нам нужно обернуть вызов в list(), чтобы превратить
# итерируемый объект в список.
# То же самое замечание насчёт порядка ключей справедливо и здесь
list(filled_dict.values())  # => [3, 2, 1] в Python <3.7
list(filled_dict.values())  # => [1, 2, 3] в Python 3.7+

# При помощи ключевого слова in можно проверять наличие ключей в словаре
"one" in filled_dict  # => True
1 in filled_dict      # => False

# Попытка получить значение по несуществующему ключу выбросит ошибку KeyError
filled_dict["four"]  # Выбрасывает ошибку KeyError

# Чтобы избежать этого, используйте метод get()
filled_dict.get("one")      # => 1
filled_dict.get("four")     # => None
# Метод get поддерживает аргумент по умолчанию, когда значение отсутствует
filled_dict.get("one", 4)   # => 1
filled_dict.get("four", 4)  # => 4

# Метод setdefault() вставляет пару ключ-значение, только если такого ключа нет
filled_dict.setdefault("five", 5)  # filled_dict["five"] возвращает 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] по-прежнему возвращает 5

# Добавление элементов в словарь
filled_dict.update({"four":4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4         # Другой способ добавления элементов

# Удаляйте ключи из словаря с помощью ключевого слова del
del filled_dict["one"]  # Удаляет ключ "one" из словаря

# В Python 3.5+ вы также можете использовать дополнительные параметры распаковки
{'a': 1, **{'b': 2}}  # => {'a': 1, 'b': 2}
{'a': 1, **{'a': 2}}  # => {'a': 2}


# Множества содержат... ну, в общем, множества
empty_set = set()
# Инициализация множества набором значений.
# Да, оно выглядит примерно как словарь. Ну извините, так уж вышло.
filled_set = {1, 2, 2, 3, 4}  # => {1, 2, 3, 4}

# Как и ключи словаря, элементы множества должны быть неизменяемыми.
invalid_set = {[1], 1}  # => Выбрасывает ошибку TypeError: unhashable type: 'list'
valid_set = {(1,), 1}

# Множеству можно назначать новую переменную
filled_set = some_set
filled_set.add(5)  # {1, 2, 3, 4, 5}
# В множествах нет повторяющихся элементов
filled_set.add(5)  # {1, 2, 3, 4, 5}

# Пересечение множеств: &
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}

# Объединение множеств: |
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}

# Разность множеств: -
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}

# Симметричная разница: ^
{1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}

# Проверить, является ли множество слева надмножеством множества справа
{1, 2} >= {1, 2, 3}  # => False

# Проверить, является ли множество слева подмножеством множества справа
{1, 2} <= {1, 2, 3}  # => True

# Проверка на наличие в множестве: in
2 in filled_set   # => True
10 in filled_set  # => False

# Сделать однослойную глубокую копию
filled_set = some_set.copy()  # {1, 2, 3, 4, 5}
filled_set is some_set        # => False


####################################################
## 3. Поток управления и итерируемые объекты
####################################################

# Для начала создадим переменную
some_var = 5

# Так выглядит выражение if. Отступы в python очень важны!
# Конвенция заключается в использовании четырех пробелов, а не табуляции.
# Pезультат: "some_var меньше, чем 10"
if some_var > 10:
    print("some_var точно больше, чем 10.")
elif some_var < 10:  # Выражение elif необязательно.
    print("some_var меньше, чем 10.")
else:                # Это тоже необязательно.
    print("some_var равно 10.")


"""
Циклы For проходят по спискам.
Выводит:
    собака — это млекопитающее
    кошка — это млекопитающее
    мышь — это млекопитающее
"""
for animal in ["собака", "кошка", "мышь"]:
    # Можете использовать format() для интерполяции форматированных строк
    print("{} — это млекопитающее".format(animal))

"""
"range(число)" возвращает список чисел от нуля до заданного числа.
Выводит:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
"range(начало, конец)" возвращает список чисел от начального числа 
к конечному, не включая конечное.
Выводит:
    4
    5
    6
    7
"""
for i in range(4, 8):
    print(i)

"""
"range(начало, конец, шаг)" возвращает список чисел от начального 
числа к конечному, увеличивая шаг за шагом.
Если шаг не указан, значение по умолчанию - 1.
Выводит:
    4
    6
"""
for i in range(4, 8, 2):
    print(i)

"""
Можно перебрать список и получить индекс и значение каждого элемента в списке
Выводит:
    0 собака
    1 кошка
    2 мышь
"""
animals = ["собака", "кошка", "мышь"]
for i, value in enumerate(animals):
    print(i, value)

"""
Циклы while продолжаются до тех пор, пока указанное условие не станет ложным.
Выводит:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1  # Краткая запись для x = x + 1


# Обрабатывайте исключения блоками try/except
try:
    # Чтобы выбросить ошибку, используется raise
    raise IndexError("Это ошибка индекса")
except IndexError as e:
    pass                  # pass — это просто отсутствие оператора. Обычно здесь происходит восстановление после ошибки.
except (TypeError, NameError):
    pass                  # Можно обработать больше одного исключения.
else:                     # Необязательно. Добавляется за последним except.
    print("Всё хорошо!")  # Выполнится, только если не было никаких исключений.
finally:                  # Необязательно. Выполнить при любых обстоятельствах.
    print("Мы можем очистить ресурсы здесь")

# Вместо try/finally чтобы очистить ресурсы, можно использовать оператор with
with open("myfile.txt") as f:
    for line in f:
        print(line)

# Запись в файл
contents = {"aa": 12, "bb": 21}
with open("myfile1.txt", "w+") as file:
    file.write(str(contents))         # Записывает строку в файл

with open("myfile2.txt", "w+") as file:
    file.write(json.dumps(contents))  # Записывает объект в файл

# Чтение из файла
with open("myfile1.txt", "r+") as file:
    contents = file.read()            # Читает строку из файла
print(contents)                       # => '{"aa": 12, "bb": 21}'

with open("myfile2.txt", "r") as file:
    contents = json.load(file)        # Читает объект json из файла
print(contents)                       # => {"aa": 12, "bb": 21}


# Python предоставляет фундаментальную абстракцию,
# которая называется итерируемым объектом (Iterable).
# Итерируемый объект — это объект, который воспринимается как последовательность.
# Объект, который возвратила функция range() — итерируемый.

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)  # => dict_keys(['one', 'two', 'three']). Это объект, реализующий интерфейс Iterable

# Мы можем проходить по нему циклом.
for i in our_iterable:
    print(i)  # Выводит one, two, three

# Но мы не можем обращаться к элементу по индексу.
our_iterable[1]  # Выбрасывает ошибку TypeError

# Итерируемый объект знает, как создавать итератор.
our_iterator = iter(our_iterable)

# Итератор может запоминать состояние при проходе по объекту.
# Мы получаем следующий объект, вызывая функцию next().
next(our_iterator)  # => "one"

# Он сохраняет состояние при вызове next().
next(our_iterator)  # => "two"
next(our_iterator)  # => "three"

# Возвратив все данные, итератор выбрасывает исключение StopIteration
next(our_iterator)  # Выбрасывает исключение StopIteration

# Мы можем проходить по нему циклом.
our_iterator = iter(our_iterable)
for i in our_iterator:
    print(i)  # Выводит one, two, three

# Вы можете получить сразу все элементы итератора, вызвав на нём функцию list().
list(our_iterable)  # => Возвращает ["one", "two", "three"]
list(our_iterator)  # => Возвращает [] потому что состояние сохраняется


####################################################
## 4. Функции
####################################################

# Используйте def для создания новых функций
def add(x, y):
    print("x равен %s, а y равен %s" % (x, y))
    return x + y  # Возвращайте результат с помощью ключевого слова return

# Вызов функции с аргументами
add(5, 6)  # => Выводит "x равен 5, а y равен 6" и возвращает 11

# Другой способ вызова функции — вызов с именованными аргументами
add(y=6, x=5)  # Именованные аргументы можно указывать в любом порядке.

# Вы можете определить функцию, принимающую переменное число аргументов
def varargs(*args):
    return args

varargs(1, 2, 3)  # => (1,2,3)


# А также можете определить функцию, принимающую переменное число
# именованных аргументов
def keyword_args(**kwargs):
    return kwargs

# Вызовем эту функцию и посмотрим, что из этого получится
keyword_args(big="foot", loch="ness")  # => {"big": "foot", "loch": "ness"}

# Если хотите, можете использовать оба способа одновременно
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) выводит:
    (1, 2)
    {"a": 3, "b": 4}
"""

# Вызывая функции, можете сделать наоборот!
# Используйте символ * для распаковки кортежей и ** для распаковки словарей
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)            # эквивалентно all_the_args(1, 2, 3, 4)
all_the_args(**kwargs)         # эквивалентно all_the_args(a=3, b=4)
all_the_args(*args, **kwargs)  # эквивалентно all_the_args(1, 2, 3, 4, a=3, b=4)

# Возврат нескольких значений (с назначением кортежей)
def swap(x, y):
    return y, x  # Возвращает несколько значений в виде кортежа без скобок.
                 # (Примечание: скобки исключены, но могут быть включены)

x = 1
y = 2
x, y = swap(x, y)     # => x = 2, y = 1
# (x, y) = swap(x,y)  # Снова, скобки были исключены, но могут быть включены.

# Область определения функций
x = 5

def set_x(num):
    # Локальная переменная x — это не то же самое, что глобальная переменная x
    x = num   # => 43
    print(x)  # => 43

def set_global_x(num):
    global x
    print(x)  # => 5
    x = num   # Глобальная переменная x теперь равна 6
    print(x)  # => 6

set_x(43)
set_global_x(6)

# Python имеет функции первого класса
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)  # => 13

# Также есть и анонимные функции
(lambda x: x > 2)(3)                  # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1)  # => 5

# Есть встроенные функции высшего порядка
list(map(add_10, [1, 2, 3]))          # => [11, 12, 13]
list(map(max, [1, 2, 3], [4, 2, 1]))  # => [4, 2, 3]

list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # => [6, 7]

# Для удобного отображения и фильтрации можно использовать списочные интерпретации
# Интерпретация списка сохраняет вывод в виде списка, который сам может быть вложенным списком
[add_10(i) for i in [1, 2, 3]]         # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

# Вы также можете создавать интерпретации множеств и словарей.
{x for x in 'abcddeef' if x not in 'abc'}  # => {'d', 'e', 'f'}
{x: x**2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


####################################################
## 5. Модули
####################################################

# Вы можете импортировать модули
import math
print(math.sqrt(16))  # => 4.0

# Вы можете получить определенные функции из модуля
from math import ceil, floor
print(ceil(3.7))   # => 4.0
print(floor(3.7))  # => 3.0

# Вы можете импортировать все функции из модуля.
# Предупреждение: это не рекомендуется
from math import *

# Вы можете сократить имена модулей
import math as m
math.sqrt(16) == m.sqrt(16)  # => True

# Модули Python - это обычные файлы Python. Вы
# можете писать свои собственные и импортировать их. Имя
# модуля совпадает с именем файла.

# Вы можете узнать, какие функции и атрибуты
# определены в модуле.
import math
dir(math)

# Если у вас есть скрипт Python с именем math.py в той же папке,
# что и ваш текущий скрипт, файл math.py будет
# будет загружен вместо встроенного модуля Python.
# Это происходит потому, что локальная папка имеет приоритет
# над встроенными библиотеками Python.


####################################################
## 6. Классы
####################################################

# Мы используем оператор class для создания класса
class Human:

    # Атрибут класса. Он используется всеми экземплярами этого класса
    species = "Гомосапиенс"

    # Обычный конструктор, вызывается при инициализации экземпляра класса
    # Обратите внимание, что двойное подчёркивание в начале и в конце имени
    # означает объекты и атрибуты, которые используются Python, но находятся
    # в пространствах имён, управляемых пользователем.
    # Методы (или объекты или атрибуты), например:
    # __init__, __str__, __repr__ и т. д. называются специальными методами.
    # Не придумывайте им имена самостоятельно.
    def __init__(self, name):
        # Присваивание значения аргумента атрибуту
        self.name = name

        # Инициализация свойства
        self._age = 0

    # Метод экземпляра. Все методы принимают self в качестве первого аргумента
    def say(self, msg):
        return "{name}: {message}".format(name=self.name, message=msg)

    # Другой метод экземпляра
    def sing(self):
        return 'йо... йо... проверка микрофона... раз, два... раз, два...'

    # Метод класса разделяется между всеми экземплярами
    # Они вызываются с указыванием вызывающего класса в качестве первого аргумента
    @classmethod
    def get_species(cls):
        return cls.species

    # Статический метод вызывается без ссылки на класс или экземпляр
    @staticmethod
    def grunt():
        return "*grunt*"

    # property похоже на геттер.
    # Оно превращает метод age() в одноименный атрибут только для чтения.
    # Однако нет необходимости писать тривиальные геттеры и сеттеры в Python.
    @property
    def age(self):
        return self._age

    # Это позволяет установить свойство
    @age.setter
    def age(self, age):
        self._age = age

    # Это позволяет удалить свойство
    @age.deleter
    def age(self):
        del self._age


# Когда интерпретатор Python читает исходный файл, он выполняет весь его код.
# Проверка __name__ гарантирует, что этот блок кода выполняется только тогда, когда
# этот модуль - это основная программа.
if __name__ == '__main__':
    # Инициализация экземпляра класса
    i = Human(name="Иван")
    i.say("привет")                 # Выводит: "Иван: привет"
    j = Human("Пётр")
    j.say("привет")                 # Выводит: "Пётр: привет"
    # i и j являются экземплярами типа Human, или другими словами: они являются объектами Human

    # Вызов метода класса
    i.say(i.get_species())          # "Иван: Гомосапиенс"
    # Изменение разделяемого атрибута
    Human.species = "Неандертальец"
    i.say(i.get_species())          # => "Иван: Неандертальец"
    j.say(j.get_species())          # => "Пётр: Неандертальец"

    # Вызов статического метода
    print(Human.grunt())            # => "*grunt*"

    # Невозможно вызвать статический метод с экземпляром объекта
    # потому что i.grunt() автоматически поместит "self" (объект i) в качестве аргумента
    print(i.grunt())                # => TypeError: grunt() takes 0 positional arguments but 1 was given

    # Обновить свойство для этого экземпляра
    i.age = 42
    # Получить свойство
    i.say(i.age)                    # => "Иван: 42"
    j.say(j.age)                    # => "Пётр: 0"
    # Удалить свойство
    del i.age
    # i.age                         # => это выбрасило бы ошибку AttributeError


####################################################
## 6.1 Наследование
####################################################

# Наследование позволяет определять новые дочерние классы, которые наследуют методы и
# переменные от своего родительского класса.

# Используя класс Human, определенный выше как базовый или родительский класс, мы можем
# определить дочерний класс Superhero, который наследует переменные класса, такие как
# "species", "name" и "age", а также методы, такие как "sing" и "grunt" из класса Human,
# но также может иметь свои уникальные свойства.

# Чтобы воспользоваться преимуществами модульности по файлам, вы можете поместить
# вышеперечисленные классы в их собственные файлы, например, human.py

# Чтобы импортировать функции из других файлов, используйте следующий формат
# from "имя-файла-без-расширения" import "функция-или-класс"

from human import Human


# Укажите родительский класс(ы) как параметры определения класса
class Superhero(Human):

    # Если дочерний класс должен наследовать все определения родителя без каких-либо
    # изменений, вы можете просто использовать ключевое слово pass (и ничего больше),
    # но в этом случае оно закомментировано, чтобы разрешить уникальный дочерний класс:
    # pass

    # Дочерние классы могут переопределять атрибуты своих родителей
    species = 'Сверхчеловек'

    # Дочерние классы автоматически наследуют конструктор родительского класса, включая
    # его аргументы, но также могут определять дополнительные аргументы или определения
    # и переопределять его методы, такие как конструктор класса.
    # Этот конструктор наследует аргумент "name" от класса "Human"
    # и добавляет аргументы "superpower" и "movie":
    def __init__(self, name, movie=False,
                 superpowers=["сверхсила", "пуленепробиваемость"]):

        # добавить дополнительные атрибуты класса:
        self.fictional = True
        self.movie = movie
        # помните об изменяемых значениях по умолчанию,
        # поскольку значения по умолчанию являются общими
        self.superpowers = superpowers

        # Функция "super" позволяет вам получить доступ к методам родительского класса,
        # которые переопределяются дочерним, в данном случае, методом __init__.
        # Это вызывает конструктор родительского класса:
        super().__init__(name)

    # переопределить метод sing
    def sing(self):
        return 'Бам, бам, БАМ!'

    # добавить дополнительный метод экземпляра
    def boast(self):
        for power in self.superpowers:
            print("Я обладаю силой '{pow}'!".format(pow=power))


if __name__ == '__main__':
    sup = Superhero(name="Тик")

    # Проверка типа экземпляра
    if isinstance(sup, Human):
        print('Я человек')
    if type(sup) is Superhero:
        print('Я супергерой')

    # Получить порядок поиска разрешения метода (MRO),
    # используемый как getattr(), так и super()
    # Этот атрибут является динамическим и может быть обновлен
    print(Superhero.__mro__)    # => (<class '__main__.Superhero'>,
                                # => <class 'human.Human'>, <class 'object'>)

    # Вызывает родительский метод, но использует свой собственный атрибут класса
    print(sup.get_species())    # => Сверхчеловек

    # Вызов переопределенного метода
    print(sup.sing())           # => Бам, бам, БАМ!

    # Вызывает метод из Human
    sup.say('Ложка')            # => Тик: Ложка

    # Метод вызова, существующий только в Superhero
    sup.boast()                 # => Я обладаю силой 'сверхсила'!
                                # => Я обладаю силой 'пуленепробиваемость'!

    # Атрибут унаследованного класса
    sup.age = 31
    print(sup.age)              # => 31

    # Атрибут, который существует только в Superhero
    print('Достоин ли я Оскара? ' + str(sup.movie))


####################################################
## 6.2 Множественное наследование
####################################################

# Eще одно определение класса
# bat.py
class Bat:

    species = 'Летучая мышь'

    def __init__(self, can_fly=True):
        self.fly = can_fly

    # В этом классе также есть метод say
    def say(self, msg):
        msg = '... ... ...'
        return msg

    # И свой метод тоже
    def sonar(self):
        return '))) ... ((('

if __name__ == '__main__':
    b = Bat()
    print(b.say('привет'))
    print(b.fly)


# И еще одно определение класса, унаследованное от Superhero и Bat
# superhero.py
from superhero import Superhero
from bat import Bat

# Определите Batman как дочерний класс, унаследованный от Superhero и Bat
class Batman(Superhero, Bat):

    def __init__(self, *args, **kwargs):
        # Обычно для наследования атрибутов необходимо вызывать super:
        # super(Batman, self).__init__(*args, **kwargs)
        # Однако здесь мы имеем дело с множественным наследованием, а super()
        # работает только со следующим базовым классом в списке MRO.
        # Поэтому вместо этого мы вызываем __init__ для всех родителей.
        # Использование *args и **kwargs обеспечивает чистый способ передачи
        # аргументов, когда каждый родитель "очищает слой луковицы".
        Superhero.__init__(self, 'анонимный', movie=True,
                           superpowers=['Богатый'], *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        # переопределить значение атрибута name
        self.name = 'Грустный Бен Аффлек'

    def sing(self):
        return 'на на на на на бэтмен!'


if __name__ == '__main__':
    sup = Batman()

    # Получить порядок поиска разрешения метода (MRO),
    # используемый как getattr(), так и super()
    # Этот атрибут является динамическим и может быть обновлен
    print(Batman.__mro__)       # => (<class '__main__.Batman'>,
                                # => <class 'superhero.Superhero'>,
                                # => <class 'human.Human'>,
                                # => <class 'bat.Bat'>, <class 'object'>)

    # Вызывает родительский метод, но использует свой собственный атрибут класса
    print(sup.get_species())    # => Сверхчеловек

    # Вызов переопределенного метода
    print(sup.sing())           # => на на на на на бэтмен!

    # Вызывает метод из Human, потому что порядок наследования имеет значение
    sup.say('Я согласен')          # => Грустный Бен Аффлек: Я согласен

    # Вызов метода, существующий только во втором родителе
    print(sup.sonar())          # => ))) ... (((

    # Атрибут унаследованного класса
    sup.age = 100
    print(sup.age)              # => 100

    # Унаследованный атрибут от второго родителя,
    # значение по умолчанию которого было переопределено.
    print('Могу ли я летать? ' + str(sup.fly))  # => Могу ли я летать? False


####################################################
## 7. Дополнительно
####################################################

# Генераторы помогут выполнить ленивые вычисления
def double_numbers(iterable):
    for i in iterable:
        yield i + i

# Генераторы эффективны с точки зрения памяти, потому что они загружают только данные,
# необходимые для обработки следующего значения в итерации.
# Это позволяет им выполнять операции с недопустимо большими диапазонами значений.
# ПРИМЕЧАНИЕ: "range" заменяет "xrange" в Python 3.
for i in double_numbers(range(1, 900000000)):  # "range" - генератор.
    print(i)
    if i >= 30:
        break

# Так же, как вы можете создать интерпретации списков, вы можете создать и
# интерпретации генераторов.
values = (-x for x in [1,2,3,4,5])
for x in values:
    print(x)  # Выводит -1 -2 -3 -4 -5

# Вы также можете преобразовать интерпретацию генератора непосредственно в список.
values = (-x for x in [1,2,3,4,5])
gen_to_list = list(values)
print(gen_to_list)  # => [-1, -2, -3, -4, -5]


# Декораторы
# В этом примере "beg" оборачивает "say".
# Если say_please равно True, он изменит возвращаемое сообщение.
from functools import wraps


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Пожалуйста! У меня нет денег :(")
        return msg

    return wrapper


@beg
def say(say_please=False):
    msg = "Вы не купите мне пива?"
    return msg, say_please


print(say())                 # Вы не купите мне пива?
print(say(say_please=True))  # Вы не купите мне пива? Пожалуйста! У меня нет денег :(

