import tkinter as tk
from PIL import ImageTk, Image

class Home(tk.Frame):
    def __init__(self, parent, change_section):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.change_section = change_section
        self.label = tk.Label(self, text="Home")
        self.label.pack(fill="both", expand=1)

        # Background
        self.initial_bg = Image.open(r"home.PNG")
        self.bg = ImageTk.PhotoImage(self.initial_bg)
        self.bg_name = tk.Label(self, image=self.bg)
        self.bg_name.place(x=0, y=0, relwidth=1, relheight=1)

        # Menubar
        self.menu_bar = tk.Menu(self.parent)
        self.parent.config(menu=self.menu_bar)
        
        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        # Register menu item
        self.file_menu.add_command(label="Register", command=self.register)

    def register(self):
        print("Register section")

    def present(self):
        self.pack()

    def hide(self):
        self.pack_forget()
