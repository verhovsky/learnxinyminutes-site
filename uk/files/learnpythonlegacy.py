# Однорядкові коментарі починаються з символу решітки.

""" Текст, що займає декілька рядків,
    може бути записаний з використанням 3 знаків " і 
    зазвичай використовується у якості
    вбудованої документації
"""

####################################################
## 1. Примітивні типи даних та оператори
####################################################

# У вас є числа
3  # => 3

# Математика працює досить передбачувано
1 + 1  # => 2
8 - 1  # => 7
10 * 2  # => 20
35 / 5  # => 7

# А ось з діленням все трохи складніше. Воно цілочисельне і результат
# автоматично округлюється у меншу сторону.
5 / 2  # => 2

# Аби правильно ділити, спершу варто дізнатися про числа
# з плаваючою комою.
2.0  # Це число з плаваючою комою
11.0 / 4.0  # => 2.75 ох... Так набагато краще

# Результат цілочисельного ділення округлюється у меншу сторону
# як для додатніх, так і для від'ємних чисел.
5 // 3  # => 1
5.0 // 3.0  # => 1.0  # Працює і для чисел з плаваючою комою
-5 // 3  # => -2
-5.0 // 3.0  # => -2.0

# Зверніть увагу, що ми також можемо імпортувати модуль для ділення, 
# див. розділ Модулі
# аби звичне ділення працювало при використанні лише '/'.
from __future__ import division

11 / 4  # => 2.75  ...звичне ділення
11 // 4  # => 2 ...цілочисельне ділення

# Залишок від ділення
7 % 3  # => 1

# Піднесення до степеня
2 ** 4  # => 16

# Приорітет операцій вказується дужками
(1 + 3) * 2  # => 8

# Логічні оператори
# Зверніть увагу: ключові слова «and» і «or» чутливі до регістру букв
True and False  # => False
False or True  # => True

# Завважте, що логічні оператори також використовуються і з цілими числами
0 and 2  # => 0
-5 or 0  # => -5
0 == False  # => True
2 == True  # => False
1 == True  # => True

# Для заперечення використовується not
not True  # => False
not False  # => True

# Рівність — це ==
1 == 1  # => True
2 == 1  # => False

# Нерівність — це !=
1 != 1  # => False
2 != 1  # => True

# Ще трохи порівнянь
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Порівняння можуть бути записані ланцюжком!
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# Рядки позначаються символом " або '
"Це рядок."
'Це теж рядок.'

# І рядки також можна додавати!
"Привіт " + "світ!" # => "Привіт світ!"
# Рядки можна додавати і без '+'
"Привіт " "світ!"  # => "Привіт світ!"

# ... або множити
"Привіт" * 3  # => "ПривітПривітПривіт"

# З рядком можна працювати як зі списком символів
"Це рядок"[0]  # => 'Ц'

# Ви можете дізнатися довжину рядка
len("Це рядок")  # => 8

# Символ % використовується для форматування рядків, наприклад:
"%s можуть бути %s" % ("рядки", "інтерпольовані")

# Новий спосіб форматування рядків — використання методу format.
# Це бажаний спосіб.
"{} є {}".format("Це", "заповнювач")
"{0} можуть бути {1}".format("рядки", "форматовані")
# Якщо ви не хочете рахувати, то можете скористатися ключовими словами.
"{name} хоче з'істи {food}".format(name="Боб", food="лазанью")

# None - це об'єкт
None  # => None

# Не використовуйте оператор рівності '=='' для порівняння 
# об'єктів з None. Використовуйте для цього «is»
"etc" is None  # => False
None is None  # => True

# Оператор 'is' перевіряє ідентичність об'єктів. Він не 
# дуже корисний при роботі з примітивними типами, проте 
# незамінний при роботі з об'єктами.

# None, 0 і порожні рядки/списки рівні False.
# Всі інші значення рівні True
bool(0)  # => False
bool("")  # => False


####################################################
## 2. Змінні та колекції
####################################################

