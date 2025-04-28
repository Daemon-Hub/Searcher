from tkinter import *
import os

WIDTH = 600
HEIGHT = 400

srch = []
srch_compit = []


def Search():

    user_width = window.winfo_screenwidth()
    user_height = window.winfo_screenheight()

    dirr = dir_entry.get()
    expansion = expansion_enty.get()

    for root, dirs, files in os.walk(dirr):
        for file in files:
            if file.endswith(expansion):
                srch.append(os.path.join(root, file))
    
    srch_count = len(srch)

    window.geometry('{}x{}'.format(user_width, user_height))
    
    srch_compit = StringVar(value=srch)

    msg['listvariable'] = srch_compit
    msg.place(x=0, y=100, width=user_width, height=user_height)
    
    label_count['text'] = f'Всего найдено " {expansion} " файлов : {srch_count}'
    label_count.place(x=WIDTH, y=0, width=user_width/2, height=100)
    
    srch.clear()


window = Tk()
window.title('Searsh')
window.geometry('{}x{}'.format(WIDTH, HEIGHT))
window.config(bg='black')
window.resizable(width=True, height=True)


dir_entry = Entry(font=("Arial", 30))
dir_entry.place(x=100, y=0, width=250, height=100)
dir_entry.focus()

expansion_enty = Entry(font=("Arial", 30))
expansion_enty.place(x=350, y=0, width=250, height=100)
expansion_enty.focus()


img = PhotoImage(file='search.png')
btn = Button(image=img, bg='black', command=Search)
btn.place(x=0, y=0)


label_info = Label(text='1)В первой строке укажите директорию для пойска например:\n[C:/Users/Public/]\n2)Во второй расширение файла например: [.exe, .pdf, .docx]\n3)Не советую указывать только [С:/]', font=('Arial', 16), fg='white', bg='black')
label_info.place(x=0, y=120, width=WIDTH)

label_count = Label(text='', font=('Arial', 30), fg='white', bg='black')

msg = Listbox(listvariable='')


window.mainloop()