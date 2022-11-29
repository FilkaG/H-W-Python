
def show_book(book):
    book_list = ''
    for i in range(0, len(book)):
        for x in book[i]:
            book_list = book_list + book[i][x]+' '
        print(book_list)
        book_list = ''

def search_surname(surname, book):
    count = 0
    for i in range(0, len(book)):
        if book[i]["Фамилия"] == surname: 
            for x in book[i]:
                print(book[i][x])
            print('')
            count += 1
    if count == 0: print('Dont have this person!')
        
def search_number(number, book):
    count = 0
    for i in range(0, len(book)):
        if book[i]["Телефон"] == number: 
            for x in book[i]:
                print(book[i][x])
            print('')
            count += 1
    if count == 0: print('Dont have this person!')

def new_person(name, surname, number, comment, book):
    book.append({"Фамилия": surname, "Имя": name, "Телефон": number,"Описание": comment })
    return book


def save_book(book, file):
    f = open(file,'w',encoding='UTF-8')
    for i in range(0, len(book)):
        for x in book[i]:
            str = (book[i][x] + '\n')
            f.write(str)
    f.close
