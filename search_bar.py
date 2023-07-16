import tkinter as tk
from PIL import ImageTk, Image

class Search_Bar(tk.Frame):
    def __init__(self, parent, change_section):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.change_section = change_section
        self.label = tk.Label(self, text="Home")
        self.label.pack(fill="both", expand=1)

        # Background
        self.initial_bg = Image.open("register.png")
        self.bg = ImageTk.PhotoImage(self.initial_bg)
        self.bg_name = tk.Label(self, image=self.bg)
        self.bg_name.place(x=0, y=0, relwidth=1, relheight=1)
        self.bind("<Configure>", self.resize_image) 
       
        # Resize image
    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        resized_image = self.initial_bg.resize((new_width, new_height), Image.NEAREST)
        self.bg_image = ImageTk.PhotoImage(resized_image)
        self.bg_name.configure(image=self.bg_image)

# Search Entry
        # Search bar label
        self.search_label = tk.Label(self, bg="yellow", fg="black",text="Search by Name:")
        self.search_label.place(x=30, y=45)
        # Search bar entry
        self.search_entry = tk.Entry(self, width=100)
        self.search_entry.place(x=150, y=45)
        # Search button
        self.search_button = tk.Button(self, text="Search", command=lambda: self.change_section(0)) # temporary so that the search button will appear
        self.search_button.place(x=780, y=45)
        # Search Result
        self.result_label = tk.Label(self, text="") # Display the result of the searched informaion
        self.result_label.place(x=30, y=100)
    
       
# Navigation buttons
        # Back button
        self.back_button = tk.Button(self, text="Back to Home", command=lambda: self.change_section(0))
        self.back_button.place(x=250, y=720)

        # Exit button
        self.exit_button = tk.Button(self, text="Exit", command=lambda: self.change_section(2))
        self.exit_button.place(x=650, y=720)

    def present(self):
        self.pack()

    def hide(self):
        self.pack_forget()
    