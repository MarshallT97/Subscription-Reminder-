from tkinter import *
import new_reminder
import center_function
# import the frame class needed to inherit from
from tkinter.ttk import Frame,Style

class Window(Frame):
    def __init__(self, master):
        # use the __init__() of the Frame class
        super().__init__()
        self.search_input = StringVar()
        self.master = master
        self.init_ui()

    def init_ui(self):
        # set the title of the window
        self.master.title("Main Window")
        self.style = Style()
        self.style.theme_use('clam')
        center_function.center(700, 440, self.master)

        search_label = Label(self.master, text="Search:")
        search_label.grid(row=0, column=2, sticky=N)
        search_bar = Entry(self.master, width=56)
        search_bar.grid(row=0, column=3, columnspan=100, sticky=N)

        scrollbar = Scrollbar(self.master)
        scrollbar.grid(row=0, column=1, rowspan=105, sticky=N+S+W)

        self.reminder_list = Listbox(self.master, height=21, yscrollcommand=scrollbar.set)
        self.reminder_list.grid(row=0, column=0, rowspan=105, sticky=W)
        self.reminder_list.insert(0, self.list_format("Cor_Vous Sub"))
        for x in range(1, 31):
            self.reminder_list.insert(END, str(x))
        scrollbar.config(command=self.reminder_list.yview)

        self.reminder_text()
        self.reminder_text("Cor_Vous Sub", "Twitch subscription for Cor_Vous", 4.99, "October 22, 2018", "Twitch")

        add_button = Button(self.master, text="Add", command=self.create_reminder)
        add_button.grid(row=15, column=3)
        delete_button = Button(self.master, text="Delete")
        delete_button.grid(row=15, column=102)

        self.total_cost()

    def reminder_text(self, title="", description="", price=0, date="", tag=""):
        field_width = 454
        field_height = 225
        inital_x = 7
        inital_y = 5

        field = Canvas(self.master, width=field_width, height=field_height)
        field.grid(row=1, column=3, columnspan=100)
        field.create_rectangle(0, 0, field_width, field_height, fill="white")
        field.create_text(inital_x, inital_y*2, anchor=NW, text="Title: {}".format(title))
        field.create_text(inital_x, inital_y*11, anchor=NW, text="Description: {}".format(description))
        field.create_text(inital_x, inital_y*20, anchor=NW, text="Price: ${}".format(price))
        field.create_text(inital_x, inital_y*29, anchor=NW, text="Due: {}".format(date))
        field.create_text(inital_x, inital_y*38, anchor=NW, text="Tag: {}".format(tag))

    def total_cost(self):
        field_width = 600
        field_height = 50
        inital_x = 7
        inital_y = 5

        field = Canvas(self.master, width=field_width, height=field_height)
        field.grid(row=104, column=2, columnspan=200)
        field.create_rectangle(0, 0, field_width, field_height, fill="green")
        field.create_text((field_width-120)/2, field_height/2, anchor=CENTER,
                          fill="white", text="Month Total: $1000.00")

    def list_format(self, title):
        if len(title) >= 21:
            return title[:21] + ".."
        else:
            return title

    def create_reminder(self):
        new_window = new_reminder.Creator(self.master)


if __name__ == '__main__':
    root = Tk()
    window = Window(root)
    root.resizable(0, 0)
    root.mainloop()