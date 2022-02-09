class Human:

    def __init__(self, name, gender):
        
        self.name = name
        self.gender = gender
        self.age = 0
        self.height = 0
        self.skin_color = "Black"


    def set_age(self, age):
        self.age = age

    def get_age(self, age):
        self.age = age

    def set_height(self, height):
        self.height = height

    def set_skin_color(self, skin_color):
        self.skin_color = skin_color

# age = dami["age"]
# age = dami.age

dami = Human("Dami", "Male")
dami.set_age(16)
print(dami.age)
dami.set_height(1.67)
print(dami.height)
dami.set_skin_color("Brown skin boyyyyyy")
print(dami.skin_color)
