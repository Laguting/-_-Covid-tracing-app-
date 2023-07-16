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

# Personal Information Labels
    # Name
        # Name label
        self.name_guide = tk.Label(self, text="FIRST NAME,MIDDLE NAME,SURNAME", bg="yellow",fg="black", font=("Times New Roman", 7)) # Name entry guide
        self.name_guide.place(x=100, y=60)
        self.name_label = tk.Label(self, bg="yellow",fg="black", text="Name:")
        self.name_label.place(x=30, y=80)
    # Address
        # Adress Label
        self.add_label = tk.Label(self, bg="yellow",fg="black", text="Address:")
        self.add_label.place(x=30, y=120)
    # Date of Birth
        # Date of Birth Label
        self.birth_guide = tk.Label(self, text="MONTH/DATE/YEAR", bg="yellow",fg="black", font=("Times New Roman", 7)) # Date entry guide
        self.birth_guide.place(x=100, y=140)
        self.birth_label = tk.Label(self, bg="yellow",fg="black", text="Birth Date:")
        self.birth_label.place(x=30, y=160)
    # Contact Information
        self.contact_banner = tk.Label(self, text="CONTACT INFORMATION", bg="yellow",fg="black", font=("Times New Roman", 10)) # Contact info banner
        self.contact_banner.place(x=370, y=190)
        # Phone Number Label
        self.phone_label = tk.Label(self, bg="yellow",fg="black", text="Phone Number:")
        self.phone_label.place(x=30, y=220)
        # Email Address
        self.phone_label = tk.Label(self, bg="yellow",fg="black", text="Email address:")
        self.phone_label.place(x=30, y=260)
        
# Personal Information Entries
    # Name
        # Name entry field
        self.name_entry = tk.Entry(self, width= 100)
        self.name_entry.place(x=100, y=80)
    # Address
        # Address Entry Field
        self.add_entry = tk.Entry(self, width= 100)
        self.add_entry.place(x=100, y=120)
    # Date of Birth
        # Date of Birth entry Field
        self.birth_entry = tk.Entry(self, width= 30)
        self.birth_entry.place(x=100, y=160)
    # Contact Information
        # Phone Number Label
        self.phone_entry = tk.Entry(self, width= 30)
        self.phone_entry.place(x=130, y=220)
        # Email Address
        self.email_entry = tk.Entry(self, width= 100)
        self.email_entry.place(x=120, y=260)

# Checklist for their health status
    # Vaccination status checklist
        self.healt_banner = tk.Label(self, text="HEALTH INFORMATION", bg="blue",fg="white", font=("Times New Roman", 10)) # Health Info banner
        self.healt_banner.place(x=370, y=290)
        self.vaccination_label = tk.Label(self, bg="yellow",fg="black", text="Vaccination Status")
        self.vaccination_label.place(x=30,y=320)
    # Are they Positive
        self.positive_label = tk.Label(self, bg="yellow",fg="black", text="Have you tested positive?")
        self.positive_label.place(x=30,y=420)
    # Have they been in contact with others
        self.contact_label = tk.Label(self, bg="yellow",fg="black", text="Have you been in contact with someone since you felt the symptoms?")
        self.contact_label.place(x=500,y=320)
    # Information of their identified closed contact
        self.close_contact_label = tk.Label(self, text="CLOSE CONTACT INFORMATION", bg="blue",fg="white", font=("Times New Roman", 10))
        self.close_contact_label.place(x=370, y=480)
    
# Buttons and Checklist
    # vaccination status chacklist
        self.vaccination_var1 = tk.IntVar() # 1st dose
        self.vaccination_check1 = tk.Checkbutton(self, text="1st Dose", variable=self.vaccination_var1)
        self.vaccination_check1.place(x=60,y=350)

        self.vaccination_var2 = tk.IntVar() # 2nd dose
        self.vaccination_check2 = tk.Checkbutton(self, text="2nd Dose", variable=self.vaccination_var2)
        self.vaccination_check2.place(x=60,y=380)

        self.vaccination_var3 = tk.IntVar() # 1st Booster
        self.vaccination_check3 = tk.Checkbutton(self, text="1st Booster", variable=self.vaccination_var3)
        self.vaccination_check3.place(x=190,y=350)

        self.vaccination_var4 = tk.IntVar() # 2nd booster
        self.vaccination_check4 = tk.Checkbutton(self, text="2nd Booster", variable=self.vaccination_var4)
        self.vaccination_check4.place(x=190,y=380)
    # Are they positive button
        self.positive_var = tk.StringVar() 
        # They're positive
        self.positive_radio1 = tk.Radiobutton(self, text="Yes", variable=self.positive_var, value="Yes")
        self.positive_radio1.place(x=60,y=450)
        
        # They're negative
        self.positive_radio2 = tk.Radiobutton(self, text="No", variable=self.positive_var, value="No")
        self.positive_radio2.place(x=120,y=450)  
    # Have they been in contact with others button
        self.contact_var = tk.StringVar()
        #They've been in contact with someone
        self.contact_radio1 = tk.Radiobutton(self, text="Yes", variable=self.contact_var, value="Yes")
        self.contact_radio1.place(x=530,y=350)
        
        # They haven't been in contact with someone
        self.contact_radio2 = tk.Radiobutton(self, text="No", variable=self.contact_var, value="No")
        self.contact_radio2.place(x=620,y=350)
        
