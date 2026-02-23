import json
import math

def priority_score(item):
    pass

def producing_score(item):
    pass

def load_data_from_level(game_level):
    with open("json/level.json", "r") as f:
        levelData = json.load(f)

    unlockedAnimals = []
    unlockedCrops = []
    unlockedProducts = []
    unlockedMachines = []
    unlockedTrees = []
    for level in levelData:
        if game_level<int(level):
            break
        curLevel = levelData[level]
        for infoType in curLevel:
            if infoType == "animal":
                unlockedAnimals.append(curLevel[infoType])
            elif infoType == "machine":
                unlockedMachines.append(curLevel[infoType])
            elif infoType == "crops":
                crops = curLevel[infoType]
                for crop in crops:
                    unlockedCrops.append(crop)
            elif infoType == "products":
                products = curLevel[infoType]
                for product in products:
                    unlockedProducts.append(product)
            elif infoType == "tree":
                trees = curLevel[infoType]
                for fruit in trees:
                    unlockedTrees.append(fruit)
            else:
                raise TypeError(f"{infoType} is  of Unknown type")


    return unlockedAnimals, unlockedCrops, unlockedProducts, unlockedMachines, unlockedTrees

def configure_machines(machines,products):
    with open("json/machine.json", "r") as f:
        machineData = json.load(f)
    machine_configurations ={}
    for machine in machines:
        availableProduce = []
        thisMachineData = machineData[machine]

        thisMachine = {"slots":machineData[machine]["slots"]}
        for produce in thisMachineData["produce"]:
            if produce in products:
                availableProduce.append(produce)
        thisMachine["produce"] = availableProduce
        machine_configurations[machine] = thisMachine

    return machine_configurations

def count_animals(animals):
    animal_count = {}

    for animal in animals:
        if animal == "Chicken":
            count = 6
        elif animal == "Goat":
            count = 4
        else:
            count = 5

        animal_count[animal] = animal_count.get(animal, 0) + count

    return animal_count

def calculate_feed(animals):
    cropsForFeed = {}
    with open("json/feed.json", "r") as f:
        feedData = json.load(f)
    for animal in animals:
        feed=feedData[animal]
        feedToMake = math.ceil(animals[animal]/3)
        for crop in feed:
            cropsForFeed[crop] = cropsForFeed.get(crop, 0) + feed[crop]*feedToMake
    return cropsForFeed

def calculate_field_size(game_level):
    fieldCount = 3
    if game_level<50:
        fieldCount+=math.ceil((game_level/2)*3)
    elif game_level<100:
        fieldCount+=75+math.ceil((game_level-50)/2*2)
    else:
        fieldCount+=125+math.ceil((game_level-100)/2)
    return fieldCount

def get_raw_material(item, raw_materials):
    with open("json/recipe.json", "r") as f:
        recipeData = json.load(f)
    for material in recipeData[item]:
        print(material,recipeData[item][material])
        if material in recipeData:
            get_raw_material(material,raw_materials)
        else:
            raw_materials[material]=raw_materials.get(material,0)+recipeData[item][material]

def max_profit(machine):
    slots = machine["slots"]
    products = machine["products"]

def find_work_range(machine):
    pass

def calculate_storage_factor(item):
    pass

if __name__ == "__main__":
    inputLevel = 20
    checkinInterval = 4
    availableAnimals, availableCrops, availableProducts, availableMachines, availableTrees = load_data_from_level(inputLevel)
    #print(f"Loading till level {inputLevel}. SUCCESS\nAnimals{availableAnimals}\nCrops{availableCrops}\nProducts{availableProducts}\nMachines{availableMachines}\nTrees{availableTrees}")
    configured_machines = configure_machines(availableMachines,availableProducts)
    print(configured_machines)
    animalCount = count_animals(availableAnimals)
    feed_required = calculate_feed(animalCount)
