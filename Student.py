class Student:

    def __init__(self, name, major, gpa, is_male):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_male = is_male

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
