class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound"
class dog(Animal):
    def speak(self):
        return f"{self.name} barks"
class cat(Animal):
    def speak(self):
        return f"{self.name} meow"
animal = Animal("GenericAnimal")
p1 = dog("Emeliy")
p2 = cat("Barsik")
print(animal.speak())
print(p1.speak())
print(p2.speak())