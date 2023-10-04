-- Recipes
INSERT INTO Recipes (recipe_name, cuisine, instructions) VALUES ('Spaghetti Bolognese', 'Italian', 'Cook pasta. Prepare sauce. Combine.');
INSERT INTO Recipes (recipe_name, cuisine, instructions) VALUES ('Chicken Curry', 'Indian', 'Cook chicken. Prepare curry sauce. Combine.');

-- Ingredients
INSERT INTO Ingredients (ingredient_name) VALUES ('Pasta');
INSERT INTO Ingredients (ingredient_name) VALUES ('Tomato Sauce');
INSERT INTO Ingredients (ingredient_name) VALUES ('Chicken');
INSERT INTO Ingredients (ingredient_name) VALUES ('Curry Sauce');

-- RecipeIngredients
INSERT INTO RecipeIngredients (recipe_id, ingredient_id, quantity, unit) VALUES (1, 1, 100, 'grams');
INSERT INTO RecipeIngredients (recipe_id, ingredient_id, quantity, unit) VALUES (1, 2, 200, 'ml');
INSERT INTO RecipeIngredients (recipe_id, ingredient_id, quantity, unit) VALUES (2, 3, 150, 'grams');
INSERT INTO RecipeIngredients (recipe_id, ingredient_id, quantity, unit) VALUES (2, 4, 200, 'ml');

-- MealPlans
INSERT INTO MealPlans (plan_name) VALUES ('Week 1');

-- PlanRecipes
INSERT INTO PlanRecipes (plan_id, recipe_id) VALUES (1, 1);
INSERT INTO PlanRecipes (plan_id, recipe_id) VALUES (1, 2);
