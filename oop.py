class student:
    def __init__(self, name, age, course, place):
        self.name = name
        self.age = age
        self.course = course
        self.place = place

    def show_std_details(self):
        print("Name: ", self.name)
        print("Age: :", self.age)
        print("Course: ", self.course)
        print("Place: ", self.place)


std1 = student("Rick", 22, "python", "UK")

std1.show_std_details()
