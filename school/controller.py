# 1. Показ списка учеников
# 2. Добаить нового студента (поля: имя, фамилия)
# 3. Добаить предмет
# 4. Добаить оценку ученику
# 5. Редактировать данные ученика
# 6. Удалить ученика
# 7. Показ листа оценок конкретного ученика
# 8. Выход из программы


import view
import model

def start():
    value =''
    while True:
        value = view.menu()
        match value:
            case 1:
                model.open_file()
                view.show_students(model.get_students_book())
                model.close_file()
            case 2:
                model.open_file()
                new_student = list(view.create_student())
                model.add_new_student(new_student)
                view.information(f'\nНовый ученик {new_student} добавлен.\n')
                model.save_file()
                model.close_file()
            case 3:
                pass
            case 4:
                pass
            case 5:
                model.open_file()
                name = view.select_student('Введите ученика, которого необходимо изменить: ')
                student = model.get_student(name) # кортеж - студент и его индекс
                print(student)
                if student:
                    upd_student = view.change_student()
                    model.change_student(student[1], list(upd_student)) # в кортеже под индексом 1 хранится индекс (кортеж - студент и его индекс)
                elif student == []:
                    view.empty_request()
                else:
                    view.many_request()
                view.information(f'\nДанные об ученике {student[0][0]} обновлены\n')
                model.save_file()
                model.close_file()
            case 6:
                model.open_file()
                del_name = view.select_student('Введите удаляемый контакт: ')
                student = model.get_student(del_name)
                if student:
                    confirm = view.delete_confirm(student[0][0])
                    if confirm:
                        model.del_student(student[0])  
                        view.information(f'\nДанные об ученике {student[0][0]} удалены\n')
                elif student == []:
                    view.empty_request()
                else:
                    view.many_request()
                model.save_file()
                model.close_file()
            case 7:
                pass
            case 8:
                view.end_prog()
                break