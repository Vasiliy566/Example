# Задачки

## 1. if-else

### Гороскоп

Китайский гороскоп делит время на 12-летние циклы, и каждому году
соответствует конкретное животное. После окончания одного цикла начинается другой, то есть
2012 год снова символизирует дракона

| Год  | Животное | Год  | Животное |
|:------|:---------:|:-----:|-------:|
| 2000 | Дракон   | 2006 | Собака|
| 2001 | Змея     | 2007 | Свинья|
| 2002 | Лошадь   | 2008 | Крыса|
| 2003 | Коза     | 2009 | Бык|
| 2004 | Обезьяна | 2010 | Тигр |
| 2005 | Петух    | 2011 | Кролик|

Программа принимает на вход одно число - год.

### Шахматы

Клетки на шахматной доске идентифицируются буквой и цифрой. Буква
определяет положение клетки по горизонтали, а цифра – по вертикали,

Ваша программа должна запрашивать у пользователя координаты клетки. 
Используйте условное выражение для определения того, с какой клетки – белой или черной – начинается столбец. 
Затем при помощи обычной арифметики необходимо определить цвет конкретной клетки. Напри-
мер, если пользователь ввел a1, программа должна определить, что клетка
с этими координатами черная. Если d5 – белая. Проверку на ошибочность
ввода координат клетки выполнять не нужно.

## 2. Циклы

### Полиндромы

Помимо слов, существуют целые фразы, являющиеся палиндромами, если
не обращать внимания на пробелы. Вот лишь несколько примеров на английском:
«go dog», «flee to me remote elf» and «some men interpret nine
memos». Русские варианты есть следующие: «А кобыле цена дана, да не
целы бока», «А Луна канула» и другие. Напишите программу, определяющую,
является ли введенная строка полиндромом.

### Двоичные числа

Напишите программу, которая будет преобразовывать двоичные зна-
чения (по основанию 2) в десятичные (по основанию 10). Пользователь
должен ввести число в двоичном виде как строку, а программа – преоб-
разовать его посимвольно в десятичный вид и вывести на экран с соот-
ветствующим сообщением.

### Монетка

Какое минимальное количество раз вы должны подбросить монетку, что-
бы три раза подряд выпал либо орел, либо решка? А какое максимальное
количество попыток может для этого понадобиться? А в среднем? В дан-
ном упражнении мы выясним это, создав симулятор подбрасывания вир-
туальной монетки.
Напишите программу, использующую для подброса монетки генера-
тор случайных чисел Python. Монетка при этом должна быть правильной
формы, что означает равную вероятность выпадения орла и решки. Под-
брасывать монетку необходимо до тех пор, пока три раза подряд не вы-
падет одно значение, вне зависимости от того, орел это будет или решка.
Выводите на экран букву О всякий раз, когда выпадает орел, и Р – когда
выпадает решка. При этом для одной симуляции бросков все выпавшие
значения необходимо размещать на одной строке. Также необходимо из-
вестить пользователя о том, сколько попыток потребовалось, чтобы полу-
чить нужный результат.
Программа должна выполнить десять симуляций и в конце представить
среднее количество подбрасываний монетки, требуемое для достижения
нужного нам результата. Пример вывода программы показан ниже:

### Наибольший общий делитель

Наибольший общий делитель двух положительных чисел представляет
собой наибольшее число, на которое без остатка делятся оба числа. Су-
ществует несколько алгоритмов, позволяющих определить наибольший
общий делитель двух чисел, включая следующий.
Инициализируйте переменную d меньшим из чисел n и m
Пока n или m не делятся на d без остатка, выполнять
Уменьшить d на единицу
Выведите на экран d, это и есть наибольший общий делитель для n и m
Напишите программу, запрашивающую у пользователя два положи-
тельных целых числа и выводящую для них наибольший общий делитель.

