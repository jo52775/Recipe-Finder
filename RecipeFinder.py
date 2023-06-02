import requests
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = "https://api.spoonacular.com/recipes/complexSearch?"

api_key = os.getenv("API_KEY")

#Ask user to set limitations on carbohydrates, cholesterol, and sugar
print("Please enter the maximum carbohydrates, cholesterol, and sugar that you want in a recipe: ")
print()
carbs = input("Max carbohydrates (in grams): ")
cholesterol = input("Max cholesterol (in milligrams): ")
sugar = input("Max sugar (in grams): ")
print()

url = BASE_URL + "&apiKey=" + api_key + "&maxCarbs=" + carbs + "&maxCholesterol=" + cholesterol + "&maxSugar=" + sugar

response = requests.get(url).json()

#Displaying recipes to user
print("Here are your recipe options: ")

dishTitles = []
for i in range(0,len(response['results'])):
    dishTitles.append(response['results'][i]['title'])


for i in range(0,len(dishTitles)):
     print(str((i+1)) + ". " + dishTitles[i])

#User chooses a recipe
recipe_num = int(input("Select a recipe number: "))
print()
for i in range(0,len(dishTitles)):
    if(recipe_num == i+1):
            selected_recipe = dishTitles[i]
            print("SELECTED RECIPE: " + selected_recipe)
            break
    
#Required ingredients for selected recipe are displayed to the user
#Firstly, by acquiring ID of selected recipe
for i in range(0, len(response['results'])):
     if(response['results'][i]['title'] == selected_recipe):
          recipe_id = response['results'][i]['id']
          break

#Generating ingredient information
url2 = "https://api.spoonacular.com/recipes/" + str(recipe_id) + "/ingredientWidget.json?" + "&apiKey=" + api_key 
response2 = requests.get(url2).json()

print() 
print()
print("INGREDIENTS: ")
print()
for i in range(0,len(response2['ingredients'])):
    print(response2['ingredients'][i]['name'])
    
    string_value = str(response2['ingredients'][i]['amount']['metric']['value'])
    string_unit = str(response2['ingredients'][i]['amount']['metric']['unit'])
    print("("+string_value + " "  + string_unit+")")
    print()

#Give user option to view similar recipes:
print()
print("View similar recipes: ")
url3 = "https://api.spoonacular.com/recipes/" + str(recipe_id) + "/similar?" + "&apiKey=" + api_key
response3 = requests.get(url3).json()

similarDishes = []
for i in range(0,len(response3)):
    similarDishes.append(response3[i]['title'])


for i in range(0,len(similarDishes)):
     print(str((i+1)) + ". " + similarDishes[i])
