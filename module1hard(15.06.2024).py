grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  #Список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  #Множество

grades_1 = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])]
print(grades_1)

students_1 = list(students)  #Преобразование множества в список и сортировка в алф. порядке, не понял почему именно так работает
students_2 = students_1.sort()
print(students_1)

general_list = [[students_1[0], grades_1[0]], [students_1[1], grades_1[1]], [students_1[2], grades_1[2]], [students_1[3], grades_1[3]], [students_1[4], grades_1[4]]]  #Список, объединение в пары
print(general_list)

average_student_grade = dict(general_list)  #Создание словаря
print(average_student_grade)