```
О Р Р Р (попыток: 4)
О О Р Р О Р О Р Р О О Р О Р Р О Р Р Р (попыток: 19)
Р Р Р (попыток: 3)
Р О О О (попыток: 4)
О О О (попыток: 3)
Р О Р Р О Р О О Р Р О О Р О Р О О О (попыток: 18)
О Р Р О О О (попыток: 6)
Р О Р Р Р (попыток: 5)
Р Р О Р Р О Р О Р О О О (попыток: 12)
Р О Р Р Р (попыток: 5)
Среднее количество попыток: 7,9.
```

## 3. Функции

### Простые числа 1

Простое число представляет собой число, большее единицы, которое без
остатка делится лишь на само себя и единицу. Напишите функцию для
определения того, является ли введенное число простым. Возвращаемое
значение должно быть либо True, либо False. В основной программе, как
и ожидается, пользователь должен ввести целое число и получить ответ
о том, является ли оно простым. Убедитесь, что основная программа не
будет запускаться, если файл импортирован в другой файл в качестве
модуля.

### Простые числа 2

В данном упражнении вам нужно написать функцию с именем nextPrime,
которая находит и возвращает первое простое число, большее введенного
числа n. Само число n должно передаваться в функцию в качестве един-
ственного параметра. В основной программе запросите у пользователя
это значение и выведите на экран первое простое число, большее за-
данного. Для решения этой задачи импортируйте функцию, созданную
в прошлом упражнении.

### Генератор паролей

Напишите функцию, которая будет генерировать случайный пароль. В па-
роле должно быть от 7 до 10 символов, при этом каждый символ должен
быть случайным образом выбран из диапазона от 33 до 126 в таблице
ASCII. Ваша функция не должна принимать на вход параметры, а возвра-
щать будет сгенерированный пароль. В основной программе вы должны
просто вывести созданный случайным образом пароль. Программа долж-
на запускаться только в том случае, если она не импортирована в виде
модуля в другой файл.

### Мокращение дробей

Напишите функцию, принимающую на вход два целочисленных пара-
метра, представляющих числитель и знаменатель дроби. В теле функции
должно выполняться максимально возможное сокращение дроби, а полу-
ченные в итоге числитель и знаменатель должны быть возвращены исход-
ной программе. Например, если на вход функции передать числа 6 и 63,
числитель и знаменатель итоговой дроби должны быть 2 и 21. В основной
программе нужно запросить у пользователя числитель и знаменатель ис-
ходной дроби, передать их в функцию и вывести на экран результат.
Используйте функцию из упражнения `Наибольший общий делитель`

## 4. Списки

### Собственные делители

Собственным делителем числа называется всякий его делитель, отличный
от самого числа. Напишите функцию, которая будет возвращать список
всех собственных делителей заданного числа. Само это число должно
передаваться в функцию в виде единственного аргумента. Результатом
функции будет перечень собственных делителей числа, собранных в спи-
сок. Основная программа должна демонстрировать работу функции, за-
прашивая у пользователя число и выводя на экран список его собственных
делителей. Программа должна запускаться только в том случае, если она
не импортирована в виде модуля в другой файл

### Совершенные числа

Целое число n называется совершенным, если сумма всех его собственных
делителей равна самому числу n. Например, 28 – это совершенное число,
поскольку его собственными делителями являются 1, 2, 4, 7 и 14, а 1 + 2 + 4 + 7 + 14 = 28.
Напишите функцию для определения того, является ли заданное число
совершенным. Функция будет принимать на вход единственный пара-
метр и возвращать True, если он представляет собой совершенное число,
и False – если нет. Разработайте небольшую программу, которая будет
использовать функцию для идентификации и вывода на экран всех со-
вершенных чисел в диапазоне от 1 до 10 000. При решении этой задачи
импортируйте функцию, написанную в прошлой задаче.

### Простые числа

