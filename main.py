from tkinter import *
from pytube import YouTube


def yo():
    link = t.get('1.0', END)
    save_path = r"Yo"
    try:
       url = YouTube(link)
       video = url.streams.get_lowest_resolution()
       video.download(save_path)
       s.config(text="Готово")
    except:
        s.config(text="Не верный URL")
        

root = Tk()

root.title('YODownloader')
root.geometry('400x590')
root.config(bg='black')
root.resizable(False, False)


icon = PhotoImage(file='Путь к иконке')

but = Button(root, image=icon, bg='black', width=64, height=64, command=yo, relief=FLAT)
but.pack(side=BOTTOM, pady=100,)

t = Text(root, bg="red", fg='white', width=100, height=2, font='Arial 10 bold')
t.pack(padx=30, pady=100)

s = Label(root, bg='black', fg='white', text="YODownloader", font='Arial 20 bold')
s.pack(pady=30, padx=30)

root.mainloop()