# Close contact informations
    # Close contact labels
    # Name
        # Name label
        self.close_name_guide = tk.Label(self, text="FIRST NAME,MIDDLE NAME,SURNAME", bg="yellow",fg="black", font=("Times New Roman", 7)) # Name entry guide
        self.close_name_guide.place(x=100, y=520)
        self.close_name_label = tk.Label(self, bg="yellow",fg="black", text="Name:")
        self.close_name_label.place(x=30, y=550)
    # Address
        # Adress Label
        self.close_add_label = tk.Label(self, bg="yellow",fg="black", text="Address:")
        self.close_add_label.place(x=30, y=590)
    # Contact Information
        self.close_contact_banner = tk.Label(self, text="CONTACT INFORMATION", bg="yellow",fg="black", font=("Times New Roman", 10)) # Contact info banner
        self.close_contact_banner.place(x=370, y=610)
        # Phone Number Label
        self.close_phone_label = tk.Label(self, bg="yellow",fg="black", text="Phone Number:")
        self.close_phone_label.place(x=30, y=630)
        # Email Address
        self.close_phone_label = tk.Label(self, bg="yellow",fg="black", text="Email address:")
        self.close_phone_label.place(x=30, y=690)
        
    # Close contact entries     
    # Name
        # Name entry field
        self.close_name_entry = tk.Entry(self, width= 100)
        self.close_name_entry.place(x=100, y=550)
    # Address
        # Address Entry Field
        self.close_add_entry = tk.Entry(self, width= 100)
        self.close_add_entry.place(x=100, y=580)
    # Contact Information
        # Phone Number Label
        self.close_phone_entry = tk.Entry(self, width= 30)
        self.close_phone_entry.place(x=130, y=630)
        # Email Address
        self.close_email_entry = tk.Entry(self, width= 100)
        self.close_email_entry.place(x=120, y=690)
        
        # Submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_registration)
        self.submit_button.place(x=450, y=730)
        

    def submit_registration(self):
        name = self.name_entry.get()
        address = self.add_entry.get()
        birth_date = self.birth_entry.get()
        phone_number = self.phone_entry.get()
        email_add = self.email_entry.get()
        vaccination_status = {
            "1st Dose": bool(self.vaccination_var1.get()),
            "2nd Dose": bool(self.vaccination_var2.get()),
            "1st Booster": bool(self.vaccination_var3.get()),
            "2nd Booster": bool(self.vaccination_var4.get()),
        }
        positive = self.positive_var.get()
        contact = self.contact_var.get()
        close_contact_name = self.close_name_entry.get()
        close_contact_address = self.close_add_entry.get()
        close_contact_phone = self.close_phone_entry.get()
        close_contact_email = self.close_email_entry.get()
    # Save the informations in txt file
        with open("user_inputs_folder.txt", "a") as file:
            file.write("Registration Information:\n")
            file.write("Name: {}\n".format(name))
            file.write("\n")
        # Perform further processing or save the registration information

        # Print the registration information as an example
        print("Registration Information:")
        print("Name:", name)
        print("Address:", address)
        print("Birth Date:", birth_date)
        print("Phone Number:", phone_number)
        print("Email Address:", email_add)
        print("Vaccination Status:", vaccination_status)
        print("Have you tested positive?:", positive)
        print("Have you been in contact with someone since you felt the symptoms?:", contact)
        print("Close Contact Information:")
        print("Close Contact Name:", close_contact_name)
        print("Close Contact Address:", close_contact_address)
        print("Close Contact Phone:", close_contact_phone)
        print("Close Contact Email Address: ", close_contact_email)
        
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
