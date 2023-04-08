import view as v
import model as m

def click_button():
    value = v.main_menu()
    if value == 1:
        v.view_data(m.show_note())
        v.close()
    elif value == 2:
        m.filter_by_date(v.filter_by_date())
        v.close()
    elif value == 3:
        m.new_note(v.new_note())
        v.close()
    elif value == 4:
        m.remove_note(v.remove_note())
        v.close()
    elif value == 5:
        m.change_note(v.change_note())
        v.close()
    elif value == 6:
        exit()





   
   

  