from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Dictionary to store recipes
recipes = {}

# Pydantic model for a recipe
class Recipe(BaseModel):
    name: str
    description: str
    ingredients: List[str]
    instructions: List[str]

# 1. Get all recipes
@app.get("/recipes", response_model=List[Recipe])
def get_recipes():
    return list(recipes.values())

# 2. Create a new recipe
@app.post("/recipes", response_model=Recipe)
def create_recipe(recipe: Recipe):
    if recipe.name in recipes:
        raise HTTPException(status_code=400, detail="Recipe already exists")
    recipes[recipe.name] = recipe
    return recipe

# 3. Delete a recipe
@app.delete("/recipes/{recipe_name}", response_model=Recipe)
def delete_recipe(recipe_name: str):
    if recipe_name not in recipes:
        raise HTTPException(status_code=400, detail="Recipe does not exist")
    # Delete the recipe and return the deleted recipe
    deleted_recipe = recipes.pop(recipe_name)
    return deleted_recipe

# 4. Update an existing recipe
@app.put("/recipes/{recipe_name}", response_model=Recipe)
def update_recipe(recipe_name: str, updated_recipe: Recipe):
    if recipe_name not in recipes:
        raise HTTPException(status_code=400, detail="Recipe does not exist")
    # Update the recipe
    recipes[recipe_name] = updated_recipe
    return updated_recipe
