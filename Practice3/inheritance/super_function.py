# super_function.py

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        parent_sound = super().speak()
        return f"{parent_sound}, specifically a {self.breed} barks"


dog = Dog("Buddy", "Labrador")
print(dog.speak())
