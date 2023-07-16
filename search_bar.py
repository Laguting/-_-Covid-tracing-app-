import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

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
        self.search_button = tk.Button(self, text="Search", command=self.search_registration) # Search the entry
        self.search_button.place(x=780, y=45)
        # Search Result
        self.result_label = tk.Label(self, bg="yellow", fg="black" ,text="") # Display the result of the searched informaion
        self.result_label.place(x=200, y=100)

# Navigation buttons
        # Back button
        self.back_button = tk.Button(self, text="Back to Home", command=lambda: self.change_section(0))
        self.back_button.place(x=250, y=720)

        # Exit button
        self.exit_button = tk.Button(self, text="Exit", command=lambda: self.change_section(2))
        self.exit_button.place(x=650, y=720)

# Search entry confirmation
    def search_registration(self):
        name_to_search = self.search_entry.get()
        registration_info = self.get_registration_info(name_to_search)

        if registration_info:
            self.result_label.config(text=registration_info)
            self.present_button.config(state=tk.NORMAL)
            messagebox.showinfo("Search Result", "Registration found!")
        else:
            self.result_label.config(text="No matching registration found.")
            self.present_button.config(state=tk.DISABLED)
            messagebox.showinfo("Search Result", "No matching registration found.")
            
# Get the registration information
    def get_registration_info(self, name):
        with open("user_inputs_folder.txt", "r") as file:
            lines = file.readlines()

        registration_info = ""
        found = False
        is_matching_registration = False

        for line in lines:
            line = line.strip()
            if line.startswith("Name:") and name in line:
                found = True
                is_matching_registration = True
                registration_info += line + "\n"
            elif is_matching_registration:
                registration_info += line + "\n"
                if line.startswith("Name: "):
                    is_matching_registration = False
        return registration_info if found else ""
        
    def present(self):
        self.pack()

    def hide(self):
        self.pack_forget()
    