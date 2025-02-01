class robots:
    species = "Robot"
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
tom = robots("Tom", "model1")
jerry = robots("Jerry", "model2")

print("Tom is a {}".format(tom.species))
print("Jerry is also a  {}".format(jerry.species))
print("{} is {}".format(tom.name,tom.model))
print("{} is {}".format(jerry.name,jerry.model))