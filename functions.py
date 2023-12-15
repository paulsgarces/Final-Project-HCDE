import requests
from keys import spoonapikey

def searchrecipes(ingredients):
    base_url = 'https://api.spoonacular.com/recipes/findByIngredients'
    searchparams = {'ingredients': ingredients, 'apiKey': spoonapikey, 'number': 10, 'limitLicense': True, 'ranking': 1, 'ignorePantry': False}

    try:
        recipoutput = requests.get(base_url, params=searchparams)
        recipes = recipoutput.json()
        return recipes
    except requests.exceptions.RequestException as err:
        print("Error: {}".format(err))
        return None

def analyzedinstructions(recipe_id):
    base_url = f'https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions'
    analyzedparams = {'apiKey': spoonapikey}

    try:
        ingroutput = requests.get(base_url, params=analyzedparams)
        instructions = ingroutput.json()
        return instructions
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
        return None