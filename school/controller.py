import view
import model

def start():
    value =''
    while True:
        value = view.menu()
        match value:
            case 1:
                value = view.menu()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                view.end_prog()
                break