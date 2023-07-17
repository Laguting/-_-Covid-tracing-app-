
    
    def change_section(self, section_n):
        for section in self.sections:
            section.hide()
        self.present_section(section_n)

if __name__ == "__main__":
    cta = CovidTrace()
    cta.mainloop()
