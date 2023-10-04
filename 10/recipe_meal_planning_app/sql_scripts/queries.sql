-- Ingredients needed for Spaghetti Bolognese
SELECT i.ingredient_name, ri.quantity, ri.unit FROM RecipeIngredients ri JOIN Ingredients i ON ri.ingredient_id = i.ingredient_id WHERE ri.recipe_id = 1;

-- Recipes included in Week 1 meal plan
SELECT r.recipe_name FROM PlanRecipes pr JOIN Recipes r ON pr.recipe_id = r.recipe_id WHERE pr.plan_id = 1;

-- Different cuisines available in recipes
SELECT DISTINCT cuisine FROM Recipes;
