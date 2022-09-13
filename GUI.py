from tkinter import *
window = Tk()
window.geometry("420x420")
window.title("first gui program")

icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background="blue")

window.mainloop()