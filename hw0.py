from flask import Flask, render_template, request
from functions import searchrecipes, analyzedinstructions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    ingredients = request.form['ingredients']
    recipes = searchrecipes(ingredients)
    return render_template('results.html', recipes=recipes)

@app.route('/recipe/<int:recipe_id>')
def get_instructions(recipe_id):
    instructions = analyzedinstructions(recipe_id)
    return render_template('instructions.html', instructions=instructions)