# В Python є оператор print
print "Я Python. Приємно познайомитись!"  # => Я Python. Приємно познайомитись!

# Отримати дані з консолі просто
input_string_var = raw_input(
    "Введіть щось: ")  # Повертає дані у вигляді рядка
input_var = input("Введіть щось: ")  # Працює з даними як з кодом на python
# Застереження: будьте обережні при використанні методу input()

# Оголошувати змінні перед ініціалізацією не потрібно.
some_var = 5  # За угодою використовується нижній_регістр_з_підкресленнями
some_var  # => 5

# При спробі доступу до неініціалізованої змінної
# виникне виняткова ситуація.
# Див. розділ Потік управління, аби дізнатись про винятки більше.
some_other_var  # Помилка в імені

# if може використовуватися як вираз
# Такий запис еквівалентний тернарному оператору '?:' у мові С
"yahoo!" if 3 > 2 else 2  # => "yahoo!"

# Списки зберігають послідовності
li = []
# Можна одразу створити заповнений список
other_li = [4, 5, 6]

# Об'єкти додаються у кінець списку за допомогою методу append
li.append(1)  # li тепер дорівнює [1]
li.append(2)  # li тепер дорівнює [1, 2]
li.append(4)  # li тепер дорівнює [1, 2, 4]
li.append(3)  # li тепер дорівнює [1, 2, 4, 3]
# І видаляються з кінця методом pop
li.pop()  # => повертає 3 і li стає рівним [1, 2, 4]
# Повернемо елемент назад
li.append(3)  # li тепер знову дорівнює [1, 2, 4, 3]

# Поводьтесь зі списком як зі звичайним масивом
li[0]  # => 1
# Присвоюйте нові значення вже ініціалізованим індексам за допомогою =
li[0] = 42
li[0]  # => 42
li[0] = 1  # Зверніть увагу: повертаємось до попереднього значення
# Звертаємось до останнього елементу
li[-1]  # => 3

# Спроба вийти за границі масиву призводить до помилки в індексі
li[4]  # помилка в індексі

# Можна звертатися до діапазону, використовуючи так звані зрізи
# (Для тих, хто любить математику: це називається замкнуто-відкритий інтервал).
li[1:3]  # => [2, 4]
# Опускаємо початок
li[2:]  # => [4, 3]
# Опускаємо кінець
li[:3]  # => [1, 2, 4]
# Вибираємо кожен другий елемент
li[::2]  # => [1, 4]
# Перевертаємо список
li[::-1]  # => [3, 4, 2, 1]
# Використовуйте суміш вищеназваного для більш складних зрізів
# li[початок:кінець:крок]

# Видаляємо довільні елементи зі списку оператором del
del li[2]  # li тепер [1, 2, 3]

# Ви можете додавати списки
li + other_li  # => [1, 2, 3, 4, 5, 6]
# Зверніть увагу: значення li та other_li при цьому не змінились.

# Поєднувати списки можна за допомогою методу extend
li.extend(other_li)  # Тепер li дорівнює [1, 2, 3, 4, 5, 6]

# Видалити перше входження значення
li.remove(2)  # Тепер li дорівнює [1, 3, 4, 5, 6]
li.remove(2)  # Помилка значення, оскільки у списку li немає 2

# Вставити елемент за вказаним індексом
li.insert(1, 2)  # li знову дорівнює [1, 2, 3, 4, 5, 6]

# Отримати індекс першого знайденого елементу
li.index(2)  # => 1
li.index(7)  # Помилка значення, оскільки у списку li немає 7

# Перевірити елемент на входження у список можна оператором in
1 in li  # => True

# Довжина списку обчислюється за допомогою функції len
len(li)  # => 6

# Кортежі схожі на списки, лише незмінні
tup = (1, 2, 3)
tup[0]  # => 1
tup[0] = 3  # Виникає помилка типу

# Все те ж саме можна робити і з кортежами
len(tup)  # => 3
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tup[:2]  # => (1, 2)
2 in tup  # => True

