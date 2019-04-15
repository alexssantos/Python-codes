getIn = True
students = []


def media(students):
    ages = [y for x, y in students]
    return sum(ages)/len(ages)


while getIn:
    print('AVISO: se quiser sair só precione ENTER. \n')
    name = input('Nome: ')
    student = [name]
    if name == '':
        getIn = False
        break
    ageNotOk = True
    while ageNotOk:
        a = input('Altura: ')
        try:
            age = float(a)
            student.append(age)
            ageNotOk = False
        except ValueError:
            print('ERRO - Altura invalida!')
    students.append(student)
    print(students)

media = media(students)
print('MEDIA: ', media)
upStudents = [x for x, y in students if y > media]
print(upStudents)