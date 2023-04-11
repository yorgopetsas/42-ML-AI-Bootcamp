import os

os.system('clear')

cookbook = [
        {
            'name' : 'bocadillo',
            'ingredients': ['jamón', 'pan', 'queso', 'tomate'],
            'meal': "almuerzo",
            'prep_time': 10
        }, 
        {
            'name' : 'tarta',
            'ingredients': ['harina', 'azúcar', 'huevos'],
            'meal': "postre",
            'prep_time': 60
        }, 
        {
            'name' : 'salad',
            'ingredients': ['aguacate', 'rúcula', 'tomates', 'espinacas'],
            'meal': "almuerzo",
            'prep_time': 15
        }
    ]


def addRecipe():
    name = input("Please enter the name: ")
    ingredients = input("\nPlease enter the ingredientes separated by coma: ")
    meal = input("\nPlease enter the type of meal. Ex. Breakfast, Lunch: ")
    prep_time = input("\nPlease enter the preparation time in minutes. Maximum time 240 min: ")
    new_recipe = {'name': name, 'ingredients': [ingredients], 'meal': meal, 'prep_time': prep_time}
    cookbook.append(new_recipe)
    for i in range(len(cookbook)):
        if cookbook[i]['name'] == name:
            print(f"\nRecipe {name.upper()} was created\n")


def removeRecipe(yz_rm):
    status = 0
    for i in range(len(cookbook)):
        if cookbook[i - 1]['name'] == yz_rm:
            del cookbook[i - 1]
            print('\nRecipe Deleted!\n')
            status = 1
    if status == 0:
        print(f'\nRecipe with name {yz_rm.upper()} does not exist, please try again.\n')



def printRecipe(recipe):
    status = 0
    for i in range(len(cookbook)):
        if cookbook[i - 1]['name'] == recipe:
            status = 1
            dict = cookbook[i - 1]
            print()
            for key, value in dict.items():
                if key == "ingredients":
                    print("ingredients: ", end="")
                    for i in value:
                        print(f"{i}, ", end="")    
                    print()
                else:
                    print(key,":", value)
            print()
    if status == 0:
        print(f'\nRecipe with name {recipe.upper()} does not exist, please try again.\n')


def printCookbook():
    print('\nThe CookBook has the following recipies:\n')
    for i, _ in enumerate(cookbook):
        print(cookbook[i]['name'])
    print()


def selection_control(selection):
    if selection == 1:
        os.system('clear')
        addRecipe()
    elif selection == 2:
        ipt = input("\nPlease write the name of the recipe you want to delete: ")
        os.system('clear')
        removeRecipe(ipt)
    elif selection == 3:
        ipt = input("\nPlease write the name of the recipe you want to view: ")
        os.system('clear')
        printRecipe(ipt)
    elif selection == 4:
        os.system('clear')
        printCookbook()
    elif selection == 5:
        print("\nCookbook closed. Goodbye !\n")
        quit()


def menu():
    selection = input("Please select an option:\n\n\t1: Add a recipe\n\t2: Delete a recipe\n\t3: Print a recipe\n\t4: Print the Cookbook\n\t5: Quit\nYour Choice is: ")
    if selection.isdigit() == False:
        print("Only numbers accepted. Please try again:\n")
        menu()
    elif selection.isdigit() == True:
        selection = int(selection)
        if selection not in range(1, 6):
            print("Please select a number from 1 to 5:\n")
            menu()
        else:
            selection_control(selection)


if __name__ == "__main__":
    status = 0
    selection = 0
    print("Welcome to the Python Cookbook! ", end="")
    while status == 0:
        menu()