# Ви можете розпаковувати кортежі (або списки) у змінні
a, b, c = (1, 2, 3)  # a == 1, b == 2 и c == 3
d, e, f = 4, 5, 6  # дужки можна опустити
# Кортежі створюються за замовчуванням, якщо дужки опущено
g = 4, 5, 6  # => (4, 5, 6)
# Дивіться, як легко обміняти значення двох змінних
e, d = d, e  # тепер d дорівнює 5, а e дорівнює 4

# Словники містять асоціативні масиви
empty_dict = {}
# Ось так описується попередньо заповнений словник
filled_dict = {"one": 1, "two": 2, "three": 3}

# Значення можна отримати так само, як і зі списку
filled_dict["one"]  # => 1

# Можна отримати всі ключі у виді списку за допомогою методу  keys
filled_dict.keys()  # => ["three", "two", "one"]
# Примітка: збереження порядку ключів у словників не гарантується
# Ваші результати можуть не співпадати з цими.

# Можна отримати і всі значення у вигляді списку, використовуйте метод values
filled_dict.values()  # => [3, 2, 1]
# Те ж зауваження щодо порядку ключів діє і тут

# Отримуйте всі пари ключ-значення у вигляді списку кортежів 
# за допомогою "items()"
filled_dict.items()  # => [("one", 1), ("two", 2), ("three", 3)]

# За допомогою оператору in можна перевіряти ключі на входження у словник
"one" in filled_dict # => True
1 in filled_dict  # => False

# Спроба отримати значення за неіснуючим ключем викине помилку ключа
filled_dict["four"]  # помилка ключа

# Аби уникнути цього, використовуйте метод get()
filled_dict.get("one")  # => 1
filled_dict.get("four")  # => None
# Метод get також приймає аргумент за замовчуванням, значення якого буде
# повернуто при відсутності вказаного ключа
filled_dict.get("one", 4)  # => 1
filled_dict.get("four", 4)  # => 4
# Зверніть увагу, що filled_dict.get("four") все ще => None
# (get не встановлює значення елементу словника)

# Присвоюйте значення ключам так само, як і в списках
filled_dict["four"] = 4  # тепер filled_dict["four"] => 4

# Метод setdefault() вставляє пару ключ-значення лише 
# за відсутності такого ключа
filled_dict.setdefault("five", 5)  #  filled_dict["five"] повертає 5
filled_dict.setdefault("five", 6)  #  filled_dict["five"] все ще повертає 5


# Множини містять... ну, загалом, множини
# (які схожі на списки, проте в них не може бути елементів, які повторюються)
empty_set = set()
# Ініціалізація множини набором значень
some_set = set([1,2,2,3,4])  # some_set тепер дорівнює set([1, 2, 3, 4])

# Порядок не гарантовано, хоча інколи множини виглядають відсортованими
another_set = set([4, 3, 2, 2, 1])  # another_set тепер set([1, 2, 3, 4])

# Починаючи з Python 2.7, ви можете використовувати {}, аби створити множину
filled_set = {1, 2, 2, 3, 4}  # => {1, 2, 3, 4}

# Додавання нових елементів у множину
filled_set.add(5)  # filled_set тепер дорівнює {1, 2, 3, 4, 5}

# Перетин множин: &
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}

# Об'єднання множин: |
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}

# Різниця множин: -
{1,2,3,4} - {2,3,5}  # => {1, 4}

# Симетрична різниця множин: ^
{1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}

# Перевіряємо чи множина зліва є надмножиною множини справа
{1, 2} >= {1, 2, 3}  # => False

# Перевіряємо чи множина зліва є підмножиною множини справа
{1, 2} <= {1, 2, 3}  # => True

# Перевірка на входження у множину: in
2 in filled_set  # => True
10 in filled_set  # => False


####################################################
## 3. Потік управління
####################################################

# Для початку створимо змінну
some_var = 5

# Так виглядає вираз if. Відступи у python дуже важливі!
# результат: «some_var менше, ніж 10»
if some_var > 10:
    print("some_var набагато більше, ніж 10.")
