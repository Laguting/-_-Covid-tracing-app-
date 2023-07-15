import tkinter as tk
from home import Home

class CovidTrace(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initial interface
        self.title("Hygieia")
        self.geometry("940x788")
        self.sections = []
        self.currentsection = 0
        
        # Sections
        self.frame = Home(self, self.change_section)
        self.sections = [self.frame]
        
        # Show initial section
        self.present_section(self.currentsection)

    def present_section(self, section_n):
        section = self.sections[section_n]
        section.pack(fill="both", expand=True)
        self.present = section_n
    
    def change_section(self, section_n):
        self.sections[self.currentsection].hide()
        self.present_section(section_n)

if __name__ == "__main__":
    cta = CovidTrace()
    cta.mainloop()
