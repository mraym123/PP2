class Father:
    def skills(self):
        return "Gardening, Programming"

class Mother:
    def skills(self):
        return "Cooking, Art"

class Child(Father, Mother):
    def skills(self):
        father_skills = super().skills()
        mother_skills = Mother.skills(self)
        return f"{father_skills}, {mother_skills}"

child = Child()
print(child.skills())