elif some_var < 10:  # Вираз elif є необов'язковим.
    print("some_var менше, ніж 10.")
else:  # Це теж необов'язково.
    print("some_var дорівнює 10.")


"""
Цикли For проходять по спискам

Результат:
    собака — це ссавець
    кішка — це ссавець
    миша — це ссавець
"""
for animal in ["собака", "кішка", "миша"]:
    # Можете використовувати оператор {0} для інтерполяції форматованих рядків
    print "{0} — це ссавець".format(animal) 
    
"""
"range(число)" повертає список чисел
від нуля до заданого числа
Друкує:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)
"""
"range(нижня_границя, верхня_границя)" повертає список чисел
від нижньої границі до верхньої
Друкує:
    4
    5
    6
    7
"""
for i in range(4, 8):
    print i

"""
Цикли while продовжуються до тих пір, поки вказана умова не стане хибною.
Друкує:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1  # Короткий запис для x = x + 1

# Обробляйте винятки блоками try/except

# Працює у Python 2.6 і вище:
try:
    # Аби створити виняток, використовується raise
    raise IndexError("Помилка у індексі!")
except IndexError as e:
    pass  # pass — оператор, який нічого не робить. Зазвичай тут відбувається
    # відновлення після помилки.
except (TypeError, NameError):
    pass  # Винятки можна обробляти групами, якщо потрібно.
else:  # Необов'язковий вираз. Має слідувати за останнім блоком except
    print("Все добре!")   # Виконається лише якщо не було ніяких винятків
finally:  # Виконується у будь-якому випадку
    print "Тут ми можемо звільнити ресурси"

# Замість try/finally для звільнення ресурсів 
# ви можете використовувати вираз with
with open("myfile.txt") as f:
    for line in f:
        print line


####################################################
## 4. Функції
####################################################

# Використовуйте def для створення нових функцій
def add(x, y):
    print "x дорівнює {0}, а y дорівнює {1}".format(x, y)
    return x + y  # Повертайте результат за допомогою ключового слова return


# Виклик функції з аргументами
add(5, 6)  # => друкує «x дорівнює 5, а y дорівнює 6» і повертає 11

# Інший спосіб виклику функції — виклик з іменованими аргументами
add(y=6, x=5)  # Іменовані аргументи можна вказувати у будь-якому порядку


# Ви можете визначити функцію, яка приймає змінну кількість аргументів,
# які будуть інтерпретовані як кортеж, за допомогою *
def varargs(*args):
    return args


varargs(1, 2, 3)  # => (1,2,3)


# А також можете визначити функцію, яка приймає змінне число
# іменованих аргументів, котрі будуть інтерпретовані як словник, за допомогою **
def keyword_args(**kwargs):
    return kwargs


# Давайте подивимось що з цього вийде
keyword_args(big="foot", loch="ness")  # => {"big": "foot", "loch": "ness"}

# Якщо хочете, можете використовувати обидва способи одночасно
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)


"""
all_the_args(1, 2, a=3, b=4) друкує:
    (1, 2)
    {"a": 3, "b": 4}
"""

# Коли викликаєте функції, то можете зробити навпаки!
# Використовуйте символ * аби розпакувати позиційні аргументи і 
# ** для іменованих аргументів
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)  # еквівалентно foo(1, 2, 3, 4)
all_the_args(**kwargs)  # еквівалентно foo(a=3, b=4)
all_the_args(*args, **kwargs)  # еквівалентно foo(1, 2, 3, 4, a=3, b=4)

# ви можете передавати довільне число позиційних або іменованих аргументів
# іншим функціям, які їх приймають, розпаковуючи за допомогою
# * або ** відповідно
def pass_all_the_args(*args, **kwargs):
    all_the_args(*args, **kwargs)
    print varargs(*args)
    print keyword_args(**kwargs)


# Область визначення функцій
x = 5


def set_x(num):
    # Локальна змінна x - не те ж саме, що глобальна змінна x
    x = num  # => 43
    print x  # => 43


