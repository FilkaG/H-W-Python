import view

def search_last_name(last_name, employee):
    count = 0
    for i in range(0, len(employee)):
        if employee[i]["last_name"] == last_name: 
            for x in employee[i]:
                print(employee[i][x])
            print('')
            count += 1
    if count == 0: print('Dont have this person!')

def search_position(position, employee):
    count = 0
    for i in range(0, len(employee)):
        if employee[i]["position"] == position: 
            for x in employee[i]:
                print(employee[i][x])
            print('')
            count += 1
    if count == 0: print('Dont have this person!')

def search_salary(salary1, salary2, employee):
    count = 0
    for i in range(0, len(employee)):
        if (employee[i]["salary"] >= salary1) and (employee[i]["salary"] <= salary2): 
            for x in employee[i]:
                print(employee[i][x])
            print('')
            count += 1
    if count == 0: print('Dont have this person!')

def new_person(id, last_name, first_name, position, phone_number, salary, employee):
    employee.append({"id": id, "last_name": last_name, "first_name": first_name,"position": position, "phone_number": phone_number, "salary": salary})
    return employee

def delete_person(id, employee):
    index = None
    for i in range(0, len(employee)):
        if employee[i]["id"] == id: 
            index = i
    if index == None: print('Dont have this person!')
    else: del employee[index]
    return employee

def new_data(id, employee):
    for i in range(0, len(employee)):
        if employee[i]["id"] == id: 
            index = i
    if index == None: print('Dont have this person!')
    else:
        last_name = input('Введите фамилию: ')
        first_name = input('Введите имя отчество: ')
        position = input('Введите должность: ')
        phone_number = input('Введите номер телефона: ')
        salary = input('Введите зарплату: ')
        employee[index]["last_name"] = last_name
        employee[index]["first_name"] = first_name
        employee[index]["position"] = position
        employee[index]["phone_number"] = phone_number
        employee[index]["salary"] = salary
    return employee
