from tkinter import *

class ClassGui(Frame):
    def __init__(self):
        super().__init__()
        self.create_widget()

    def on_configure(self,event, canvas):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        canvas.configure(scrollregion=canvas.bbox('all'))

    def create_widget(self):
        large_font = ('Verdana', 12)
        entry1Var = StringVar(value='')

        self.master.title("Chat Bot")
        frame = Frame(self, relief=RAISED, borderwidth=1, bg="white")
        frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        self.pack(fill=BOTH, expand=True, pady=20, padx=8)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=BOTH)
        mylist = Listbox(frame, font=large_font)
        for line in range(100):
            if line%2==0:
                mylist.insert(END, "BOT: This is line number " + str(line))
            else:
                mylist.insert(END, "                   YOU: This is line number " + str(line))

        mylist.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=mylist.yview)
        mylist.pack(side=LEFT, fill=BOTH, expand=YES)

        sendButton = Button(self, text="SEND", relief=RAISED)
        sendButton.pack(side=RIGHT, padx=5, pady=5)

        chat_entry = Entry(self, textvariable=entry1Var, font=large_font)
        chat_entry.pack(side=RIGHT, expand=1, fill=X, ipadx=100, ipady=5)


def main():
    root = Tk()
    root.geometry("400x500")
    app = ClassGui()
    root.mainloop()

if __name__ == '__main__':
    main()