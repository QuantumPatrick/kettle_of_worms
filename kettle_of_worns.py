from random import randint

num_statements = int(input("How many statements do you want? "))

animal_file = open("animals.txt", "r")
animal_set = list()
for line in animal_file:
    line = line.strip()
    animal_set.append(line)

container_file = open("containers.txt", "r")
container_set = list()
for line in container_file:
    line = line.strip()
    container_set.append(line)

print()

for i in range(num_statements):
    animal_num = randint(0, len(animal_set) - 1)
    container_num = randint(0, len(container_set) - 1)
    
    print(container_set[container_num], "of", animal_set[animal_num])
    print()
    print()