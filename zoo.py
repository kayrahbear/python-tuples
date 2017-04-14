zoo = ("Tiger", "Giraffe", "Panda", "Penguin", "Elephant")
print(zoo)

print("Tiger" in zoo)

(Tiger, Giraffe, Panda, Penguin, Elephant) = zoo
print(Tiger)
print(zoo)

zoo_list = list(zoo)
print(zoo_list)

zoo_list.extend(["Monkey", "Dinosaur", "Gibbon"])
print(zoo_list)

zoo = tuple(zoo_list)
print(zoo)