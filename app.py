from tkinter import Tk

colors = ['blue', 'red', 'yellow', 'green', 'pink', 'grey']
POINTER = 0


def changeBackColor(event):
    global POINTER
    if POINTER == len(colors) - 1:
        POINTER = 0
    else:
        POINTER += 1
    gui['background'] = colors[POINTER]


gui = Tk(className="Lab_01_Aidar_Khuzin_Evgeny_Petrashko")
gui.geometry("800x800")
gui.configure(bg='blue')
gui.bind('<Button-1>', changeBackColor)
gui.mainloop()


