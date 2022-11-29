import view
import model

filename = 'database.cvs'

def buttom_click():
    if filename == 'database.cvs': employee = view.read_csv()
    elif filename == 'database02.json': employee = view.read_json()
    bool = True
    while bool == True:
        tap = view.show_menu()
        if tap == 9: break
        if tap == 1:
            last_name = input('Введите фамилию: ')
            model.search_last_name(last_name, employee)
        if tap == 2:
            position = input('Введите должность: ')
            model.search_position(position, employee)
        if tap == 3:
            salary1 = int(input('Введите зарплату от: '))
            salary2 = int(input('Введите зарплату до: '))
            model.search_salary(salary1, salary2, employee)
        if tap == 4:
            id = int(input('Введите id: '))
            last_name = input('Введите фамилию: ')
            first_name = input('Введите имя отчество: ')
            position = input('Введите должность: ')
            phone_number = input('Введите номер телефона: ')
            salary = input('Введите зарплату: ')
            employee = model.new_person(id, last_name, first_name, position, phone_number, salary, employee)
        if tap == 7: view.write_json(employee)
        if tap == 8: view.write_csv(employee)
        if tap == 5:
            id = int(input('Введите id, которого надо убрать: ')) 
            employee = model.delete_person(id, employee)
        if tap == 6:
            id = int(input('Введите id сотрудника, у которого надо изменить даные: '))
            employee = model.new_data(id, employee)
    