Решето Эратосфена – алгоритм, изобретенный более 2000 лет назад и слу-
жащий для нахождения всех простых чисел от 2 до некоторого целого
числа n. Описание этого алгоритма приведено ниже.
Выписываем все целые числа от 0 до заданной границы
Вычеркиваем 0 и 1 как непростые числа
Устанавливаем значение переменной p, равное 2
Пока p меньше указанного числа, делать
Вычеркиваем все числа, кратные p, но не его само
Устанавливаем значение p, равное следующему невычеркнутому числу
Выводим все числа, оставшиеся незачеркнутыми
Ценность данного алгоритма заключается в том, что на бумаге очень
легко вычеркнуть все числа, кратные определенному. Для компьютера
это также не самая сложная задача – с этим может прекрасно справиться

## 5. Словари

### Эрудит

В известной игре Эрудит (Scrabble™) каждой букве соответствует опреде-
ленное количество очков. Общая сумма очков, которую получает игрок,
составивший это слово, складывается из очков за каждую букву, входящую
в его состав. Чем более употребимой является буква в языке, тем меньше
очков начисляется за ее использование. В табл. 6.5 приведены все соот-
ветствия букв и очков из английской версии игры

| Очки  | Буквы |
|:------|:---------:|
1|  A, E, I, L, N, O, R, S, T и U
2| D и G
3| B, C, M и P
4| F, H, V, W и Y
5| K
8| J и X
10| Q и Z

### Игральные кости

В данном упражнении мы будем симулировать 1000 выбрасываний
игральных костей. Начнем с написания функции, выполняющей случай-
ное выбрасывание двух обычных шестигранных костей. Эта функция не
будет принимать входных параметров, а возвращать должна число, вы-
павшее в сумме на двух костях.
В основной программе реализуйте симуляцию тысячи выбрасываний
костей. Программа должна хранить все результаты с частотой их выпаде-
ния. После завершения процесса должна быть показана итоговая таблица
с результатами. Выразите
частоту выпадения каждого из чисел в процентах вместе с ожидаемым
результатом согласно теории вероятностей.

### Мобильное сообщение

Если помните, на старых мобильных телефонах текстовые сообщения на-
бирались при помощи цифровых кнопок. При этом одна кнопка была ас-
нажатий на кнопку. Однократное нажатие приводило к появлению первой
буквы в соответствующем этой кнопке списке, последующие нажатия ме-
няли ее на следующую. Список символов, ассоциированных с цифровой
панелью, приведен в таблице

| Кнопка  | Символы |
|:------|:---------:|
1| . , ? ! :
2| A B C
3| D E F
4| G H I
5| J K L
6| M N O
7| P Q R S
8| T U V
9| W X Y Z
0| Пробел

## 6. Файлы

### Удаление комментариев

Как вы знаете, в языке Python для создания комментариев в коде исполь-
зуется символ #. Комментарий начинается с этого символа и продолжает-
ся до конца строки – без возможности остановить его раньше.
В данном упражнении вам предстоит написать программу, которая
будет удалять все комментарии из исходного файла с кодом на языке
Python. Пройдите по всем строкам в файле на предмет поиска символа
#. Обнаружив его, программа должна удалить все содержимое, начиная
с этого символа и до конца строки. Для простоты не будем рассматривать
ситуации, когда знак решетки встречается в середине строки. Сохраните
новое содержимое в созданном файле. Имена файла источника и фай-
ла назначения должны быть запрошены у пользователя. Удостоверьтесь
в том, что программа корректно обрабатывает возможные ошибки при
работе с обоими файлами.

### Служебные слова

Перед публикацией текста или документа обычно принято удалять или
изменять в них служебную информацию.
В данном упражнении вам необходимо написать программу, которая
будет заменять все служебные слова в тексте на символы звездочек (по
количеству символов в словах). Вы должны осуществлять регистрозави-
симый поиск служебных слов в тексте, даже если эти слова входят в состав
других слов. Список служебных слов должен храниться в отдельном файле.
Сохраните отредактированную версию исходного файла в новом файле.
Имена исходного файла, файла со служебными словами и нового файла
должны быть введены пользователем.