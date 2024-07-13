grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = list(sorted(students))
average_grades = []
for i in grades:
    average_grades.append(sum(i)/len(i))
print(dict(zip(sorted_students, average_grades)))