from tkinter import *

ablak = Tk()
ablak.geometry("600x400")


def key_press(event):
    key = event.char
    print(key, 'is pressed')


def enter(event):
    wid = event.widget
    a = wid.grid_info()
    b = (a["row"], a["column"])
    print('Button-1 pressed at :' + str(wid) + " Grid, info: " + str(b))


txt1 = Label(ablak, text="Első mező:")
txt2 = Label(ablak, text="Második mező:")
txt3 = Label(ablak, text="Harmadik mező:")

mezo1 = Entry(ablak)
mezo2 = Entry(ablak)
mezo3 = Entry(ablak)

# egy bitmap képet tartalmazó 'Canvas' widget létrehozása :
can1 = Canvas(ablak, width=160, height=160, bg='white')
photo = PhotoImage(file='alien1.gif')
item = can1.create_image(80, 80, image=photo)

txt1.grid(row=0, sticky=W)
txt2.grid(row=1, sticky=W)
txt3.grid(row=2, sticky=W)

mezo1.grid(row=0, column=1)
mezo2.grid(row=1, column=1)
mezo3.grid(row=2, column=1)
can1.grid(row=0, column=3, rowspan=3, padx=10, pady=3)

for r in range(3):
    for c in range(4, 10):
        # "flat", "raised", "sunken", "ridge", "solid", and "groove".
        Label(ablak, text='R%s/C%s' % (r, c), borderwidth=1, relief="groove", cursor="hand2", ).grid(row=r, column=c)
        print(type(Label))


ablak.bind('<Button-1>', enter)
ablak.bind('<Key>', key_press)

ablak.mainloop()