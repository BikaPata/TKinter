import tkinter


class simpleapp_tk(tkinter.Tk):

    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()  # .grid() Layout type, in a grid you put objects by telling python the position of things (column=x, row=y)

        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0, row=0, sticky='EW')  # .entry is for text entries
        self.entry.bind("<Return>",
                        self.OnPressEnter)  # here we bind the method that will be called when we press Enter
        self.entryVariable.set(u"Enter text here.")

        button = tkinter.Button(self, text=u"Click me !",
                                command=self.OnButtonClick)  # here we bind the method that will be called when we click the button
        button.grid(column=1, row=0)  # .button obviously you know wtf a button is.

        self.labelVariable = tkinter.StringVar()  # we set up a special variable to the label then bind it to the label.
        label = tkinter.Label(self, textvariable=self.labelVariable,
                              anchor="w", fg="white",
                              bg="black")  # .label here you will set the configs of a LABEL, in the indented with (self, are the configurations of the color.
        label.grid(column=0, row=1, columnspan=2, sticky='EW')
        self.labelVariable.set(u"Hello !")

        self.grid_columnconfigure(0, weight=1)  # when you resize the program the COLUMNS=0 will resize too horizontaly.
        self.resizable(True,
                       False)  # .resizable(Horizontaly, Verticaly) how the program will be resized (True, False) the program will resize horizontaly but not verticaly.
        self.update()
        self.geometry(self.geometry())  # this will give the program the ability to keep geometric.
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def OnButtonClick(self):
        self.labelVariable.set(
            self.entryVariable.get() + " (You clicked the button !)")  # function that will be executed when you click the button.
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

    def OnPressEnter(self, event):
        self.labelVariable.set(self.entryVariable.get() + " (You pressed enter !)")  # function for when you press enter
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()  # the program wil have a infite loop, this will keep it open until the user do something.
