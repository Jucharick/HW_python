import view
import model



def start():
    value =''
    while True:
        value = view.menu()
        match value:
            case 1:
                model.open_file()
                view.information('\nФайл успешно открыт\n')
            case 2:
                model.save_file()
                view.information('\nФайл успешно сохранен\n')
            case 3:
                view.show_contacts(model.get_phone_book())
            case 4:
                new_contact = list(view.create_contact())
                model.add_new_contact(new_contact)
                view.information(f'\nНовый контакт {new_contact} создан, не забудьте сохранить => 2\n')
            case 5:
                del_name = view.select_contact('Введите удаляемый контакт: ')
                contact = model.get_contact(del_name)
                if contact:
                    confirm = view.delete_confirm(contact[0][0])
                    if confirm:
                        model.del_contact(contact[0])   
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request()
                view.information(f'\nКонтакт {contact[0][0]} удален, не забудьте сохранить => 2\n')
            case 6:
                name = view.select_contact('Введите изменяемый контакт: ')
                contact = model.get_contact(name) # кортеж - сам контакт и его индекс
                if contact:
                    upd_contact = view.change_contact()
                    model.change_contact(contact[1], list(upd_contact)) # в кортеже под индексом 1 хранится индекс (кортеж - сам контакт и его индекс)
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request()
                view.information(f'\nКонтакт {contact[0][0]} изменен, не забудьте сохранить => 2\n')
            case 7:
                find = view.find_contact()
                result = model.search_contact(find)
                view.show_contacts(result)
            case 8:
                view.end_prog()
                break