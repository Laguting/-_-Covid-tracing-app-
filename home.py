import tkinter as tk
from PIL import ImageTk, Image

#Create class for the home
class Home(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text = "Home")
        self.label.pack(fill = "both", expand = 1)

        # Background
        self.initial_bg = Image.open(r"home.PNG")
        self.bg = ImageTk.PhotoImage(self.initial_bg)
        self.bg_name = tk.Label(self, image = self.bg)
        self.bg_name.place(x= 0, y=0, relwidth=1, relheight=1)
    
    def present(self):
        self.pack()
    def hide(self):
        self.pack_forget()


