import tkinter as tk
from PIL import ImageTk, Image

class Register(tk.Menu):
    def __init__(self, parent, change_section):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.change_section = change_section
        self.label = tk.Label(self, text="Register")
        self.label.pack(fill="both", expand=1)

        # Background
        self.initial_bg = Image.open("register.png")
        self.bg = ImageTk.PhotoImage(self.initial_bg)
        self.bg_name = tk.Label(self, image=self.bg)
        self.bg_name.place(x=0, y=0, relwidth=1, relheight=1)
        self.bind("<Configure>", self.resize_image) 

        self.info = tk.Label(self,text = "Registration ", height=1, font=("Times New Roman", 13))
        self.info.place(x=400, y=45)

# Labels
        # name
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.place(x = 30, y =60)
        self.name_label.pack()
# Entry fields of the user
        #name
        self.name_entry = tk.Entry(self, width = 50)
        self.name_entry.place(x=30, y= 90)
        self.name_entry.insert(0, "FIRST NAME,MIDDLE NAME,SURNAME")
        self.name_entry.bind("<FocusIn>", self.clear_name)
        self.name_entry.config(fg="blue")
        self.name_entry.pack()
        
    def clear_name(self, event):
        self.name_entry.delete(0, tk.END)
        self.name_entry.config(fg="black")

        # Submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_registration)
        self.submit_button.place(x=30, y=90)
        self.submit_button.pack()

    def submit_registration(self):
        name = self.name_entry.get()
        # Perform further processing or save the registration information

        # Print the registration information as an example
        print("Registration Information:")
        print("Name:", name)
        
        # resize image 
    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        resized_image = self.initial_bg.resize((new_width, new_height), Image.NEAREST)
        self.bg_image = ImageTk.PhotoImage(resized_image)
        self.bg_name.configure(image=self.bg_image)
        
    def present(self):
        self.pack()

    def hide(self):
        self.pack_forget()