def set_global_x(num):
    global x
    print x  # => 5
    x = num  # глобальна змінна x тепер дорівнює 6
    print x  # => 6


set_x(43)
set_global_x(6)

# В Python функції є об'єктами першого класу
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_10 = create_adder(10)
add_10(3)  # => 13

# Також є і анонімні функції
(lambda x: x > 2)(3)  # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1)  # => 5

# Присутні вбудовані функції вищого порядку
map(add_10, [1, 2, 3])  # => [11, 12, 13]
map(max, [1, 2, 3], [4, 2, 1])  # => [4, 2, 3]

filter(lambda x: x > 5, [3, 4, 5, 6, 7])  # => [6, 7]

# Для зручного відображення і фільтрації можна використовувати 
# включення у вигляді списків
[add_10(i) for i in [1, 2, 3]]  # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

# Ви також можете скористатися включеннями множин та словників
{x for x in 'abcddeef' if x in 'abc'}  # => {'a', 'b', 'c'}
{x: x ** 2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


####################################################
## 5. Класи
####################################################

# Аби отримати клас, ми наслідуємо object.
class Human(object):
    # Атрибут класу. Він розділяється всіма екземплярами цього класу.
    species = "H. sapiens"

    # Звичайний конструктор, буде викликаний при ініціалізації екземпляру класу
    # Зверніть увагу, що подвійне підкреслення на початку та наприкінці імені
    # використовується для позначення об'єктів та атрибутів,
    # які використовуються Python, але знаходяться у просторах імен, 
    # якими керує користувач. Не варто вигадувати для них імена самостійно.
    def __init__(self, name):
        # Присвоєння значення аргумента атрибуту класу name
        self.name = name

        # Ініціалізуємо властивість
        self.age = 0

    # Метод екземпляру. Всі методи приймають self у якості першого аргументу
    def say(self, msg):
       return "%s: %s" % (self.name, msg)

    # Методи класу розділяються між усіма екземплярами
    # Вони викликаються з вказанням викликаючого класу 
    # у якості першого аргументу
    @classmethod
    def get_species(cls):
        return cls.species

    # Статичний метод викликається без посилання на клас або екземпляр
    @staticmethod
    def grunt():
        return "*grunt*"

    # Властивість.
    # Перетворює метод age() в атрибут тільки для читання
    # з таким же ім'ям.
    @property
    def age(self):
        return self._age

    # Це дозволяє змінювати значення властивості
    @age.setter
    def age(self, age):
        self._age = age

    # Це дозволяє видаляти властивість
    @age.deleter
    def age(self):
        del self._age


# Створюємо екземпляр класу
i = Human(name="Данило")
print(i.say("привіт"))  # Друкує: «Данило: привіт»

j = Human("Меланка")
print(j.say("Привіт"))  # Друкує: «Меланка: привіт»

# Виклик методу класу
i.get_species()  # => "H. sapiens"

# Зміна розділюваного атрибуту
Human.species = "H. neanderthalensis"
i.get_species()  # => "H. neanderthalensis"
j.get_species()  # => "H. neanderthalensis"

# Виклик статичного методу
Human.grunt()  # => "*grunt*"

# Оновлюємо властивість
i.age = 42

# Отримуємо значення
i.age  # => 42

# Видаляємо властивість
del i.age
i.age  # => виникає помилка атрибуту

####################################################
## 6. Модулі
####################################################

# Ви можете імпортувати модулі
import math

print(math.sqrt(16))  # => 4.0

# Ви можете імпортувати окремі функції з модуля
from math import ceil, floor

print(ceil(3.7))  # => 4.0
print(floor(3.7))  # => 3.0

# Можете імпортувати всі функції модуля.
# Попередження: краще так не робіть
from math import *

# Можете скорочувати імена модулів
import math as m

math.sqrt(16) == m.sqrt(16)  # => True
# Ви також можете переконатися, що функції еквівалентні
from math import sqrt

math.sqrt == m.sqrt == sqrt  # => True

# Модулі в Python — це звичайні Python-файли. Ви
# можете писати свої модулі та імпортувати їх. Назва
# модуля співпадає з назвою файлу.

# Ви можете дізнатися, які функції та атрибути визначені
# в модулі
import math

dir(math)


# Якщо у вас є Python скрипт з назвою math.py у тій же папці, що
# і ваш поточний скрипт, то файл math.py
# може бути завантажено замість вбудованого у Python модуля.
# Так трапляється, оскільки локальна папка має перевагу
# над вбудованими у Python бібліотеками.

####################################################
## 7. Додатково
####################################################

# Генератори
# Генератор "генерує" значення тоді, коли вони запитуються, замість того, 
# щоб зберігати все одразу

# Метод нижче (*НЕ* генератор) подвоює всі значення і зберігає їх 
# в `double_arr`. При великих розмірах може знадобитися багато ресурсів!
def double_numbers(iterable):
    double_arr = []
    for i in iterable:
        double_arr.append(i + i)
    return double_arr


# Тут ми спочатку подвоюємо всі значення, потім повертаємо їх,
# аби перевірити умову
for value in double_numbers(range(1000000)):  # `test_non_generator`
    print value
    if value > 5:
        break


# Натомість ми можемо скористатися генератором, аби "згенерувати"
# подвійне значення, як тільки воно буде запитане
def double_numbers_generator(iterable):
    for i in iterable:
        yield i + i


# Той самий код, але вже з генератором, тепер дозволяє нам пройтися по
# значенням і подвоювати їх одне за одним якраз тоді, коли вони обробляються
# за нашою логікою, одне за одним. А як тільки ми бачимо, що value > 5, ми
# виходимо з циклу і більше не подвоюємо більшість значень, 
# які отримали на вхід (НАБАГАТО ШВИДШЕ!)
for value in double_numbers_generator(xrange(1000000)):  # `test_generator`
    print value
    if value > 5:
        break

# Між іншим: ви помітили використання `range` у `test_non_generator` і 
# `xrange` у `test_generator`?
# Як `double_numbers_generator` є версією-генератором `double_numbers`, так
# і `xrange` є аналогом `range`, але у вигляді генератора.
# `range` поверне нам масив з 1000000 значень
# `xrange`, у свою чергу, згенерує 1000000 значень для нас тоді, 
# коли ми їх запитуємо / будемо проходитись по ним.

# Аналогічно включенням у вигляді списків, ви можете створювати включення
# у вигляді генераторів.
values = (-x for x in [1, 2, 3, 4, 5])
for x in values:
    print(x)  # друкує -1 -2 -3 -4 -5

# Включення у вигляді генератора можна явно перетворити у список
values = (-x for x in [1, 2, 3, 4, 5])
gen_to_list = list(values)
print(gen_to_list)  # => [-1, -2, -3, -4, -5]

# Декоратори
# Декоратор – це функція вищого порядку, яка приймає та повертає функцію.
# Простий приклад використання – декоратор add_apples додає елемент 'Apple' в
# список fruits, який повертає цільова функція get_fruits.
def add_apples(func):
    def get_fruits():
        fruits = func()
        fruits.append('Apple')
        return fruits
    return get_fruits

@add_apples
def get_fruits():
    return ['Banana', 'Mango', 'Orange']

# Друкуємо список разом з елементом 'Apple', який знаходиться в ньому:
# Banana, Mango, Orange, Apple
print ', '.join(get_fruits())

# У цьому прикладі beg обертає say
# Beg викличе say. Якщо say_please дорівнюватиме True, то повідомлення,
# що повертається, буде змінено.
from functools import wraps


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Будь ласка! Я бідний :(")
        return msg

    return wrapper


@beg
def say(say_please=False):
    msg = "Ви можете купити мені пива?"
    return msg, say_please


print say()  # Ви можете купити мені пива?
print say(say_please=True)  # Ви можете купити мені пива? Будь ласка! Я бідний :(
