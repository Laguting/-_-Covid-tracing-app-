import tkinter as tk
from PIL import ImageTk, Image

class Register(tk.Frame):
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
        
        self.info = tk.Label(self,bg="black", fg="yellow",text = "Registration ", height=1, font=("Times New Roman", 13))
        self.info.place(x=400, y=45)

# Labels
    # Name
        # Name label
        self.name_guide = tk.Label(self, text="FIRST NAME,MIDDLE NAME,SURNAME", bg="yellow",fg="black", font=("Times New Roman", 7)) # Name entry guide
        self.name_guide.place(x=100, y=55)
        self.name_label = tk.Label(self, bg="yellow",fg="black", text="Name:")
        self.name_label.place(x=30, y=80)
    # Address
        # Adress Label
        self.add_label = tk.Label(self, bg="yellow",fg="black", text="Address:")
        self.add_label.place(x=30, y=120)

# Entries
    # Name
        # Name entry field
        self.name_entry = tk.Entry(self, width= 100)
        self.name_entry.place(x=100, y=80)
    # Address
        # Address Entry Field
        self.add_entry = tk.Entry(self, width= 100)
        self.add_entry.place(x=110, y=120)
        
        # Submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_registration)
        self.submit_button.place(x=450, y=700)
        

    def submit_registration(self):
        name = self.name_entry.get()
        # Perform further processing or save the registration information

        # Print the registration information as an example
        print("Registration Information:")
        print("Name:", name)
        
        #Resize image
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
