#1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
# print("enter something")
# user_input_one = input()
# print(user_input_one)

#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
# print("enter time in seconds")
# user_input_one = int(input())
# time_seconds = 0
# time_minutes = 0
# time_hours = 0
# time_seconds = (user_input_one % 60)
# time_minutes = ((user_input_one // 60)%60)
# time_hours = (user_input_one // 3600)
# print(str(time_hours) + ' hh ' + str(time_minutes) + ' mm ' + str(time_seconds) + ' ss')

#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
#
# print('enter number 0<=N<=9')
# user_input_three =int(input())
#
# task_countdown = user_input_three + (user_input_three * 10 + user_input_three) + ((user_input_three * 100)+ (user_input_three * 10 + user_input_three))
#
# print(task_countdown)


#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
print('enter int number (>0)')
user_input_four =int(input())
first_digit = user_input_four % 10
second_digit = user_input_four % 100 // 10
third_digit = user_input_four  % 1000 // 100
# для большего количество цифр в числе можно было бы исползовать массивы, но мы их пока не прошли
print(first_digit)
print(second_digit)
print(third_digit)






#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
# print('enter Viruchka')
# user_viruchka = input()
# print('print izdershki')
# user_izdershki  = input()
# print('virucka firmi ' + user_viruchka + ' and izdershki firmi is ' + user_izdershki)
# if (int(user_viruchka) > int(user_izdershki)):
#     print(int(user_viruchka)/int(user_izdershki))
#     print('enter number of workers')
#     user_workers = int(input())
#     print('viruchka per worker is ' + str(int(user_viruchka)/user_workers) )



#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
#Например: a = 2, b = 3.
#Результат: 1-й день: 2 2-й день: 2,2 3-й день: 2,42 4-й день: 2,66 5-й день: 2,93 6-й день: 3,22  Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
#
# print('enter start killometers')
# start_kilommeters = int(input())
# print('enter end killometers')
# end_kilometers = int(input())
#
# progress_kilometers = start_kilommeters
# aa_day = 1
# while progress_kilometers < end_kilometers:
#     progress_kilometers = progress_kilometers * 1.10
#     aa_day =aa_day+1
#     print(aa_day, progress_kilometers)
