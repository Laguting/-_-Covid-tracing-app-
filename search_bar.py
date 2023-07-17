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
        self.initial_bg = Image.open("search.png")
        self.bg = ImageTk.PhotoImage(self.initial_bg)
        self.bg_name = tk.Label(self, image=self.bg)
        self.bg_name.place(x=0, y=0, relwidth=1, relheight=1)
        self.bind("<Configure>", self.resize_image)

# Search
    # Search label
        self.search_label = tk.Label(self, bg="yellow", fg="black", text="Search by Name:")
        self.search_label.place(x=60, y=250)
    # Search entry
        self.search_entry = tk.Entry(self, width=100)
        self.search_entry.place(x=180, y=250)
    # Search button
        self.search_button = tk.Button(self, text="Search", command=self.search_registration)
        self.search_button.place(x=820, y=250)
    # Search button result
        self.result_label = tk.Label(self, bg="yellow", fg="black", text="")
        self.result_label.place(x=230, y=300)
    # Present Search
        self.present_button = tk.Button(self, text="View Entry", command=self.view_entry, state=tk.DISABLED)
        self.present_button.place(x=400, y=720)
    # Edit Button
        self.edit_button = tk.Button(self, text="Edit Entry", command=self.edit_entry, state=tk.DISABLED)
        self.edit_button.place(x=500, y=720)

        self.registration_info = ""

# Navigation buttons
    # Back to home
        self.back_button = tk.Button(self, text="Back to Home", command=lambda: self.change_section(0))
        self.back_button.place(x=270, y=720)
    # Exit
        self.exit_button = tk.Button(self, text="Exit", command=lambda: self.change_section(2))
        self.exit_button.place(x=600, y=720)

# Background image
    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        resized_image = self.initial_bg.resize((new_width, new_height), Image.NEAREST)
        self.bg_image = ImageTk.PhotoImage(resized_image)
        self.bg_name.configure(image=self.bg_image)
        
# Search Registration information
    def search_registration(self):
        name_to_search = self.search_entry.get()
        registration_info = self.get_registration_info(name_to_search)

        if registration_info:
            self.registration_info = registration_info
            self.result_label.config(text="Registration found!")
            self.present_button.config(state=tk.NORMAL)
            messagebox.showinfo("Search Result", "Registration found!")
        else:
            self.result_label.config(text="No matching registration found.")
            self.present_button.config(state=tk.DISABLED)
            messagebox.showinfo("Search Result", "No matching registration found.")
# Get registration information
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
                if line.startswith("Close Contact Email Address:"):
                    is_matching_registration = False
        return registration_info if found else ""

# Display information modification
    def display_registration_info(self):
        self.result_label.config(text="")
        registration_lines = self.registration_info.split("\n")
        for line in registration_lines:
            label, value = line.split(":", 1)
            label = label.strip()
            value = value.strip()
            label_label = tk.Label(self, text=label, bg="yellow", fg="black")
            label_label.pack(anchor=tk.W, padx=30)
            value_label = tk.Label(self, text=value, bg="yellow", fg="black")
            value_label.pack(anchor=tk.W, padx=30) 

# Ask the user first if they wanted to view their entry
    def view_entry(self):
        confirmation = messagebox.askyesno("View Entry", "Do you want to view the registration entry?")
        if confirmation:
            self.result_label.config(text=self.registration_info)

# Allow the user to edit their entry
    def edit_entry(self):
        confirmation = messagebox.askyesno("Edit Entry", "Do you want to edit the registration entry?")
        if confirmation:
        # Open a new window or form to edit the registration information
            edit_window = tk.Toplevel(self.parent)
            edit_window.title("Edit Entry")

            # Create labels and entry fields for each registration field
            fields = self.registration_info.strip().split("\n")
            entry_labels = []
            entry_fields = []

            for field in fields:
                label_text, value_text = field.split(":", 1)
                label_text = label_text.strip()
                value_text = value_text.strip()

                # Label
                label = tk.Label(edit_window, text=label_text)
                label.grid(row=len(entry_labels), column=0, sticky=tk.W, padx=10, pady=5)
                entry_labels.append(label)
            # Save Button
            save_button = tk.Button(edit_window, text="Save", command=lambda win=edit_window: self.save_edited_entry(entry_fields, win))
        save_button.grid(row=len(entry_fields) + 1, columnspan=2, padx=10, pady=10)
# Save the edited entry
    def save_edited_entry(self, entry_fields, edit_window):
        # Get the edited values from the entry fields
        edited_values = [entry.get() for entry in entry_fields]

        # Update the registration information
        updated_registration_info = ""
        fields = self.registration_info.strip().split("\n")
        for i, field in enumerate(fields):
            label_text = field.split(":")[0].strip()
            updated_registration_info += f"{label_text}: {edited_values[i]}\n"

        # Update the registration info variable
        self.registration_info = updated_registration_info

        # Close the edit window
        edit_window.destroy()

        # Display the updated registration information
        self.display_registration_info()

    def present(self):
        self.pack()

    def hide(self):
        self.pack_forget()
