import  new_list as new
import view

filename = 'phones.txt'

def button_click():
    if filename == 'phonebook.csv': book = view.read_csv(filename)
    elif filename == 'phones.txt': book = view.read_txt(filename)
    bool = True
    while bool == True:
        tap = view.show_menu()
        if tap == 6: break
        if tap == 1: new.show_book(book)
        if tap == 2:
            surname = input('Print surname: ')
            new.search_surname(surname, book)
        if tap == 3:
            number = input('Print number: ')
            new.search_number(number, book)
        if tap == 4:
            name = input('Print name: ')
            surname = input('Print surname: ')
            number = input('Print number: ')
            comment = input('Print comment: ')
            book = new.new_person(name, surname, number, comment, book)
        if tap == 5: 
            file = input('Print name file to save: ')
            new.save_book(book, file)

    