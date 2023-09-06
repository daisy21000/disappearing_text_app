from tkinter import *

timer = None

window = Tk()

window.title('Disappearing Text Writing App')

window.config(padx=20, pady=20)

title = Label(text='Disappearing Text Writing App', font=('Courier', 20, 'bold'), fg='#FF3030')

title.pack()

subtitle = Label(text='Keep writing otherwise your work will disappear in 5 seconds', font=('Arial', 10, 'italic'), fg='white', bg='black')

subtitle.pack()


def clear_text():
    text_field.delete(1.0, END)


def typed(key):
    global timer
    if timer:
        window.after_cancel(timer)
    timer = window.after(5000, clear_text)


text_field = Text(height=15, width=70, font=('Arial', 10, 'normal'))

text_field.bind('<Key>', typed)

text_field.pack()

window.mainloop()
