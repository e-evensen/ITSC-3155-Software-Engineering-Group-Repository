
from tkinter import *
import pandas as pd 
import numpy as np
import requests
import collections 

df = pd.read_excel(r'/Users/jordanmcqueen/Documents/GitHub/ITSC-3155-Software-Engineering-Group-Repository/Random-Cocktail-Recipe/InventoryData (1).xlsx')
def get_recipe():


    # Get the ingredients from the text box
    
    
    

    COCKTAIL_ENDPOINT = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    response = requests.get(COCKTAIL_ENDPOINT)
    response.raise_for_status()
    data = response.json()['drinks']


    
    
    # Get the list of ingredients
    ingredients_list = []
    for num in range(1, 16):
        item = f"strIngredient{num}"
        cocktail_ingredient = data[0][item]
        if cocktail_ingredient is not None:
            add = f"{num}. {cocktail_ingredient}"
            ingredients_list.append(add)

       
    A = pd.DataFrame(ingredients_list)
    A.columns = ['Ingredients']
    A.to_csv('ingredients.csv')
    
    B = pd.DataFrame(df['ProductName'])

    B.columns = ['ProductNames']
    B.to_csv('inventory.csv')
    
    
          
         


    

    # Get cocktail name
    cocktail_name = data[0]["strDrink"]
    name_label.config(text=cocktail_name)

    # Get cocktail status
    cocktail_status = data[0]["strAlcoholic"]
    status_label.config(text=f"{cocktail_status} Cocktail")

    # Get cocktail instruction
    cocktail_instruction = data[0]['strInstructions']
    canvas.itemconfig(instruction, text=cocktail_instruction)

    

    # Get ingredients measurements
    measurement_list = []
    for num in range(1, 16):
        measure = f"strMeasure{num}"
        cocktail_measurement = data[0][measure]
        if cocktail_measurement is not None:
            measurement_list.append(cocktail_measurement)

    # combine the two lists
    ingredients.delete(0, END)
    ingredients.insert(1, "The Cocktail Recipe: ")
    combine_dict = {k: v for k, v in zip(ingredients_list, measurement_list)}
    num = 1
    for info in combine_dict:
        num += 1
        m = combine_dict[info]
        data = f"{info} / {m}"
        print(data)
        ingredients.insert(num, data)


# UI setup
interface = Tk()
interface.title("A3AJAGBE RANDOM COCKTAIL RECIPE")
interface.config(padx=30, pady=30)

FONT = ("Courier", 40, "bold")
SUB_FONT = ("Courier", 20, "normal")
TEXT = ("Courier", 15, "italic")
COLOR = "#cc6699"

# Interface Layout

name_label = Label(text="", fg=COLOR, font=FONT)
name_label.grid(row=0, column=0, columnspan=2)

status_label = Label(text="", font=SUB_FONT)
status_label.grid(row=1, column=0, columnspan=2)

canvas = Canvas(width=500, height=200, bg=COLOR)
instruction = canvas.create_text(250, 100, text="", width=450, font=TEXT, fill="white")
canvas.grid(row=2, column=0, columnspan=2)

ingredients = Listbox(width=40, font=TEXT)
ingredients.insert(END, "")
ingredients.grid(row=3, column=0, columnspan=2, pady=20)

button = Button(text="Next", fg=COLOR, width=20, command=get_recipe)
button.config(highlightthickness=0, padx=5, pady=5, font=SUB_FONT)
button.grid(row=4, column=0, columnspan=2)

get_recipe()

# Keep the screen open until exited
interface.mainloop()
