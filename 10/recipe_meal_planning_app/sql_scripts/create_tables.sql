CREATE TABLE Recipes (
    recipe_id INTEGER PRIMARY KEY,
    recipe_name TEXT NOT NULL,
    cuisine TEXT NOT NULL,
    instructions TEXT NOT NULL
);

CREATE TABLE Ingredients (
    ingredient_id INTEGER PRIMARY KEY,
    ingredient_name TEXT NOT NULL
);

CREATE TABLE RecipeIngredients (
    recipe_id INTEGER,
    ingredient_id INTEGER,
    quantity REAL NOT NULL,
    unit TEXT NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES Recipes(recipe_id),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id)
);

CREATE TABLE MealPlans (
    plan_id INTEGER PRIMARY KEY,
    plan_name TEXT NOT NULL,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE PlanRecipes (
    plan_id INTEGER,
    recipe_id INTEGER,
    FOREIGN KEY (plan_id) REFERENCES MealPlans(plan_id),
    FOREIGN KEY (recipe_id) REFERENCES Recipes(recipe_id)
);
