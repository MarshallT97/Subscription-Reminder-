from tkinter import *
import center_function

class Creator():
    def __init__(self,master):
        self.editor = Toplevel(master)
        self.editor.title("New Reminder")
        center_function.center(470, 200, self.editor)
        self.editor.resizable(0, 0)
        self.init_ui()

    def init_ui(self):
        entry_width = 45
        entry_colspan = 100

        title_label = Label(self.editor, text="Title:")
        title_label.grid(row=0, column=0, sticky=W)
        title_entry = Entry(self.editor, width=entry_width)
        title_entry.grid(row=0, column=1, columnspan=entry_colspan, sticky=W)

        price_label = Label(self.editor, text="Price:")
        price_label.grid(row=1, column=0, sticky=W)
        price_entry = Entry(self.editor, width=entry_width)
        price_entry.grid(row=1, column=1, columnspan=entry_colspan, sticky=W)

        date_label = Label(self.editor, text="Date Renewal:")
        date_label.grid(row=2, column=0, sticky=W)
        date_entry = Entry(self.editor, width=entry_width)
        date_entry.grid(row=2, column=1, columnspan=entry_colspan, sticky=W)

        tag_label = Label(self.editor, text="Tag:")
        tag_label.grid(row=3, column=0, sticky=W)
        tag_entry = Entry(self.editor, width=entry_width)
        tag_entry.grid(row=3, column=1, columnspan=entry_colspan, sticky=W)

        description_label = Label(self.editor, text="Description:")
        description_label.grid(row=4, column=0, sticky=W)
        description_entry = Entry(self.editor, width=entry_width)
        description_entry.grid(row=4, column=1, columnspan=entry_colspan, sticky=W)

        create_button = Button(self.editor, text="Create")
        create_button.grid(row=5, column=1, pady=20, sticky=W)

        cancel_button = Button(self.editor, text="Cancel", command=self.editor.destroy)
        cancel_button.grid(row=5, column=100, pady=20)