bocadillo = {
    'ingredients': ('jamón', 'pan', 'queso', 'tomate'),
    'meal': "almuerzo",
    'prep_time': 10
}

tarta = {
    'ingredients': ('harina', 'azúcar', 'huevos'),
    'meal': "postre",
    'prep_time': 60
}

ensalada = {
    'ingredients': ('aguacate', 'rúcula', 'tomates', 'espinacas'),
    'meal': "almuerzo",
    'prep_time': 15
}

cookbook = {
    'bocadillo': bocadillo,
    'tarta': tarta,
    'ensalada': ensalada,
}


def printCookbook(cookbook):
    print('The current CookBook is: ')
    for i in cookbook:
        print(f'{i}')
    # selections()


def printDetails(receta):
    for k in receta:
        print(k, ':', receta[k])
    # selections()


def removeName(receta):
    if receta in cookbook:
        cookbook.pop(receta)
    # selections()


def createRecipe():

    # name = input("Please enter the name: ")
    nombre = input("Please enter the name: ")

    ingredients = input("\nPlease enter the ingredientes separated by coma: ")
    meal = input("\nPlease enter the type of meal. Ex. Breakfast, Lunch: ")
    prep_time = input("\nPlease enter the preparation time: ")

    # cookbook[nombre] = nombre 

    nombre = {
        'ingredients': {ingredients},
        'meal': meal,
        'prep_time': prep_time
    }
    print(cookbook)

    
    # print(nombre)
    # print(ensalada)

    # print(name)

    # selections()

# def selections():
#     selection = input("Welcome to the Python Cookbook !\nList of available option:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\nYour Choise:")
#     if selection == '1':
#         createRecipe()
#     elif selection == '2':
#         selection = input("What is the name of the recipie you want to see? ")
#         removeName(selection)
#     elif selection == '3':
#         selection = input("What is the name of the recipie you want to see? ")
#         printDetails(selection)
#     elif selection == '4':
#         printCookbook(cookbook)
#     elif selection == '5':
#         print('Cookbook closed. Goodbye !')
#         exit()

# selections()

# TEST
createRecipe()
# removeName(selection)
# printDetails(selection)
# printCookbook(cookbook)
