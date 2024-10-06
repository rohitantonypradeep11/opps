class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
jeffrey = parrot("jeffery",7)
print("jeffrey is a {}".format(jeffrey.species))
print("{} is {} years old".format(jeffrey.name,jeffrey.age))