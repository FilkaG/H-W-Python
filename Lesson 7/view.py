def read_csv(filename: str): #-> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def read_txt(filename: str): #-> list:
    data = []
    lis = ''
    count = 0
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            lis = lis + line
            count += 1
            if count == 4:
                record = dict(zip(fields, lis.strip().split('\n')))
                data.append(record)
                count = 0
                lis = ''
    return data

def show_menu(): #-> int:
    print("\nВыберите необходимое действие:\n"
    "1. Отобразить весь справочник\n"
    "2. Найти абонента по фамилии\n"
    "3. Найти абонента по номеру телефона\n"
    "4. Добавить абонента в справочник\n"
    "5. Сохранить справочник в текстовом формате\n"
    "6. Закончить работу")
    choice = int(input())
    return choice

print(read_txt('phones.txt'))